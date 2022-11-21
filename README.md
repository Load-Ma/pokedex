# pokedex

Clonez le projet dans votre IDE de votre choix:

Environnement Virtuel

Si votre IDE ne met pas en place un environnement virtuel,
vous devez en mettre un. Pour ce faire, ouvrez un terminal a la racine de votre projet
et tapez les commandes suivantes :

    -> pip install virtualenv

Pour créer un venv :

    -> py -m venv [NomduVenv]

Pour activer le venv, aller dans le dossier script dans le venv et faites la commande suivante:

    -> ./activate

Pour désactiver le venv :

    -> ./deactivate

Il devrait y avoir des erreurs c'est normal il vous manque les packages

Installer les packages

    -> pip install request

Lancer le projet

Pour lancer le projet, aller a la racine du projet et tapez la commande suivante :

    -> py ./manage.py runserver

La commande devrait vous retourner des informations et notamment une url.
Vous devrez avoir une url qui ressemble à "http://127.0.0.1:8000/"

Copiez la dans un navigateur et ouvrez le pokedex !

Si votre navigateur met du temps à charger la page c'est normal veuillez attendre une minute et tout devrait être bon vous pouvez dès a présent naviger sur le pokedex lorsque vous cliquez sur un pokemon spécific vous aurez accès au vrai pokedex avec les informations du pokedex.

![image](https://user-images.githubusercontent.com/75785249/203129867-b06e24d6-661a-45ae-9415-189835f91565.png)

Ce qui se trouve dans l'encadré bleu vous permet de passer le pokemon en shiny ou de le mettre en mode normal

![image](https://user-images.githubusercontent.com/75785249/203130492-92247e4e-1ef3-4fa7-ade5-c0930c34fb0b.png)

Les **fleches** qui se trouvent dans l'encadré jaune vous permettent de nombreuses choses ! <br>
Les fleches de gauche et droite permettent de tourner le pokemon pour pouvoir le voir de dos <br>
Les fleches du haut et du bas vous permettent d'acceder au évolution du pokemon (imaginons c'est la première forme du pokemon en allant sur la fleche du haut vous pourrez voir ses évolutions (avec leurs caractéristiques) et la fleches du bas permet de revenir à la plus petite évolution




