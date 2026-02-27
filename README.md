# 🎮 Steam Folksonomy Analysis & Game Mechanics Classification

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Data Science](https://img.shields.io/badge/Data-Science-orange.svg)](https://pandas.pydata.org/)
[![Machine Learning](https://img.shields.io/badge/Machine-Learning-green.svg)](https://scikit-learn.org/)
[![NLP](https://img.shields.io/badge/NLP-Deep--Learning-red.svg)](https://sbert.net/)

## 📌 Présentation du Projet
Ce projet de recherche explore comment les **folksonomies** (systèmes de tags collaboratifs) peuvent être exploitées pour classifier les jeux vidéo au-delà des catégories marketing traditionnelles. En analysant les données de plus de **126 000 jeux Steam**, nous cherchons à transformer un système de tags bruité en une structure de métadonnées ludologiques fiable et précise.

### ❓ Problématique
> **"Comment exploiter une folksonomie utilisateur non-supervisée et bruitée (les tags Steam) afin d’établir des règles d’association fiables permettant de caractériser les mécaniques de jeu ?"**

---

## 🚀 Pipeline d'Analyse
L'approche est structurée en sept étapes clés, allant de l'exploration initiale à l'enrichissement par Deep Learning :

1.  **Exploration de la Base de Données** : Analyse initiale de la structure SQLite et premières extractions de règles d'association via l'algorithme FP-Growth.
2.  **Taxonomie du Gameplay** : Restructuration sémantique basée sur le *Video Game Metadata Schema* (VGMS), mappant les tags dans 8 dimensions (Genre, Mechanics, Theme, Setting, etc.).
3.  **Analyse de Réseau & Co-occurrence** : Visualisation des affinités de design en utilisant le **Lift** pour identifier les corrélations significatives entre mécaniques et genres.
4.  **Clustering Folksonomique** : Découverte de structures émergentes via divers algorithmes (Louvain, OPTICS, K-Medoids) pour identifier les "genres réels" pratiqués par les joueurs.
5.  **Validation Expert vs Folksonomie** : Confrontation des classifications officielles de Steam avec les tags utilisateurs pour démontrer la plus-value descriptive de la folksonomie.
6.  **Classification par Machine Learning** : Modélisation prédictive (Random Forest, XGBoost) pour automatiser la classification des jeux.
7.  **Enrichissement NLP & Deep Learning** : Utilisation de **Sentence-BERT** pour le nommage automatique des clusters et l'analyse sémantique profonde.

---

## 🛠️ Stack Technique
*   **Data & Analyse** : `Pandas`, `NumPy`, `SQLite`
*   **Visualisation & Réseau** : `Matplotlib`, `Seaborn`, `NetworkX`, `python-louvain`
*   **Machine Learning** : `Scikit-learn`, `XGBoost`, `imbalanced-learn` (SMOTE), `mlxtend` (FP-Growth)
*   **Deep Learning & NLP** : `Sentence-Transformers` (S-BERT), `PyTorch`, `Transformers`
*   **Environnement** : `Jupyter Notebook`

---

## 📂 Structure du Dépôt
```text
├── analysis/           # Notebooks Jupyter (étapes 1 à 7 du pipeline)
├── data/               # Bases de données SQLite et exports CSV (Taxonomie)
├── docs/               # Documentation détaillée des fichiers et méthodologie
├── reports/            # Rapports de synthèse et de cohérence
├── scripts/            # Scripts de pré-traitement et utilitaires
├── biblio/             # Ressources académiques
└── requirements.txt    # Dépendances du projet
```

---

## 📚 État de l'Art 
Le projet s'appuie sur des travaux académiques de référence :

| Auteur(s) | Titre | Apport Principal |
|-----------|-------|------------------|
| Lu, Park, & Hu | *User tags vs expert-assigned terms* | Comparaison folksonomie vs experts |
| Windleharth et al. | *Full Steam Ahead* | Analyse conceptuelle des tags Steam |
| Li & Zhang | *Network analysis on steam game tags* | Méthodologie de visualisation & clustering |
| Elverdam & Aarseth | *Game Classification as Game Design* | Modèle de classification multidimensionnel |
| Lee et al. | *Video Game Metadata Schema* | Validation du schéma de métadonnées |
| Adrian et al. | *ConTag: A Semantic Tag Recommendation System* | Inspiration pour l'algorithme de suggestion |

## 🔗 Ressources Externes
**Bibliographie complète** : Retrouvez l'ensemble de nos sources sur notre [Librairie Zotero Groupée](https://www.zotero.org/groups/6288352/pdr_stearn/library).
