# Documentation Scientifique et Technique : Ontologie Dynamique du Gameplay Steam

## 1. Vision et Contexte de Recherche
Ce projet s'inscrit dans le champ de la **ludologie computationnelle** et des **sciences de l'information**. Il part d'un constat critique : les classifications traditionnelles des jeux vidéo (genres marketing comme "Action" ou "Aventure") sont devenues insuffisantes pour décrire la complexité et l'hybridité du design contemporain.

L'objectif est de construire une **ontologie multidimensionnelle** en exploitant la "sagesse des foules" (folksonomie Steam) et de la valider par des cadres théoriques académiques. Nous passons d'une vision statique du genre à une vision dynamique basée sur les **affinités de mécaniques**.

---

## 2. État de l'Art et Fondements Théoriques

### A. Folksonomie vs Classification Expert
Le projet s'appuie sur les travaux de **Windleharth et al. (2016)** qui démontrent que les tags utilisateurs sur Steam, bien que "bruyants", capturent des nuances de gameplay (ex: "Permadeath", "Procedural Generation") que les métadonnées officielles ignorent. Nous explorons le concept de "fossé sémantique" entre la perception des joueurs et les étiquettes des éditeurs (**Lu et al., 2010**).

### B. Le Schéma VGMS (Video Game Metadata Schema)
Pour structurer les données, nous utilisons le standard **VGMS (Lee et al., 2013)**. Ce schéma propose 8 dimensions fondamentales (Genre, Mechanics, Theme, Mood, Aesthetics, Perspective, Setting, Players) qui permettent de décomposer un jeu en unités sémantiques atomiques.

### C. Ontologie et Hiérarchie
Nous appliquons les principes de **Zagal et al. (2005)** sur l'ontologie des jeux pour définir les relations de dépendance entre mécaniques. L'algorithme de subsumption de **Sanderson & Croft (1999)** est utilisé pour extraire automatiquement les hiérarchies basées sur les probabilités conditionnelles.

### D. Analyse Diachronique et Dérive Sémantique
Le projet utilise les lois statistiques du changement sémantique de **Hamilton et al. (2016)** pour mesurer comment les concepts de gameplay évoluent dans le temps via le **PMI (Pointwise Mutual Information)** temporel.

---

## 3. Méthodologie : L'Approche Hybride (Data Science & Ludologie)

Le projet suit une pipeline de recherche rigoureuse en 5 phases :

### Phase I : Découverte et Nettoyage (`Notebook 1`)
- **Analyse de Pareto** : Identification des tags dominants et élimination de la "longue traîne" non-informative (seuil de présence < 1%).
- **FP-Growth** : Extraction des itemsets fréquents pour repérer les corrélations triviales (ex: *RPG* + *Fantasy*).

### Phase II : Structuration Taxonomique (`Notebook 2 & 3`)
- **Normalisation** : Correction des variantes orthographiques (ex: *Roguelike* vs *Rogue-like*).
- **Lift Sémantique** : $Lift(A, B) = \frac{P(A \cap B)}{P(A) \cdot P(B)}$. Cette métrique permet d'identifier les affinités de design qui transcendent la simple popularité brute des tags.

### Phase III : Validation par le Clustering (`Notebook 4 & 7`)
- **Clustering de Louvain** : Basé sur la modularité du graphe de co-occurrence. Validation par le **Score de Silhouette** et l'**Index de Davies-Bouldin**.
- **Embeddings BERT** : Utilisation du modèle `all-mpnet-base-v2` pour projeter les tags dans un espace vectoriel de 768 dimensions.
- **AMI (Adjusted Mutual Information)** : Mesure de la concordance entre la structure d'usage (joueurs) et la structure linguistique (modèle de langue).

### Phase IV : Modélisation Prédictive (`Notebook 6`)
- **Ingénierie de Features** : Sélection via **Test Chi2** pour identifier les descripteurs les plus discriminants par genre.
- **Ensemble Learning** : Utilisation d'un **Stacking Classifier** (Random Forest, XGBoost) avec équilibrage de classes par **SMOTE**.

### Phase V : Analyse de l'Ontologie et Hybridité (`Notebook 8`)
- **Subsumption Statistique** : Un tag $A$ est parent de $B$ si $P(A|B) \ge 0.8$ et $P(B|A) < 0.8$.
- **Entropie de Shannon** : $H = -\sum p_i \log_2(p_i)$ appliquée aux vecteurs de dimensions pour quantifier l'hybridité (mélange des genres) d'un titre.

---

## 4. Validation et Fiabilité

Le projet inclut des boucles de rétroaction pour assurer la pérennité de l'ontologie (voir dossier `reports/`) :

- **`classification_consistency_report.md`** : Analyse de la couverture sur les jeux récents (post-2024). Mesure la robustesse de la taxonomie face aux nouveaux titres.
- **`clustering_consistency_report.md`** : Calcul de l'**Indice de Rand Ajusté (ARI)** pour valider la stabilité des groupes sémantiques entre les différentes méthodes (Graphes vs NLP).
- **Stabilité par Bootstrap** : Les clusters de Louvain sont testés par ré-échantillonnage pour garantir que la structure n'est pas un artefact statistique local.

---

## 5. Architecture des Données

### Tables Sources (SQLite)
- `games` : AppID, Name, Release Date, Score.
- `game_tag` : Relation N-N entre jeux et tags.
- `game_genre` : Classifications officielles (Baseline Expert).

### Livrables de Recherche
- `data/Games_Gameplay_Taxonomy.csv` : Dataset pivot pour les futures études ludologiques.
- `data/Folksonomic_Clusters.csv` : Cartographie des 42 communautés de gameplay.

---

## 6. Guide des Analyses (Notebooks)

| Notebook | Focus Scientifique | Métriques Clés |
| :--- | :--- | :--- |
| `1_Basics` | Qualité de la donnée | Fréquence de Pareto, Règles d'association |
| `2_Taxonomy` | Standardisation | VGMS Mapping |
| `3_Network` | Affinités de design | Lift, Centralité de degré |
| `4_Clustering` | Taxonomie émergente | Modularité, Silhouette, DB Index |
| `5_Comparison` | Étude sociologique | Taux d'accord, Richesse descriptive |
| `6_ML` | Valeur prédictive | Accuracy, F1-Score, Confusion Matrix |
| `7_NLP` | Sémantique profonde | Cosine Similarity, Variance intra-cluster |
| `8_Ontology` | Théorie de l'évolution | PMI, Subsumption, Entropie de Shannon |

---

## 7. Bibliographie de Référence
- **Aarseth, E., et al. (2003)**. *A multidimensional typology of games*.
- **Hamilton, W. L., et al. (2016)**. *Diachronic Word Embeddings Reveal Statistical Laws of Semantic Change*.
- **Lee, Y., et al. (2013)**. *Video Game Metadata Schema: Standards for Content Description*.
- **Sanderson, M., & Croft, B. (1999)**. *Deriving concept hierarchies from text*.
- **Windleharth, T., et al. (2016)**. *Full Steam Ahead: A conceptual analysis of user-supplied tags on Steam*.
- **Zagal, J. P., et al. (2005)**. *Towards a Game Ontology*.
