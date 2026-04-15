import sqlite3
import pandas as pd
import os
import torch
import warnings
import re
import random
from transformers import AutoModelForMaskedLM, AutoTokenizer, DataCollatorForLanguageModeling
from transformers import Trainer, TrainingArguments, EarlyStoppingCallback, set_seed
from datasets import Dataset

# FIX CRITIQUE : Force l'utilisation d'un seul GPU pour éviter le bug de réplication (StopIteration)
# fréquent avec les modèles Large et DataParallel sur certaines versions de PyTorch.
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

set_seed(42)
warnings.filterwarnings("ignore")

# 1. Terminologie Ludologique SOTA (évite la fragmentation par le tokenizer)
GAMING_TOKENS = [
    "roguelike", "metroidvania", "soulslike", "gacha", "moba", "mmorpg", 
    "battle-royale", "bullet-hell", "deckbuilder", "permadeath", "procedural",
    "sandbox", "open-world", "multiplayer", "single-player", "co-op", "pve", 
    "pvp", "crafting", "stealth", "turn-based", "isometric", "first-person", 
    "third-person", "top-down", "side-scroller", "hack-and-slash", "loot-box"
]

def prepare_sota_data(db_path):
    """Extraction et augmentation sémantique par permutation (Gururangan et al., 2020)"""
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"Base de données SQLite introuvable : {db_path}")
    
    conn = sqlite3.connect(db_path)
    print("Extraction du corpus sémantique depuis la DB Steam...")
    
    query = """
    SELECT g.name, 
           GROUP_CONCAT(DISTINCT gen.label) as genres,
           GROUP_CONCAT(DISTINCT t.label) as tags,
           GROUP_CONCAT(DISTINCT c.label) as categories,
           (SELECT name FROM studios JOIN developers ON studios.id = developers.studio_id WHERE developers.game_id = g.id LIMIT 1) as developer
    FROM games g
    LEFT JOIN game_genre gg ON g.id = gg.game_id LEFT JOIN genres gen ON gg.genre_id = gen.id
    LEFT JOIN game_tag gt ON g.id = gt.game_id LEFT JOIN tags t ON gt.tag_id = t.id
    LEFT JOIN game_category gc ON g.id = gc.game_id LEFT JOIN categories c ON gc.category_id = c.id
    GROUP BY g.id
    """
    df = pd.read_sql_query(query, conn)
    conn.close()

    def generate_diverse_text(row):
        # Technique SOTA : Ordre aléatoire des attributs pour forcer l'apprentissage sémantique pur
        name = str(row['name'])
        blocks = []
        if row['genres']: blocks.append(f"belongs to the {row['genres']} genres")
        if row['developer']: blocks.append(f"was crafted by {row['developer']}")
        if row['categories']: blocks.append(f"features {row['categories']} modes")
        if row['tags']: blocks.append(f"is defined by the concepts of {row['tags']}")
        
        random.shuffle(blocks)
        paragraph = f"{name} is a title that {' and '.join(blocks)}."
        return paragraph.lower()

    print(f"Génération de {len(df)} descriptions augmentées pour RoBERTa...")
    df['text'] = df.apply(generate_diverse_text, axis=1)
    return Dataset.from_pandas(df[['text']])

# MODÈLE SOTA : RoBERTa-Large (355M paramètres) pour une richesse sémantique maximale
MODEL_NAME = "roberta-large" 
OUTPUT_DIR = "./models/bert-gaming-adapted"

def main():
    if not os.path.exists("./models"): os.makedirs("./models")

    print(f"Chargement du modèle de pointe : {MODEL_NAME}")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    tokenizer.add_tokens(GAMING_TOKENS)
    
    model = AutoModelForMaskedLM.from_pretrained(MODEL_NAME)
    model.resize_token_embeddings(len(tokenizer))

    dataset = prepare_sota_data('data/2024-12-13.steam.db')
    
    print("Tokenization du corpus...")
    tokenized_dataset = dataset.map(
        lambda x: tokenizer(x["text"], truncation=True, padding="max_length", max_length=128),
        batched=True,
        remove_columns=["text"]
    ).train_test_split(test_size=0.05, seed=42)

    data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=True, mlm_probability=0.15)

    # Configuration d'entraînement SOTA (DAPT)
    training_args = TrainingArguments(
        output_dir="./bert-gaming-checkpoints",
        num_train_epochs=3,
        per_device_train_batch_size=8,    # Ajusté pour RoBERTa-Large (VRAM)
        gradient_accumulation_steps=8,    # Simule un batch size global de 64
        learning_rate=2e-5,               # Taux d'apprentissage plus bas pour les modèles Large
        lr_scheduler_type="cosine",       # Décroissance cosinusoïdale pour une convergence fine
        warmup_ratio=0.1,                 # 10% de warmup pour stabiliser les nouveaux tokens
        weight_decay=0.01,
        eval_strategy="steps",
        eval_steps=500,
        save_steps=1000,
        logging_steps=100,
        fp16=torch.cuda.is_available(),   # Mixed Precision (Essentiel sur CUDA)
        load_best_model_at_end=True,
        metric_for_best_model="loss",
        report_to="none"
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        data_collator=data_collator,
        train_dataset=tokenized_dataset['train'],
        eval_dataset=tokenized_dataset['test'],
        callbacks=[EarlyStoppingCallback(early_stopping_patience=2)]
    )

    print(f"Lancement du Fine-Tuning SOTA sur {torch.cuda.get_device_name(0)}...")
    trainer.train()

    print(f"Sauvegarde du modèle adapté dans {OUTPUT_DIR}...")
    trainer.save_model(OUTPUT_DIR)
    tokenizer.save_pretrained(OUTPUT_DIR)
    print("Processus terminé. Le modèle RoBERTa-Large est prêt pour le clustering.")

if __name__ == "__main__":
    main()
