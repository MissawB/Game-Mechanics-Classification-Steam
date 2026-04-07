# 🎮 Steam Gameplay Taxonomy & Computational Ludology

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B.svg)](https://streamlit.io/)
[![Machine Learning](https://img.shields.io/badge/ML-Stacking--Ensemble-green.svg)](https://scikit-learn.org/)
[![NLP](https://img.shields.io/badge/NLP-BERT--Embeddings-red.svg)](https://sbert.net/)

## 📌 Présentation du Projet
Ce projet de recherche en **ludologie computationnelle** explore la structure profonde du game design à travers le prisme de la **folksonomie de Steam**. En analysant les données de plus de **126 000 jeux**, nous transformons la "sagesse des foules" (tags utilisateurs) en une **ontologie multidimensionnelle** rigoureuse, validée par des cadres théoriques académiques.

### ❓ La Question de Recherche
> **"Comment passer d'une folksonomie utilisateur bruitée à une ontologie structurée des mécaniques de jeu capable de modéliser l'évolution du design et l'hybridité des genres ?"**

---

## 🚀 Fonctionnalités Clés

*   **📊 Dashboard Interactif** : Une interface **Streamlit** pour explorer les réseaux d'affinités, les cartes sémantiques et les évolutions temporelles.
*   **🧬 Taxonomie VGMS** : Structuration du gameplay en 8 dimensions (Genre, Mechanics, Theme, Mood, Aesthetics, Perspective, Setting, Players).
*   **🤖 Classification Avancée** : Pipeline de Machine Learning utilisant un **Stacking Classifier** (Random Forest + XGBoost) avec équilibrage de classes par **SMOTE**.
*   **🧠 Sémantique Profonde** : Utilisation de **BERT** (`all-mpnet-base-v2`) pour aligner l'usage social des tags avec leur sens linguistique.
*   **📈 Analyse Diachronique** : Modélisation de la "spéciation" des genres (ex: Roguelike vs Roguelite) via le **PMI** temporel et l'**Entropie de Shannon**.

---

## 🛠️ Installation et Utilisation

### 1. Installation
```bash
git clone https://github.com/votre-repo/Game-Mechanics-Classification-Steam.git
cd Game-Mechanics-Classification-Steam
pip install -r requirements.txt
```

### 2. Lancer l'Exploration (Dashboard)
```bash
streamlit run dashboard.py
```

### 3. Pipeline de Mise à Jour (Nouveaux Jeux)
```bash
python scripts/New_Games_Gameplay_Taxonomy_Creation.py
```

---

## 🔬 Méthodologie en 8 Étapes

Le projet est articulé autour de 8 notebooks de recherche (`analysis/`) :

1.  **Exploration** : Nettoyage de la donnée et extraction de motifs via **FP-Growth**.
2.  **Taxonomie** : Mapping sémantique vers le standard **VGMS**.
3.  **Réseaux** : Calcul du **Lift** pour cartographier les affinités de design.
4.  **Clustering** : Détection de communautés via l'**Algorithme de Louvain**.
5.  **Comparaison** : Quantification du fossé sémantique entre **Experts (Éditeurs)** et **Foule (Joueurs)**.
6.  **ML** : Validation de la structure via la prédiction automatisée (Accuracy ~51% en multi-label).
7.  **NLP** : Analyse de la cohérence sémantique par embeddings BERT.
8.  **Ontologie** : Création de hiérarchies par **Subsumption** ($P(Parent|Enfant) \ge 0.8$).

---

## 📂 Architecture du Dépôt

```text
├── analysis/           # Notebooks de recherche (étapes 1 à 8)
├── data/               # Bases SQLite (126k jeux) et Exports CSV
├── docs/               # Documentation détaillée et définitions théoriques
├── reports/            # Rapports de validation et de cohérence
├── scripts/            # Pipelines de production, modèles BERT et ML
├── dashboard.py        # Interface Streamlit interactive
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

---

## 🔗 Liens et Documentation
*   **Documentation Complète** : [docs/Analysis_Files_Documentation.md](docs/Analysis_Files_Documentation.md)
*   **Définitions Ludologiques** : [docs/Ludological_Terms_Definitions.md](docs/Ludological_Terms_Definitions.md)
*   **Bibliographie** : Retrouvez nos sources sur notre [Librairie Zotero](https://www.zotero.org/groups/6288352/pdr_stearn/library).

---
*Projet de recherche "Game Mechanics Classification Steam" - 2025-2026*
