import pandas as pd
import kagglehub
from kagglehub import KaggleDatasetAdapter
import os

# 1. Configuration de la Taxonomie (VGMS) et des Mappings
taxonomy = {
    "Genre": [
        "Strategy", "Tower Defense", "City Builder", "Sandbox", "Roguelike", "Roguelite", "Traditional Roguelike",
        "Survival", "Tactical", "Management", "Platformer", "Action", "2D Platformer", "Adventure", "Casual",
        "Interactive Fiction", "Point & Click", "Puzzle", "Simulation", "Visual Novel", "Dating Sim",
        "Character Action Game", "Immersive Sim", "Turn-Based Strategy", "Life Sim", "Music", "Creature Collector",
        "Racing", "Flight", "Runner", "RPG", "Party-Based RPG", "Turn-Based", "2D Fighter", "3D Fighter",
        "Action RPG", "3D Platformer", "God Game", "RTS", "Real Time Tactics", "CRPG", "Walking Simulator",
        "Metroidvania", "Survival Horror", "JRPG", "Card Battler", "Deckbuilding", "Card Game", "Roguelike Deckbuilder",
        "Action-Adventure", "MMORPG", "Choose Your Own Adventure", "FPS", "Third-Person Shooter", "Shooter",
        "Space Sim", "Beat 'em up", "Hack and Slash", "Turn-Based Tactics", "Tactical RPG", "Battle Royale",
        "Arena Shooter", "Bullet Hell", "Hero Shooter", "Shoot 'Em Up", "Top-Down Shooter", "Action Roguelike",
        "Puzzle Platformer", "Rhythm", "Strategy RPG", "Otome", "Auto Battler", "Trading Card Game", "Word Game",
        "Automobile Sim", "Match 3", "4X", "Grand Strategy", "Action RTS", "Board Game", "Wargame", "MOBA",
        "Fighting", "Twin Stick Shooter", "Mystery Dungeon", "eSports", "Farming Sim", "Political Sim", "Solitaire",
        "Trivia", "Colony Sim", "Medical Sim", "Boomer Shooter", "Extraction Shooter", "Boss Rush", "Social Deduction",
        "Job Simulator", "Outbreak Sim", "Musou", "Hobby Sim",
        # New Genres
        "Horror", "Dungeon Crawler", "Arcade", "Sports"
    ],
    "Mechanics": [
        "Procedural Generation", "Grid-Based Movement", "Base Building", "Building", "Level Editor",
        "Character Customization", "Investigation", "Collectathon", "Idler", "Physics", "Crafting",
        "Controller", "Open World", "Resource Management", "Clicker", "Inventory Management", "Choices Matter",
        "Artificial Intelligence", "Multiple Endings", "Gun Customization", "Music-Based Procedural Generation",
        "Turn-Based Combat", "Logic", "Automation", "Hacking", "Economy", "Diplomacy", "6DOF", "Sokoban",
        "Time Management", "Vehicular Combat", "Loot", "Mining", "Destruction", "Mechs", "Score Attack",
        "Escape Room", "Stealth", "Bullet Time", "Time Travel", "Mouse only", "On-Rails Shooter", "Lemmings",
        "Parkour", "Hunting", "Open World Survival Craft", "Dynamic Narration", "Minigames", "Quick-Time Events",
        "Addictive", "Time Manipulation", "Real-Time", "Real-Time with Pause", "Social Deduction", "Dice",
        "Intentionally Awkward Controls", "Tile-Matching", "Jump Scare",
        # New Mechanics
        "Exploration", "Hidden Object"
    ],
    "Theme": [
        "Fantasy", "LEGO", "Futuristic", "Cyberpunk", "Supernatural", "Detective", "Mystery", "Sexual Content",
        "Nudity", "Mature", "NSFW", "Hentai", "Romance", "Anime", "Family Friendly", "Nature", "Zombies",
        "Medieval", "Tabletop", "Sci-fi", "Post-apocalyptic", "War", "Historical", "Demons", "Psychedelic",
        "Werewolves", "Gothic", "Vampire", "Cats", "Aliens", "Drama", "Emotional", "Dark Fantasy", "Combat",
        "Swordplay", "Robots", "LGBTQ", "Magic", "Underground", "Dystopian", "Dragons", "Education", "Programming",
        "Steampunk", "Mythology", "Science", "Dark Humor", "Superhero", "America", "Memes", "Parody",
        "Philosophical", "Lovecraftian", "Pirates", "Capitalism", "Faith", "Blood", "Classic", "Ninja", "Assassin",
        "Noir", "Abstract", "Dwarf", "Dinosaurs", "Conspiracy", "Illuminati", "Politics", "Comic Book", "Crime",
        "Villain Protagonist", "Satire", "Agriculture", "Nostalgia", "Medical", "Cold War", "Vikings", "Dog",
        "Farming", "Dungeons & Dragons", "Warhammer 40K", "Gambling", "Transhumanism", "Based On A Novel", "Fox"
    ],
    "Setting": [
        "Space", "Underwater", "Modern", "1980s", "1990's", "America", "Rome", "Mars", "Cold War"
    ],
    "Mood": [
        "Atmospheric", "Dark", "Psychological Horror", "Funny", "Relaxing", "Cozy", "Wholesome", "Ambient",
        "Gore", "Surreal", "Story Rich", "Psychedelic", "Psychological", "Difficult", "Stylized", "Emotional",
        "Lore-Rich", "Dark Humor", "Cinematic", "Dark Comedy", "Beautiful", "Short", "Unforgiving", "Experimental",
        "Addictive",
        # New Moods
        "Cute", "Comedy", "Thriller"
    ],
    "Aesthetics": [
        "Minimalist", "Pixel Graphics", "Colorful", "3D", "2D", "Cartoon", "Cartoony", "Stylized", "FMV",
        "Hand-drawn", "Old School", "3D Vision", "Voxel", "2.5D", "Abstract", "Retro", "8-bit Music", "Instrumental Music",
        "Rock Music", "Electronic Music"
    ],
    "Perspective": [
        "Isometric", "First-Person", "Third Person", "Side Scroller", "Top-Down"
    ],
    "Players": [
        "Singleplayer", "Multiplayer", "Online Co-Op", "PvE", "Massively Multiplayer", "Co-op", "PvP",
        "Co-op Campaign", "Team-Based", "Local Co-Op", "Local Multiplayer", "4 Player Local", "Split Screen",
        "Competitive", "Asynchronous Multiplayer"
    ]
}

# Inversion du dictionnaire pour le mapping
tag_to_category = {}
for category, tags in taxonomy.items():
    for tag in tags:
        tag_to_category[tag] = category

# Normalisation des variantes typographiques
normalizations = {
    "Rogue-like": "Roguelike",
    "Rogue-lite": "Roguelite",
    "Base-Building": "Base Building",
    "Puzzle-Platformer": "Puzzle Platformer",
    "Text-Based": "Interactive Fiction"
}

# Chemins relatifs au script
base_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Chargement de la Base Initiale
print("Chargement de la base initiale...")
initial_taxonomy_path = os.path.join(base_dir, "../data/Games_Gameplay_Taxonomy.csv")
df_initial = pd.read_csv(initial_taxonomy_path)

# On retire game_release_date pour correspondre au format de New_Games_Gameplay_Taxonomy.csv
if 'game_release_date' in df_initial.columns:
    df_initial = df_initial.drop(columns=['game_release_date'])

# 3. Chargement des Nouveaux Jeux depuis Kaggle
print("Téléchargement et chargement du dataset Kaggle...")
# Le dataset Kaggle contient 'games.csv'
kaggle_file = "games.csv"
df_kaggle = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    "fronkongames/steam-games-dataset",
    kaggle_file,
    pandas_kwargs={'index_col': False}
)

# 4. Filtrage des Nouveaux Jeux (après le 13 décembre 2024)
print("Filtrage des nouveaux jeux...")
df_kaggle['Release date'] = pd.to_datetime(df_kaggle['Release date'], errors='coerce')
cutoff_date = pd.to_datetime('2024-12-13')
df_new_games = df_kaggle[df_kaggle['Release date'] > cutoff_date].copy()

# 5. Transformation et Classification
print(f"Classification de {len(df_new_games)} nouveaux jeux...")

def process_tags(row):
    # Fallback: utiliser Genres si Tags est vide
    tags_raw = str(row['Tags']) if pd.notna(row['Tags']) else ""
    if tags_raw == "" or tags_raw.lower() == "nan":
        tags_raw = str(row['Genres']) if pd.notna(row['Genres']) else ""
    
    if not tags_raw:
        return {cat: None for cat in taxonomy.keys()}
    
    # Séparation et normalisation
    tags_list = [t.strip() for t in tags_raw.split(',')]
    normalized_tags = [normalizations.get(t, t) for t in tags_list]
    
    # Classification
    result = {cat: [] for cat in taxonomy.keys()}
    for t in normalized_tags:
        cat = tag_to_category.get(t)
        if cat:
            result[cat].append(t)
            
    # Formatage en chaînes de caractères
    return {cat: ", ".join(list(dict.fromkeys(tags))) if tags else None for cat, tags in result.items()}

# Application du traitement
processed_data = df_new_games.apply(process_tags, axis=1, result_type='expand')

# Reconstruction du DataFrame pour les nouveaux jeux
df_new_structured = pd.DataFrame({
    'game_id': df_new_games['AppID'],
    'game_name': df_new_games['Name']
})
df_new_structured = pd.concat([df_new_structured, processed_data], axis=1)

# 6. Fusion et Sauvegarde
print("Fusion des bases de données...")
# S'assurer que les colonnes sont dans le même ordre
dimensions = ["Aesthetics", "Genre", "Mechanics", "Mood", "Perspective", "Players", "Setting", "Theme"]
cols_order = ["game_id", "game_name"] + dimensions

df_initial = df_initial[cols_order]
df_new_structured = df_new_structured[cols_order]

df_final = pd.concat([df_initial, df_new_structured], ignore_index=True)

# Dédoublonnage (par nom au cas où les AppIDs diffèrent du format game_id initial)
# On garde la version la plus récente (celle de Kaggle) en cas de doublon de nom
df_final = df_final.drop_duplicates(subset=['game_name'], keep='last')

output_path = os.path.join(base_dir, "../data/New_Games_Gameplay_Taxonomy.csv")
df_final.to_csv(output_path, index=False)
print(f"Base complète sauvegardée dans {output_path} ({len(df_final)} jeux)")

# 7. Génération du Sample de Test (15k)
print("Génération de l'échantillon de test (15 000 jeux)...")
df_sample = df_final.sample(n=min(15000, len(df_final)), random_state=42)
sample_path = os.path.join(base_dir, "../data/final_test_set_15k.csv")
df_sample.to_csv(sample_path, index=False)
print(f"Échantillon de test sauvegardé dans {sample_path}")
print("Terminé !")
