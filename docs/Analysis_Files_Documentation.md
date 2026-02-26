# Documentation des Fichiers d'Analyse - Classification des Mécaniques Steam

## Introduction
Ce document détaille la raison d'être et la méthodologie de chaque fichier présent dans le répertoire `analysis/`, ainsi que les rapports de validation associés. L'objectif global est de transformer une folksonomie non-supervisée (tags Steam) en une base de données de mécaniques de jeu structurée, validée par des métriques de cohérence et enrichie par des modèles de Machine Learning. Le projet couvre désormais plus de 126 000 jeux uniques.

## Description des Fichiers d'Analyse

### 1. First_Data_Base_Analysis.ipynb
**Rôle :** Exploration initiale et structuration de la base de données SQLite.
- Identifie les tables clés (ex : `games`, `tags`, `game_tag`).
- Analyse la distribution brute des tags et la représentativité des jeux.
- Première tentative d'extraction de règles d'association via l'algorithme FP-Growth.

### 2. Gameplay_Tag_Taxonomy.ipynb
**Rôle :** Restructuration sémantique et enrichissement de la taxonomie (Axe 1 & 3).
- **Base théorique :** S'appuie sur le *Video Game Metadata Schema* (VGMS).
- **Action :** Filtre le bruit (tags de distribution), normalise les variantes (ex: Rogue-like vs Roguelike) et mappe les tags dans 8 dimensions ludologiques (Genre, Mechanics, Theme, Setting, Mood, Aesthetics, Perspective, Players).
- **Sortie :** Génère `data/Games_Gameplay_Taxonomy.csv`, la base de référence consolidée.

### 3. Network_Analysis_Cooccurrence.ipynb
**Rôle :** Analyse de réseau et affinités de design (Axe 2).
- **Méthodologie :** Calcule la co-occurrence entre Genres et Mécaniques.
- **Indicateur :** Utilisation du **Lift** pour identifier les corrélations non-aléatoires (affinités de design réelles).
- **Visualisation :** Graphe d'affinités montrant comment les mécaniques gravitent autour des genres dominants et identification de pôles structurels (Action-RPG, Réflexion, Narration).
- **Note :** Cette étape valide la cohérence de la taxonomie avant le clustering profond.

### 4. Folksonomic_Clustering_Analysis.ipynb
**Rôle :** Découverte de structures émergentes (Axe 2 & Modèle Elverdam/Aarseth).
- **Approche :** Utilise la similarité de cosinus entre les tags pour cartographier l'espace de design.
- **Méthodes de Clustering :**
    - **Algorithme de Louvain :** Détection de communautés basée sur la structure du graphe.
    - **Dendrogramme :** Clustering hiérarchique avec seuil de coupure visuel (Ward distance) pour identifier les niveaux d'agrégation.
    - **GMM (Gaussian Mixture Model) :** Approche probabiliste pour la gestion des chevauchements.
    - **OPTICS :** Détection de clusters basée sur la densité, permettant d'isoler le bruit (tags non-structurels).
    - **K-Medoids (PAM) :** Identification de tags "médoides" représentatifs pour chaque cluster de gameplay.
- **Objectif :** Identifier des "Genres Folksonomiques" basés sur l'usage réel des joueurs.

### 5. Expert_vs_Folksonomy_Comparison.ipynb
**Rôle :** Validation de la folksonomie par rapport aux classifications officielles.
- **Action :** Compare les genres officiels Steam (Experts) et les tags utilisateurs (Folksonomie).
- **Conclusion :** Démontre la plus-value descriptive des joueurs sur les mécaniques fines et l'ambiance, validant l'utilité du projet.

### 6. Machine_Learning_Classification.ipynb
**Rôle :** Modélisation prédictive de la classification des jeux.
- **Objectif :** Prédire le genre principal d'un jeu à partir de ses autres attributs (mécaniques, thèmes, etc.).
- **Modèles :** Random Forest, XGBoost et Voting Classifier.
- **Techniques :** Gestion du déséquilibre des classes via SMOTE et optimisation des hyperparamètres (GridSearch/RandomizedSearch).

## Rapports de Validation et de Synthèse

Le répertoire `reports/` contient des documents de synthèse sur l'évolution de la base :

- **classification_consistency_report.md :** Analyse de la couverture sur les jeux de 2025 et identification des tags émergents.
- **classification_update_report.md :** Synthèse des mesures de normalisation et de la fusion des datasets (126 244 jeux uniques).

## Dépendances
Le fichier `requirements.txt` à la racine du projet contient l'ensemble des bibliothèques nécessaires (Pandas, Scikit-learn, NetworkX, XGBoost, etc.).
