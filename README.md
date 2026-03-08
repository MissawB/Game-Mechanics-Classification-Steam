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

L'approche est structurée en huit étapes clés, allant de l'exploration initiale à l'analyse diachronique :

1. **Exploration de la Base de Données** : Analyse initiale de la structure SQLite et premières extractions de règles d'association via l'algorithme FP-Growth.
2. **Taxonomie du Gameplay** : Restructuration sémantique basée sur le *Video Game Metadata Schema* (VGMS), mappant les tags dans 8 dimensions (Genre, Mechanics, Theme, Setting, etc.).
3. **Analyse de Réseau & Co-occurrence** : Visualisation des affinités de design en utilisant le **Lift** pour identifier les corrélations significatives entre mécaniques et genres.
4. **Clustering Folksonomique** : Découverte de structures émergentes via divers algorithmes (Louvain, OPTICS, K-Medoids) pour identifier les "genres réels" pratiqués par les joueurs.
5. **Validation Expert vs Folksonomie** : Confrontation des classifications officielles de Steam avec les tags utilisateurs pour démontrer la plus-value descriptive de la folksonomie.
6. **Classification par Machine Learning** : Modélisation prédictive (Random Forest, XGBoost) pour automatiser la classification des jeux.
7. **Enrichissement NLP & Deep Learning** : Utilisation de **Sentence-BERT** pour le nommage automatique des clusters et l'analyse sémantique profonde.
8. **Ontologie & Analyse Diachronique** : Construction d'une hiérarchie de genres (Subsumption) et mesure de la dérive sémantique (PMI) pour cartographier l'évolution du langage des joueurs.

---

## 🛠️ Stack Technique

* **Data & Analyse** : `Pandas`, `NumPy`, `SQLite`
* **Visualisation & Réseau** : `Matplotlib`, `Seaborn`, `NetworkX`, `Plotly` (3D interactive)
* **Machine Learning** : `Scikit-learn`, `XGBoost`, `imbalanced-learn` (SMOTE), `mlxtend` (FP-Growth)
* **Deep Learning & NLP** : `Sentence-Transformers` (S-BERT), `PyTorch`, `Transformers`
* **Environnement** : `Jupyter Notebook`

---

## 📂 Structure du Dépôt

```text
├── analysis/           # Notebooks Jupyter (étapes 1 à 8 du pipeline)
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


| **Auteur(s)** | **Titre** | **Apport dans le Projet** |
| :--- | :--- | :--- |
| **Windleharth et al.** (2016) | *Full Steam Ahead* | Taxonomie VGMS (Video Game Metadata Schema). |
| **Elias et al.** (2012) | *Characteristics of Games* | Analyse structurelle des systèmes de jeux. |
| **Li & Zhang** (2020) | *Network Analysis on Steam Tags* | Méthodologie d'analyse de réseau de co-occurrence. |
| **Adrian et al.** (2015) | *ConTag: Semantic Tag Recommendation* | Inspiration pour le système de recommandation sémantique. |
| **Lu, Park, & Hu** (2010) | *User tags vs expert-assigned terms* | Comparaison Folksonomie vs Experts (Notebook 5). |
| **Lee et al.** (2014) | *Video Game Metadata Schema* | Validation des dimensions de classification. |
| **Sanderson & Croft** (1999) | *Deriving concept hierarchies from text* | Algorithme de Subsumption pour la hiérarchie des tags. |
| **Hamilton et al.** (2016) | *Diachronic Word Embeddings...* | Mesure de la dérive sémantique via le PMI. |
| **Hsu** (2006) | *Jacks of all trades...* | Concept d'Entropie de Shannon pour mesurer l'hybridité. |
| **Aarseth et al.** (2003) | *A multidimensional typology of games* | Fondements de la classification multidimensionnelle. |
| **Swink** (2009) | *Game Feel: A Game Designer's Guide* | Définition des mécaniques et de la boucle de gameplay. |

## 🔗 Ressources Externes

**Bibliographie complète** : Retrouvez l'ensemble de nos sources sur notre [Librairie Zotero Groupée](https://www.zotero.org/groups/6288352/pdr_stearn/library).
