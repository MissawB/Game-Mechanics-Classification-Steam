# Rapport de Cohérence de la Classification des Tags Steam

## 1. Vue d'Ensemble
Ce test a été effectué sur les jeux sortis après le **13 décembre 2024** (date de la dernière base de données de référence).
- **Nombre total de nouveaux jeux extraits** : 25 862

## 2. Statistiques de Couverture
La taxonomie actuelle (basée sur VGMS) a été appliquée à ces nouveaux jeux. Voici le taux de complétion par dimension :

| Dimension | Jeux Couverts | Pourcentage |
| :--- | :--- | :--- |
| **Aesthetics** | 5 608 | 21.68% |
| **Genre** | 6 373 | 24.64% |
| **Mechanics** | 4 885 | 18.89% |
| **Mood** | 4 192 | 16.21% |
| **Perspective** | 3 281 | 12.69% |
| **Players** | 5 455 | 21.09% |
| **Setting** | 1 011 | 3.91% |
| **Theme** | 5 280 | 20.42% |

**Note** : Le faible taux de couverture (comparé aux ~100% sur l'ancien dataset) s'explique par le fait que les jeux très récents ont souvent peu ou pas de tags utilisateur ("folksonomie") au moment de l'extraction.

## 3. Incohérences et Lacunes Identifiées

### A. Écarts de Typographie (Synonymes non capturés)
Certains tags très fréquents ne sont pas capturés à cause de tirets ou de variations orthographiques :
- `Rogue-like` (703 occurrences) vs `Roguelike` (Taxonomie)
- `Rogue-lite` (700 occurrences) vs `Roguelite` (Taxonomie)
- `Base-Building` (363 occurrences) vs `Base Building` (Taxonomie)
- `Puzzle-Platformer` (276 occurrences) vs `Puzzle Platformer` (Taxonomie)

### B. Tags Importants Absents de la Taxonomie
Plusieurs tags de gameplay ou thématiques fréquents ne sont pas encore classés dans nos dimensions :
- `Exploration` (1535 occurrences)
- `Cute` (1355 occurrences)
- `Horror` (1042 occurrences)
- `Arcade` (939 occurrences)
- `Comedy` (498 occurrences)
- `Hidden Object` (442 occurrences)
- `Dungeon Crawler` (357 occurrences)

### C. Dépendance aux Tags Utilisateurs
Nous avons identifié des jeux (ex: *Maze Quest VR*) qui possèdent des **Genres** officiels Steam (Action, Early Access) mais **aucun Tag**. Comme notre classification repose exclusivement sur les tags pour plus de granularité, ces jeux se retrouvent avec une classification vide.

## 4. Recommandations
1. **Normalisation** : Ajouter les variantes avec tirets (`Rogue-like`) dans le dictionnaire de mapping.
2. **Expansion** : Intégrer `Exploration` (Mechanics), `Horror` (Genre/Mood) et `Cute` (Aesthetics/Mood) dans la taxonomie.
3. **Fallback** : Utiliser la colonne `Genres` de Steam comme solution de repli lorsque la liste de `Tags` est vide.
