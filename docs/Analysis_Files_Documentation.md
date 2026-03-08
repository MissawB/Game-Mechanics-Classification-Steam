# Documentation des Fichiers d'Analyse - Classification des Mécaniques Steam

## Introduction
Ce document détaille la raison d'être et la méthodologie de chaque fichier présent dans le répertoire `analysis/`, ainsi que les rapports de validation associés. L'objectif global est de transformer une folksonomie non-supervisée (tags Steam) en une base de données de mécaniques de jeu structurée, validée par des métriques de cohérence et enrichie par des modèles de Machine Learning. Le projet couvre désormais plus de 126 000 jeux uniques.

## Description des Fichiers d'Analyse

### 1. First_Data_Base_Analysis.ipynb
**Rôle :** Exploration initiale de la folksonomie Steam.
- Identifie les tables clés de la base SQLite originale (`games`, `tags`, `game_tag`).
- Analyse la distribution des tags (Loi de Pareto) et identifie le bruit initial.
- **Règles d'association :** Première extraction de relations fortes via l'algorithme **FP-Growth** (ex: liens NSFW/Hentai isolés du gameplay).

### 2. Gameplay_Tag_Taxonomy.ipynb
**Rôle :** Restructuration sémantique et création de la taxonomie de référence.
- **Base théorique :** S'appuie sur le *Video Game Metadata Schema* (VGMS) et les travaux de Windleharth et al.
- **Action :** Filtre les tags de distribution, normalise les variantes (Rogue-like vs Roguelike) et classe les tags dans 8 dimensions (Genre, Mechanics, Theme, Setting, Mood, Aesthetics, Perspective, Players).
- **Sortie :** Génère `data/Games_Gameplay_Taxonomy.csv`.

### 3. Network_Analysis_Cooccurrence.ipynb
**Rôle :** Analyse de réseau et affinités de design.
- **Méthodologie :** Utilise le **Lift** pour identifier les corrélations non-aléatoires entre dimensions.
- **Topologie :** Identification de trois écosystèmes distincts (Puzzles, Visual Novels, et le "Grand Continent" Roguelike/RPG).
- **Centralité :** Repère les tags "Hubs" (Sandbox, Management) et les "Ponts" (Strategy, Turn-Based Combat).
- **Analyse Temporelle :** Évolution de la popularité des genres et mécaniques de 2010 à 2025.

### 4. Folksonomic_Clustering_Analysis.ipynb
**Rôle :** Découverte de genres émergents par clustering non-supervisé.
- **Approche :** Similarité de cosinus sur la présence des tags.
- **Méthodes :** 
    - **Algorithme de Louvain :** Détection de 42 communautés sémantiques.
    - **Validation :** Score de Silhouette, Index Davies-Bouldin et test de **stabilité par Bootstrap**.
- **Exploration :** Visualisation **t-SNE 3D interactive** et analyse de la "longue traîne" via OPTICS (détection du bruit).
- **Temporalité :** Suivi de l'émergence et de la croissance des clusters dans le temps.

### 5. Expert_vs_Folksonomy_Comparison.ipynb
**Rôle :** Étude du fossé entre classifications officielles et perception des joueurs.
- **Action :** Compare les genres officiels (Experts) et les tags (Folksonomie).
- **Richesse :** Démontre que les joueurs apportent 1.6x plus d'informations descriptives que les experts.
- **Accord Temporel :** Mise en évidence d'un **fossé grandissant** : les joueurs sont de moins en moins d'accord avec les étiquettes officielles sur les jeux récents.
- **Mapping :** Heatmap de correspondance montrant comment les genres officiels se projettent sur les réalités du gameplay folksonomique.

### 6. Machine_Learning_Classification.ipynb
**Rôle :** Modélisation prédictive du genre principal.
- **Ingénierie :** Encodage multi-hot et **sélection de caractéristiques via test Chi2** (réduction du bruit).
- **Modèles :** Random Forest, XGBoost et **Stacking Classifier** (méta-modèle Gradient Boosting).
- **Rigueur :** Utilisation de la **Validation Croisée Stratifiée** et gestion du déséquilibre des classes via SMOTE.
- **Diagnostic :** Analyse de l'importance des caractéristiques pour chaque grand genre.

### 7. NLP_Deep_Learning_Enrichment.ipynb
**Rôle :** Analyse sémantique fine par Embeddings.
- **Technologie :** Utilisation de modèles **Transformer (BERT)** avancés (`all-mpnet-base-v2`).
- **Nommage Automatique :** Identification des labels de clusters par calcul de centroïde sémantique.
- **Cohérence :** Analyse de la variance intra-cluster et détection des **outliers sémantiques** (tags mal classés).
- **Relations :** Heatmap de similarité entre clusters pour identifier les **Super-Genres**.

### 8. Ontology_and_Diachronic_Analysis.ipynb
**Rôle :** Vers une Ontologie Dynamique du Gameplay (Axe de recherche final).
- **Hiérarchisation (Subsumption) :** Application de la règle de Sanderson & Croft (1999) pour identifier les relations Parent-Enfant. Mise en évidence des genres "piliers" (Action, Shooter, RPG) et de leurs sous-genres (ex: Shooter -> FPS).
- **Analyse Diachronique (Spéciation) :** Mesure de la dérive sémantique par le **PMI (Pointwise Mutual Information)** sur la période 2010-2025. Étude de cas sur l'autonomisation du genre *Roguelite* par rapport au *Roguelike*.
- **Complexité Sémantique :** Utilisation de l'**Entropie de Shannon** pour quantifier l'hybridité des jeux (moyenne de 0.95), illustrant la tendance à la fusion des genres dans le design moderne.

## Scripts de Traitement et Maintenance

### New_Games_Gameplay_Taxonomy_Creation.py
**Rôle :** Pipeline d'automatisation et mise à jour de la base.
- **Source :** Extraction Kaggle (Steam Games Dataset).
- **Logique :** Filtrage post-2024, application de la taxonomie enrichie (Horror, Exploration, etc.), normalisation automatique et stratégie de repli (Fallback) sur les genres officiels si les tags sont absents.
- **Livrables :** `New_Games_Gameplay_Taxonomy.csv` et `final_test_set_15k.csv`.
- **Scripts additionnels :** `Generate_Cluster_Validation_Tasks.py` permet de générer des échantillons de validation pour un crowdsourcing (évaluation de l'accord inter-juges).

## Dépendances
Le fichier `requirements.txt` contient l'ensemble des bibliothèques nécessaires (Pandas, Scikit-learn, NetworkX, XGBoost, mlxtend, sentence-transformers, plotly, etc.).

## Bibliographie et Références Scientifiques
*   **Aarseth, E. et al. (2003).** *A multidimensional typology of games.*
*   **Hamilton, W. L. et al. (2016).** *Diachronic Word Embeddings Reveal Statistical Laws of Semantic Change.* (Utilisé pour l'approche PMI de la dérive sémantique).
*   **Hsu, G. (2006).** *Jacks of all trades and masters of none: Audiences' reactions to spanning genres in feature film production.* (Utilisé pour le concept de complexité sémantique et l'Entropie de Shannon).
*   **Li, Q., & Zhang, J. (2015).** *Folksonomy-based genre classification of video games.*
*   **Lu, Y. et al. (2010).** *Expert vs. Folksonomy Classification: A Comparison Study.*
*   **Sanderson, M., & Croft, B. (1999).** *Deriving concept hierarchies from text.* (Utilisé pour l'algorithme de Subsumption).
*   **Windleharth, T. W. et al. (2016).** *Full Steam Ahead: A conceptual analysis of user-supplied tags on Steam.* (Utilisé pour la taxonomie VGMS de base).
