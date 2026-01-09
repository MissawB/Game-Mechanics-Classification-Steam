# 🎮 Steam Folksonomy Analysis & Game Mechanics Classification

## 📌 Présentation du Projet
Ce projet de recherche vise à explorer comment les folksonomies (systèmes de tags collaboratifs) peuvent être exploitées pour classifier les jeux vidéo au-delà des catégories marketing traditionnelles.

### ❓ Problématique
  **"Comment exploiter une folksonomie utilisateur non-supervisée et bruitée (les tags Steam) afin d’établir des règles d’association fiables permettant de caractériser les mécaniques de jeu ?"**

## 🚀 Objectifs et Méthodologie
L'approche s'articule autour de quatre axes majeurs basés sur la littérature scientifique :
1. **Traitement du Bruit Sémantique** : Identification et exclusion des "troll tags" et des biais d'humour propres à Steam pour obtenir des données propres.
2. **Analyse de Réseau** : Utilisation de matrices de co-occurrence pour visualiser les clusters de jeux et les liens entre les tags.
3. **Taxonomie Multidimensionnelle** : Distinction structurelle entre les tags de Gameplay (mécaniques) et les tags de Thème (narratif).
4. **Système de Recommandation** : Développement d'un algorithme capable de suggérer des catégories basées sur des règles d'association extraites de la folksonomie.

## 🛠️ Stack Technique
* **Langage** : Python (NLP & Data Analysis)
* **Base de données** :             (Stockage des extractions API)
* **Modélisation** : Algorithmes d'extraction de règles d'association
  
## 📚 État de l'Art 
Le projet s'appuie sur des travaux académiques de référence :

| Auteur(s) | Titre | Apport Principal | Application au Projet |
|-----------|-------|------------------|-----------------------|
| Caimei Lu, Jung-ran Park, Xiaohua Hu| *User tags versus expert-assigned subject terms: A comparison of LibraryThing tags and Library of Congress Subject Headings* | Comparaison de la folksonomie par rapport aux tags d'experts | Prétraitement des données |
| Travis W. Windleharth, Jacob Jett, Marc Schmalz, Jin Ha Lee | *Full Steam Ahead: A Conceptual Analysis of User-Supplied Tags on Steam* | Analyse conceptuelle des tags Steam | Nettoyage des données |
| Xiaozhou Li, Boyang Zhang | *A preliminary network analysis on steam game tags: another way of understanding game genres* |Analyse de réseau sur les tags | Méthodologie de visualisation & clustering |
| Christian Elverdam, Espen Aarseth | *Game Classification as Game Design: Construction Through Critical Analysis* | Modèle de classification multidimensionnel | Structuration de notre taxonomie |
| Jin Ha Lee, Andrew Perti, Rachel ivy Clarke, Travis W. Windleharth | *Video Game Metadata Schema* | Schéma de métadonnées vidéo-ludiques | Validation du schéma de la base de donnée |
| Benjamin Adrian, Leo Sauermann, Thomas Roth-Berghofer | *ConTag: A Semantic Tag Recommendation System* | Système de recommandation ConTag | Inspiration pour l'algorithme de suggestion |

📂 Structure du Dépôt

    ├── data/               # Schémas SQLite et données brutes (API Steam)
    ├── scripts/            # Scripts de pré-traitement et nettoyage (NLP)
    ├── analysis/           # Notebooks Jupyter (Analyse de réseau & Graphes)
    ├── docs/               # Documentation détaillée de la taxonomie
    └── README.md           # Présentation du projet

## 🔗 Ressources Externes
**Bibliographie complète** : Retrouvez l'ensemble de nos sources sur notre [Librairie Zotero Groupée](https://www.google.com/search?q=https://www.zotero.org/groups/6288352/pdr_stearn/library).
