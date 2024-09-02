# Jeu du pendu

Développez un programme Python qui simule le jeu du pendu en mode console. Le jeu doit choisir un mot aléatoire dans une liste prédéfinie et permettre au joueur de deviner le mot lettre par lettre.

## Fonctionnalités requises

- Choisir un mot aléatoire dans une liste de mots.
- Afficher le mot sous forme de tirets (ex : "\_ \_ \_ \_ \_" pour "PYTHON").
- Demander au joueur de proposer une lettre.
- Vérifier si la lettre est dans le mot et mettre à jour l'affichage.
- Gérer le nombre d'essais restants et afficher l'état du pendu.
- Annoncer la victoire ou la défaite du joueur.

## Paramètres ajustables

- Nombre d'essais maximum
- Liste de mots à deviner
- Option pour afficher ou non les lettres déjà proposées

## Bonus

Permettre au joueur de choisir la difficulté (facile, moyen, difficile) qui ajuste le nombre d'essais et la longueur des mots.

## Comment exécuter le code

### Version ligne de commande

```bash
python src/main.py cli
```

### Version pygame

```bash
python src/main.py pygame
```

## Comment exécuter les tests

```bash
pytest
```
