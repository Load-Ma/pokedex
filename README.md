# pokedex

Clonez le projet dans votre IDE de votre choix:

Environnement Virtuel

Si votre IDE ne met pas en place un environnement virtuel (normalement pokedex est un venv),
vous devez en mettre un. Pour ce faire, ouvrez un terminal a la racine de votre projet
et tapez les commandes suivantes :

    -> pip install virtualenv

Pour créer un venv :

    -> py -m venv [NomduVenv]

Pour activer le venv, aller dans le dossier script dans le venv et faites la commande suivante:

    -> ./activate

Il devrait y avoir des erreurs c'est normal il vous manque les packages

Installer les packages

    -> pip install request

Lancer le projet

Pour lancer le projet, aller a la racine du projet et tapez la commande suivante :

    -> py ./manage.py runserver

La commande devrait vous retourner des informations et notamment une url.
Vous devrez avoir une url qui ressemble à "http://127.0.0.1:8000"

Copiez la dans un navigateur et ajouter y un /pokemon/all pour accéder a la liste des pokemons !

Si votre navigateur met du temps à charger la page c'est normal veuillez attendre une minute et tout devrait être bon vous pouvez dès a présent naviger sur le pokedex lorsque vous cliquez sur un pokemon spécific vous aurez accès au vrai pokedex avec les informations du pokémon.

![image](https://user-images.githubusercontent.com/75785249/203160881-6d7e8cf7-5681-4dd9-bb85-2ed52d9fb16a.png)

Au dessus de votre pokedex vous pouvez retrouver une barre de rechercher pour retrouver le pokemon que vous chercher en tapant son nom en anglais !

![image](https://user-images.githubusercontent.com/75785249/203129867-b06e24d6-661a-45ae-9415-189835f91565.png)

Ce qui se trouve dans l'encadré bleu vous permet de passer le pokemon en __shiny__ ou de le mettre en mode normal. <br>
Vous pouvez également changer le sexe du pokemon en cliquant sur les icônes mâle ou femelle.

![image](https://user-images.githubusercontent.com/75785249/203130492-92247e4e-1ef3-4fa7-ade5-c0930c34fb0b.png)

Les __fleches__ qui se trouvent dans l'encadré jaune vous permettent de nombreuses choses ! <br>
Les __fleches__ de gauche et droite permettent de tourner le pokemon pour pouvoir le voir de dos. <br>
Les __fleches__ du haut et du bas vous permettent de vous déplacer de pokemon en pokemon, cela est très utile pour les évolutions des pokemons qui sont classés par ID (imaginons c'est la première forme du pokemon en allant sur la fleche du haut vous pourrez voir ses évolutions (avec leurs caractéristiques) et la fleches du bas permet de revenir à la plus petite évolution.)

![image](https://user-images.githubusercontent.com/75785249/203132276-d3665d04-b75b-4d94-8c45-56de510b2bbe.png)

Pour finir l'encadré blanc représente votre équipe de pokemon par des gifs, vous pouvez possedez jusqu'à 6 pokémons dans votre équipe. <br>
L'encadré rose défini le type de votre pokemon dans le cas ici present il est uniquement de type "eau" il y a deux encadrés car il peut y avoir des pokémons avec deux types. <br>
Vous retrouvez également dans les encadrés noirs au dessus toutes les caractéristiques du pokemon comme sa taille, son poids ou encore ses abilités.
L'encardé vert represente les boutons vout permettant d'ajouter ou retirer un pokemon de votre équipe (il se peut que lorsque vous ajoutez ou retirez votre pokemon il se passe rien il suffira de raffraichir la page pour le voir ajouté ou supprimé)

LECONTE Cameron <br>
CAILLE Romain <br>
GOUEREC Enzo

