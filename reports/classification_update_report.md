# Rapport de Modification : Normalisation et Consolidation de la Taxonomie

## 1. Améliorations de la Taxonomie (Mapping)
La taxonomie a été enrichie pour combler les lacunes identifiées lors de l'analyse des nouveaux jeux :
- **Expansion des Dimensions** :
    - **Genre** : Ajout de `Horror`, `Dungeon Crawler`, `Arcade`, `Sports`.
    - **Mechanics** : Ajout de `Exploration`, `Hidden Object`.
    - **Mood** : Ajout de `Cute`, `Comedy`, `Thriller`.
- **Normalisation Automatique** : Mise en place d'un moteur de transformation pour unifier les variantes typographiques :
    - `Rogue-like` / `Rogue-lite` -> `Roguelike` / `Roguelite`
    - `Base-Building` -> `Base Building`
    - `Puzzle-Platformer` -> `Puzzle Platformer`
    - `Text-Based` -> `Interactive Fiction`

## 2. Fiabilisation du Processus d'Intégration
Pour résoudre l'hétérogénéité des données entre l'ancienne base et les nouveaux jeux Steam :
- **Gestion du Bruit** : Exclusion systématique des tags non informatifs pour le gameplay (`Indie`, `Early Access`, `Free to Play`, `Violent`).
- **Stratégie de Repli (Fallback)** : Pour les jeux récents n'ayant pas encore de tags "folksonomiques", le script utilise désormais les **Genres officiels Steam** comme source secondaire pour garantir une classification minimale.

## 3. Consolidation des Données
Les deux jeux de données ont été fusionnés pour créer un référentiel unique :
- **Base Initiale** : 100 384 jeux.
- **Nouveaux Jeux** : 25 862 jeux (sortis après le 13/12/2024).
- **Total Après Dédoublonnage** : **126 244 jeux uniques** classifiés.

## 4. Livrables Générés
- **`data/New_Games_Gameplay_Taxonomy.csv`** : La nouvelle base de référence complète, nettoyée et normalisée.
- **`data/final_test_set_15k.csv`** : Échantillon aléatoire de **15 000 jeux** extrait de la base totale, optimisé pour servir de set de validation pour les modèles de classification ou les analyses statistiques.
