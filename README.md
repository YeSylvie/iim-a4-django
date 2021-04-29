# Projet Django de Sylvie YE 

Projet à rendre pour le ***14 mars 2021***

### Contexte et motivations du projet 

>L’objectif de ce projet est la création d’un site web (ou une partie de site si vous repartez du site R&D que vous avez déjà développé) permettant le stockage de CVs. Ce site permettra: (1) aux candidats de déposer des candidatures spontanées (2) aux recruteurs de pouvoir rechercher des profils qui les intéressent.

### Composition du projet

Ce projet a été developper avec le framework Django dans un cadre scolaire. 

Le projet comporte 4 pages : 
- Accueil : avec la partie R&D
- Candidature : formulaire qui permet d'upload des CV 
- Dashboard : Intégration du dashboard 
- Contact : formulaire de contact 

### Pour lancer l'application 
Avoir un environnement virtuel et le lancer -> ici **Virtualenv**
```
source myvenv/bin/activate
```

Ensuite, se mettre dans le dossier /mysite. 
```
cd mysite/
```

Puis lancer la commande suite : 
```
python3 manage.py runserver
```

Vous pouvez accéder à l'application via ici : http://127.0.0.1:8000/

### Pour la partie des tests unitaires 

Groupe : Laura TRICHET & Hugo LAMBERT & Sylvie YE

Commande pour lancer les tests unitaires : 
```
python3 manage.py test
```
