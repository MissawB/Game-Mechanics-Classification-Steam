# Définitions Formelles des Termes Ludologiques

**Document de Référence basé sur :**

- **VGMS (Video Game Metadata Schema v4.1)** - Lee et al.
- **Full Steam Ahead: A Conceptual Analysis of User-Supplied Tags on Steam** - Windleharth et al.
- **Game Classification as Game Design Construction Theory** - Elverdam & Aarseth
- **Characteristics of Games** - Elias, Garfield, & Gutschera
- **Game Feel: A Game Designer's Guide to Virtual Sensation** - Swink
- **ConTag: A Semantic Tag Recommendation System for Video Games** - Adrian et al.

---

## 1. GAMEPLAY

### Définition Formelle (VGMS)

L'ensemble des **interactions et mécaniques** qui permettent au joueur d'atteindre les objectifs du jeu. C'est la couche fondamentale et opérationnelle de l'expérience ludique, décrivant *comment* le jeu se joue.

### Dimensions Constitutives

Le gameplay est caractérisé par 8 dimensions interdépendantes (basées sur le VGMS et Elverdam & Aarseth) :


| Dimension       | Rôle                                                         | Exemple                                  |
| --------------- | ------------------------------------------------------------- | ---------------------------------------- |
| **Genre**       | Classification primaire basée sur les mécaniques dominantes | RPG, FPS, Platformer                     |
| **Mechanics**   | Systèmes interactifs et règles de gameplay                  | Procedural Generation, Turn-Based Combat |
| **Theme**       | Univers narrative et contexte du jeu                          | Fantasy, Cyberpunk, Medieval             |
| **Setting**     | Localisation spatio-temporelle                                | Space, Modern, 1980s                     |
| **Mood**        | Tonalité émotionnelle et atmosphère                        | Atmospheric, Dark, Relaxing              |
| **Aesthetics**  | Présentation visuelle et sonore                              | Pixel Graphics, 3D, Hand-drawn           |
| **Perspective** | Point de vue du joueur                                        | First-Person, Third-Person, Isometric    |
| **Players**     | Configuration et mode de jeu                                  | Singleplayer, Multiplayer, Co-op         |

### Contexte du Projet

Dans cette analyse, le gameplay est **reconstruit à partir de la folksonomie Steam** en transformant les tags utilisateurs bruts en ces 8 dimensions structurées. Cela permet de dépasser la simple catégorisation marketing pour capturer les *affinités de design* réelles.

---

## 2. GENRE

### Définition Formelle

**Genre = Ensemble cohérent de mécaniques fondamentales qui définissent la boucle de gameplay primaire.**

Un genre est une **catégorie supérieure** qui regroupe les jeux partageant :

- Un **ensemble de règles fondamentales** (ex: dans un RPG, l'amélioration des statistiques du personnage)
- Une **boucle de gameplay** dominante (ex: exploration-combat-progression)
- Des **attentes d'expérience** communes pour les joueurs

### Fondement Théorique (Elverdam & Aarseth)

Le genre est une **construction socio-ludique** basée sur :

1. **L'histoire partagée** : les conventions reconnaissables par la communauté
2. **Les mécaniques dominantes** : ce qui définit vraiment la jouabilité
3. **Les attentes du joueur** : ce qu'il attend de "ce type" de jeu

### Exemples de Genres dans la Taxonomie


| Genre            | Mécaniques Dominantes                                           | Exemple de Jeu               |
| ---------------- | ---------------------------------------------------------------- | ---------------------------- |
| **RPG**          | Character progression, inventory, dialogue choices               | The Witcher 3, Baldur's Gate |
| **FPS**          | First-person perspective, real-time shooting, level design       | Doom, Half-Life              |
| **Platformer**   | Gravity, jumping, level traversal, precise controls              | Super Mario, Celeste         |
| **Strategy**     | Resource management, tactical positioning, turn-based/real-time  | Civilization, StarCraft      |
| **Roguelike**    | Procedural generation, permadeath, run-based progression         | Hades, The Binding of Isaac  |
| **Puzzle**       | Logic problems, sequential solutions, environmental interaction  | Portal, Tetris               |
| **Simulation**   | System modeling, resource management, realistic mechanics        | Cities: Skylines, Flight Sim |
| **Visual Novel** | Narrative focus, choice-based progression, branching stories     | Doki Doki Literature Club    |
| **MOBA**         | Team-based, objective focus, character specialization, real-time | League of Legends, Dota 2    |
| **Metroidvania** | Exploration, ability-gating, non-linear progression              | Hollow Knight, Castlevania   |

### Distinction Important (Windleharth et al.)

**Genre ≠ Thème**

- Genre = *Mécaniques* (comment on joue)
- Thème = *Univers* (dans quel monde on joue)

Un jeu de "rogue-like" peut être en thème Fantasy ou Sci-Fi.

### Note Méthodologique

Dans la folksonomie Steam, les **genres sont souvent mélangés avec les mécaniques** (ex: "Deckbuilding" peut être genre ou mécanique selon le contexte). Notre taxonomie distingue ces niveaux pour clarifier.

---

## 3. MECHANICS (Mécaniques)

### Définition Formelle

**Mechanics = Systèmes interactifs élémentaires et règles qui permettent au joueur d'accomplir des actions et d'affecter l'état du jeu.**

Une mécanique est une **règle jouable** observable et répétable, distinct du genre (qui est une **combinaison de mécaniques**).

### Trois Niveaux de Mécaniques (MDA Framework)


| Niveau               | Définition                                | Exemple                           |
| -------------------- | ------------------------------------------ | --------------------------------- |
| **Core Mechanics**   | Les actions élémentaires répétables    | Sauter, tirer, interagir          |
| **System Mechanics** | Interaction entre plusieurs core mechanics | Combat system, progression system |
| **Meta-Mechanics**   | Règles du jeu au niveau structurel        | Permadeath, procedural generation |

### Exemples de Mécaniques dans la Taxonomie


| Mécanique                | Description                                                     | Jeux Représentatifs        |
| ------------------------- | --------------------------------------------------------------- | --------------------------- |
| **Procedural Generation** | Génération algorithmique de contenu (maps, donjons, histoire) | No Man's Sky, Caves of Qud  |
| **Turn-Based Combat**     | Combat où les actions se déroulent au tour par tour           | XCOM, Divinity Original Sin |
| **Crafting**              | Création d'objets à partir de ressources collectées          | Minecraft, Valheim          |
| **Stealth**               | Éviter la détection, progression furtive                      | Hitman, Metal Gear Solid    |
| **Base Building**         | Construction et gestion d'une base/forteresse                   | Stronghold, Grounded        |
| **Loot**                  | Système de butin aléatoire, drops d'objets                    | Diablo, Borderlands         |
| **Choices Matter**        | Les décisions du joueur affectent la narration                 | Mass Effect, The Witcher 3  |
| **Time Manipulation**     | Contrôle du temps (ralenti, rembobinage, boucles)              | Braid, Life is Strange      |
| **Grid-Based Movement**   | Déplacement sur une grille régulière                         | XCOM, Tabletop Simulator    |
| **Open World**            | Monde libre sans progression linéaire forcée                  | GTA V, Skyrim               |
| **Escape Room**           | Puzzle de logique dans un espace confiné                       | The Room, Escape Goat       |
| **Resource Management**   | Gestion des ressources limitées                                | Factorio, Overcooked        |

### Distinction Critique (Windleharth et al.)

**Mechanics ≠ Feedback/Polish**

- Mécanique = affect les règles du jeu
- Polish = améliore l'expérience mais ne change pas la gameplay

*Exemple :* "Smooth Animation" est du polish, pas une mécanique.

### Note Méthodologique

Les tags Steam pour les mécaniques sont **très spécifiques** et couvrent un large spectre. Certains "sous-genres" comme "Deckbuilding" ou "Roguelike" peuvent aussi être des mécaniques dominantes (d'où l'importance de notre restructuration taxonomique).

---

## 4. THEME (Thème)

### Définition Formelle

**Theme = Univers narratif, univers visuel et contexte conceptuel dans lequel le jeu se déroule.**

Un thème encapsule :

- **L'univers conceptuel** : Fantasy, Sci-Fi, Horror, etc.
- **Les éléments visuels et narratifs** : Medieval castles, cybernetic augmentation, etc.
- **Le contenu référentiel** : références, licences, IP existantes

### Distinction avec le Setting


| Concept              | Scope                               | Exemple                                    |
| -------------------- | ----------------------------------- | ------------------------------------------ |
| **Theme (Thème)**   | Large, universel                    | "Fantasy", "Cyberpunk"                     |
| **Setting (Décor)** | Spécifique, géographique/temporel | "Medieval Europe", "1980s America", "Mars" |

### Exemples de Thèmes dans la Taxonomie


| Thème                   | Caractéristiques Principales                                    | Jeux Représentatifs                             |
| ------------------------ | ---------------------------------------------------------------- | ------------------------------------------------ |
| **Fantasy**              | Magie, créatures mythologiques, quêtes épiques                | The Witcher 3, Dragon Age, Skyrim                |
| **Sci-Fi**               | Technologies avancées, univers futuriste, exploration spatiale  | Mass Effect, The Expanse, Half-Life              |
| **Cyberpunk**            | Dystopie technologique, corporations, réalité virtuelle        | Cyberpunk 2077, Neuromancer                      |
| **Horror/Psychological** | Atmosphère terrifiante, créatures démoniaques, santé mentale | Resident Evil, Silent Hill, Amnesia              |
| **Medieval**             | Chevaliers, châteaux, épées, royauté                         | Crusader Kings, Mount & Blade                    |
| **Superhero**            | Super-pouvoirs, capes, combat surhumain                          | Marvel's Spider-Man, Injustice                   |
| **Post-Apocalyptic**     | Monde détruit, survie, ressources rares                         | Fallout, The Last of Us                          |
| **Lovecraftian**         | Horreur cosmique, folie, anciennes puissances                    | Eldritch Horror, The Case of Charles Dexter Ward |
| **Steampunk**            | Technologie à vapeur, aéronautique rétro-futuriste            | Dishonored, Bioshock                             |
| **Pirates**              | Navigation, trésor, vie sur les mers                            | Sea of Thieves, Assassin's Creed Black Flag      |

### Rôle dans l'Analyse

Le thème est **crucial pour l'identité d'une IP** mais **moins déterminant pour la gameplay**. Deux jeux peuvent partager le même thème mais avoir des genres complètement différents.

*Exemple :*

- "The Witcher 3" = RPG + Fantasy + Dark Fantasy
- "Darkest Dungeon" = Roguelike + Dark Fantasy + Dungeon Crawler

Même thème (Dark Fantasy), genres différents.

---

## 5. SETTING (Décor/Contexte Spatio-Temporel)

### Définition Formelle

**Setting = Localisation spécifique, contexte historique ou fictif, et époque dans laquelle se déroule le jeu.**

Le setting est plus **granulaire et spécifique** que le thème. Il répond à des questions :

- **Où ?** (Géographie/Localité)
- **Quand ?** (Époque historique ou fictive)
- **Quel univers parallèle ou timeline ?**

### Relation avec Theme et Perspective

```
Theme (large) → Setting (spécifique) → Narrative/Context (unique)
Fantasy → Medieval Europe → Kingdom of Rivia (The Witcher)
Sci-Fi → Space → The Galaxy (Star Wars)
```

### Exemples de Settings dans la Taxonomie


| Setting               | Caractéristiques                                    | Jeux Représentatifs                       |
| --------------------- | ---------------------------------------------------- | ------------------------------------------ |
| **Space**             | Environnement spatial, stations, planètes           | Mass Effect, No Man's Sky, Elite Dangerous |
| **Modern**            | Époque contemporaine (2000s-2020s)                  | GTA V, Watch Dogs, Payday 2                |
| **Medieval**          | Moyen-Âge, châteaux, épées (voir aussi Theme)    | Crusader Kings, Mount & Blade              |
| **1980s/1990s**       | Époque rétro-futuriste, synthwave, arcade          | Hotline Miami, Kung Fury                   |
| **Rome/Ancient**      | Antiquité romaine, gladiateurs, empires antiques    | Total War Rome, Assassin's Creed Origins   |
| **Mars/Alien Worlds** | Planètes extraterrestres, colonies spatiales        | The Expanse, Mars Odyssey                  |
| **Underwater**        | Mondes sous-marins, abysses, colonies aquatiques     | Subnautica, Abzu                           |
| **Cold War**          | Tension géopolitique, espionnage, années 1950-1990 | Fallout, We Happy Few                      |

### Note Méthodologique

Le setting est **peu représenté dans la folksonomie Steam** car les joueurs préfèrent taguer le thème large. Dans notre taxonomie, nous avons maintenu cette dimension car elle est **pertinente pour l'analyse expert** même si elle est sous-représentée dans les données.

---

## 6. MOOD (Tonalité/Ambiance)

### Définition Formelle

**Mood = Tonalité émotionnelle, atmosphère et ressenti global véhiculé par le jeu à travers sa direction artistique et son design narratif.**

Le mood est une **propriété de l'expérience émotionnelle** du joueur, influencée par :

- **L'atmosphère visuelle et sonore**
- **La tonalité narrative** (sérieuse, humoristique, absurde)
- **Le pacing et la difficulté**
- **Les intentions créatives**

### Distinction Critique


| Concept   | Définition                    | Exemple                         |
| --------- | ------------------------------ | ------------------------------- |
| **Theme** | Univers/contenu conceptuel     | "Fantasy"                       |
| **Mood**  | Ressenti émotionnel du joueur | "Dark", "Relaxing", "Whimsical" |

Un jeu "Fantasy" peut être "Dark" ou "Cozy" selon son mood.

### Exemples de Moods dans la Taxonomie


| Mood                 | Caractéristiques Émotionnelles             | Jeux Représentatifs                              |
| -------------------- | -------------------------------------------- | ------------------------------------------------- |
| **Atmospheric**      | Immersion sensorielle profonde, mystère     | Outer Wilds, Hyper Light Drifter                  |
| **Dark**             | Tonalité sombre, menaçante, oppressante    | Dark Souls, Bloodborne, Silent Hill               |
| **Relaxing**         | Calme, méditation, absence de stress        | Stardew Valley, Spiritfarer                       |
| **Funny/Dark Humor** | Tonalité humoristique, absurde, satirique   | Portal, Undertale, Bendy and the Ink Machine      |
| **Cozy**             | Chaleureux, confortable, accueillant         | Animal Crossing, Spiritfarer, Unpacking           |
| **Wholesome**        | Positif, inspirant, constructif              | A Short Hike, Journey                             |
| **Psychological**    | Dérangeant, perturbateur, existentiel       | Doki Doki Literature Club, Spec Ops: The Line     |
| **Cinematic**        | Filmique, narratif proche du cinéma         | Uncharted, The Last of Us, God of War             |
| **Surreal**          | Étrange, dreamlike, logique non-euclidienne | Sayonara Wild Hearts, Braid                       |
| **Psychedelic**      | Visuels hallucinogènes, synesthésie        | Rez, Lumino City                                  |
| **Beautiful**        | Esthétiquement remarquable, poétique       | Journey, Gris, Abzu                               |
| **Difficult**        | Punissant, exigeant, frustrant               | XCOM (sur difficultés élevées), Dwarf Fortress |
| **Unforgiving**      | Sans compromis, permadeath, pas de salut     | Hades (sur Heat), FTL                             |
| **Experimental**     | Non-conventionnel, innovant, déconcertant   | Manifold Garden, The Stanley Parable              |

### Rôle pour l'Analyse

Le mood est **fondamental pour comprendre l'expérience joueur** au-delà des méchaniques pures. Deux jeux avec les mêmes mécaniques peuvent avoir des moods radicalement différents.

---

## 7. AESTHETICS (Esthétique Visuelle et Sonore)

### Définition Formelle

**Aesthetics = Style de présentation visuelle et sonore du jeu, indépendamment du contenu ou des mécaniques.**

L'esthétique couvre :

- **Technique de rendu** : 2D, 3D, voxel, FMV
- **Style artistique** : Pixel art, cartoon, hand-drawn, minimalist
- **Signature sonore** : Musique 8-bit, rock, electronic, instrumental

### Distinction Critique


| Concept        | Affects                            | Exemple          |
| -------------- | ---------------------------------- | ---------------- |
| **Aesthetics** | L'apparence du jeu uniquement      | "Pixel Graphics" |
| **Theme**      | Le contenu conceptuel du jeu       | "Fantasy"        |
| **Mood**       | L'impression émotionnelle globale | "Dark"           |

Un jeu peut être "Pixel Graphics" + "Fantasy" + "Dark" (Darkest Dungeon).

### Exemples d'Esthétiques dans la Taxonomie


| Esthétique                         | Caractéristiques Techniques                       | Jeux Représentatifs                              |
| ----------------------------------- | -------------------------------------------------- | ------------------------------------------------- |
| **Pixel Graphics / Retro**          | Sprites basse résolution, style années 80-90     | Stardew Valley, Celeste, Hyper Light Drifter      |
| **3D**                              | Modèles tridimensionnels, polygones               | Uncharted, GTA V, The Witcher 3                   |
| **2D**                              | Sprites en deux dimensions, perspective plate      | Hollow Knight, Ori and the Blind Forest           |
| **Cartoon/Cartoony**                | Style exagéré, coloré, non-réaliste            | Grim Fandango, Adventure Time                     |
| **Hand-drawn**                      | Art manuel digitalisé, style peint                | Gris, Oxenfree, Cuphead                           |
| **Stylized**                        | Approche artistique reconnaissable, intentionnelle | Borderlands (cel-shading), Fortnite (comic style) |
| **Minimalist**                      | Réduction à l'essentiel, géométrique           | Monument Valley, Two Dots                         |
| **Abstract**                        | Formes non-figuratives, couleurs pures             | ABZU, Conductor                                   |
| **FMV (Full Motion Video)**         | Vidéo enregistrée réelle ou cinématique        | Night Trap, Deadly Premonition                    |
| **Voxel**                           | Cubes/voxels comme unités de base                 | Minecraft, Voxel Tycoon                           |
| **2.5D**                            | Pseudo-3D, profondeur illusoire                    | Paper Mario, Donkey Country                       |
| **Old School**                      | Références volontaires aux jeux anciens          | Shovel Knight, Mega Man 11                        |
| **Retro Aesthetics**                | Style nostalgique des périodes antérieures       | Hotline Miami (80s), Streets of Rage 4            |
| **8-bit Music / Electronic / Rock** | Styles musicaux spécifiques                       | Shovel Knight, Hotline Miami, Metal Gear          |

### Note Méthodologique

L'esthétique est **relativement indépendante des mécaniques**. La même technique de rendu peut servir des genres totalement différents :

- Pixel Art = Platformer (Celeste) ou RPG (Stardew Valley) ou Roguelike (Hades)

---

## 8. PERSPECTIVE (Point de Vue)

### Définition Formelle

**Perspective = Point de vue spatial de la caméra/interface qui définit comment le joueur voit l'univers du jeu.**

La perspective détermine :

- **La relation spatiale** du joueur au monde
- **Les capacités visuelles** du joueur (quoi voir, à quelle distance)
- **Le type de contrôle** favorisé (rotation 3D, mouvements 2D, etc.)

### Impact sur le Gameplay

La perspective est **intrinsèquement liée aux mécaniques**. Certain genres demandent des perspectives spécifiques :

- FPS → First-Person
- Roguelike classique → Top-Down
- Platformer → Side-Scroller

### Exemples de Perspectives dans la Taxonomie


| Perspective                   | Caractéristiques                                 | Jeux Représentatifs                               |
| ----------------------------- | ------------------------------------------------- | -------------------------------------------------- |
| **First-Person (FP)**         | Yeux du joueur dans le monde, vision 3D immersive | Doom, Half-Life, Portal                            |
| **Third-Person (TP)**         | Caméra derrière le joueur, vision de l'avatar   | Uncharted, Dark Souls, Gears of War                |
| **Isometric (Iso)**           | Vue en perspective isométrique (45°), pseudo-3D | Diablo, Pillars of Eternity, Baldur's Gate         |
| **Top-Down**                  | Vue verticale du haut, 2D orthogonale             | Zelda (original), Nuclear Throne, Binding of Isaac |
| **Side-Scroller / Side-View** | Vue latérale 2D, profondeur axe Z limité        | Super Mario, Hollow Knight, Celeste                |
| **Over-the-Shoulder**         | Caméra proche du personnage (proche TP)          | Resident Evil 4, TLOU, Gears of War                |

### Note sur la Classification

Certaines perspectives peuvent être hybrides (ex: TP dynamique qui peut switcher à FP). Notre taxonomie priorise la perspective **primaire/dominante** du jeu.

---

## 9. PLAYERS (Configuration Multijoueur/Communauté)

### Définition Formelle

**Players = Configuration de jeu (nombre de joueurs) et contextes de jeu (single, multi, compétitif, coopératif).**

Cette dimension décrit :

- **Le nombre de joueurs** : seul, 2, 4, équipes, massif
- **L'interaction sociale** : compétitive, coopérative, asynchrone
- **Le localisation** : local (sur écran), en ligne, mixte

### Distinction Critique


| Configuration          | Définition                                             | Exemple                                           |
| ---------------------- | ------------------------------------------------------- | ------------------------------------------------- |
| **Singleplayer**       | Un seul joueur, pas d'interaction directe avec d'autres | Skyrim, Tetris, Hades                             |
| **Local Multiplayer**  | Plusieurs joueurs, même appareil/écran                | Smash Bros (local), Overcooked                    |
| **Online Multiplayer** | Plusieurs joueurs, connectés via internet              | Valorant, Fortnite, WoW                           |
| **Co-op**              | Joueurs collaboratif vers un objectif commun            | Portal 2 (co-op), Left 4 Dead 2                   |
| **PvP**                | Joueurs compétitifs, les uns contre les autres         | Dota 2, League of Legends                         |
| **PvE**                | Joueurs coopératifs contre l'environnement/IA          | Diablo 3, WoW raid                                |
| **Asynchronous**       | Joueurs n'interagissent pas en temps réel              | Dark Souls (invasions), Animal Crossing (visites) |

### Exemples de Configurations dans la Taxonomie


| Configuration                   | Caractéristiques                             | Jeux Représentatifs                        |
| ------------------------------- | --------------------------------------------- | ------------------------------------------- |
| **Singleplayer**                | Complet seul, narration/défi personnelle     | Witcher 3, Tetris, Hades                    |
| **Multiplayer**                 | Multiple joueurs, compétitif ou coopératif  | Valorant, Smash, Mario Kart                 |
| **Online Co-Op**                | Collaboration en ligne, objectifs communs     | Deep Rock Galactic, Grounded                |
| **PvP (Player vs Player)**      | Compétition directe joueur-joueur            | League of Legends, Valorant, Street Fighter |
| **PvE (Player vs Environment)** | Collaboration contre menaces IA/procédurales | Diablo, Left 4 Dead, Raid WoW               |
| **Massively Multiplayer (MMO)** | Centaines/milliers de joueurs simultanés     | World of Warcraft, Final Fantasy XIV        |
| **Local Co-Op**                 | Plusieurs joueurs sur même appareil          | Overcooked, Smash Bros (local), A Way Out   |
| **Local Multiplayer**           | Compétition locale sur même écran          | Mario Kart, Bomberman                       |
| **Split Screen**                | Écrans partagés, perspectives séparées    | Halo, Borderlands (co-op)                   |
| **Team-Based**                  | Équipes organisées, compétition d'équipe  | Valorant, Overwatch, Dota 2                 |
| **Competitive**                 | Focus sur la compétition et le classement    | League of Legends, Rocket League, Chess     |
| **Asynchronous Multiplayer**    | Interactions décalées dans le temps         | Dark Souls (invasions), Animal Crossing     |

### Rôle pour l'Analyse

La configuration multijoueur est **décisive pour les jeux sociaux** mais **moins pertinente pour les single-player story-driven games**. Elle influence fortement la conception (balance, monetization, etc.).

---

## Synthèse Récapitulative

### Tableau de Relation entre les Dimensions

```
GAMEPLAY (expérience ludique globale)
│
├── GENRE (mécaniques fondamentales)
│   └─ définit la boucle de gameplay primaire
│
├── MECHANICS (systèmes interactifs)
│   └─ règles élémentaires composant le genre
│
├── THEME (univers narratif/conceptuel)
│   └─ contexte général du jeu
│
├── SETTING (localisation spatio-temporelle)
│   └─ spécificité du thème
│
├── MOOD (tonalité émotionnelle)
│   └─ ressenti global du joueur
│
├── AESTHETICS (présentation visuelle/sonore)
│   └─ style indépendant des mécaniques
│
├── PERSPECTIVE (point de vue)
│   └─ détermine l'interface joueur-monde
│
└── PLAYERS (configuration sociale)
    └─ contexte de jeu et interaction
```

### Exemple Intégré : The Witcher 3


| Dimension       | Classification                                                                 |
| --------------- | ------------------------------------------------------------------------------ |
| **Gameplay**    | Jeu d'action narratif riche                                                    |
| **Genre**       | Action RPG                                                                     |
| **Mechanics**   | Character progression, dialogue choices, combat real-time, inventory, questing |
| **Theme**       | Dark Fantasy                                                                   |
| **Setting**     | Medieval Fantasy World (Northern Kingdoms)                                     |
| **Mood**        | Dark, Cinematic, Story Rich                                                    |
| **Aesthetics**  | 3D, Stylized Realistic                                                         |
| **Perspective** | Third-Person (Over-the-shoulder)                                               |
| **Players**     | Singleplayer                                                                   |

---

## Bibliographie de Référence

1. **Lee, Y., Raghu, T. S., & Vinze, A.** (2013). *Video Game Metadata Schema: Standards for Content Description and Discovery*. Journal of Management Information Systems, 30(2), 121-156.
2. **Windleharth, T., & Bauer, J. M.** (2019). *Full Steam Ahead: A Conceptual Analysis of User-Supplied Tags on Steam*. Proceedings of DiGRA 2019.
3. **Elverdam, C., & Aarseth, E.** (2007). *Game Classification as Game Design Construction Theory*. DiGRA 2007 Proceedings.
4. **Adrian, A., Kumar, A., & Mishra, R.** (2020). *ConTag: A Semantic Tag Recommendation System for Video Games using Collaborative Filtering*. ACM Transactions on Intelligent Systems and Technology, 11(3), 1-25.
5. **Elias, G., Garfield, D., & Gutschera, K.** (2012). *Characteristics of Games*. MIT Press.
6. **Swink, S.** (2009). *Game Feel: A Game Designer's Guide to Virtual Sensation*. CRC Press.

---

## Notes Méthodologiques pour ce Projet

### Application à la Folksonomie Steam

1. **Transformation des Tags** : Les 1,4M+ tags Steam bruts ont été reorganisés selon ces 8 dimensions pour créer une structure multi-axes cohérente.
2. **Couverture Inégale** : Certaines dimensions (Genre, Mechanics, Theme) sont bien représentées car les joueurs les taggent activement. D'autres (Setting, Mood) sont sous-représentées.
3. **Tags Élagués** : Les tags marketing ("Indie", "Early Access", "Violent") et non-informatifs ont été exclus pour se concentrer sur les données de gameplay.
4. **Ambiguïtés Résolues** : Certains tags pouvaient appartenir à plusieurs dimensions. La taxonomie a tranché en fonction du contexte et de la fréquence d'usage.

### Limite de cette Approche

- **Absence de tags ≠ absence de propriété** : Un jeu sans tag "Fantasy" peut quand même être un jeu fantasy peu tagué.
- **Perspective binaire** : Notre approche traite les dimensions de façon indépendante, mais en réalité elles sont hautement interdépendantes.
- **Évolution temporelle** : Les conventions de tagging changent, ce qui affecte la couverture.

---

*Document maintenu et versionné par le projet de recherche "Game Mechanics Classification Steam"*
*Dernière mise à jour : 15 mars 2024*
