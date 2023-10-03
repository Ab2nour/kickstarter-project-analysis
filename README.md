# Analyse de survie

Analyse de survie sur des projets Kickstarter.

![Logo Kickstarter](img/kickstarter-logo.svg)

## Ce qu'est Kickstarter

_Kickstarter_ est un site Internet qui permet le _crowd-funding_, autrement dit le financement participatif. Des créateurs proposent leur idée de projet, un objectif de financement à atteindre.

Si l'objectif de financement est atteint, les créateurs obtiennent le financement et peuvent réaliser le projet. Si l'objectif n'est pas atteint, les financeurs sont remboursés et le projet est annulé.

## Modélisation du problème

La **fonction de survie** correspond ici à la probabilité que le **succès** intervienne après un temps t.

Soit **$T$ le succès**, on cherche à modéliser la fonction de survie $s(t) = P(T > t)$.

La **censure** correspond au fait que certains projets n'ont pas atteint le succès dans le temps imparti pour leur récolte de fonds.

# Jeu de données

Le jeu de données contient une liste de 18 143 projets Kickstarter menés entre le 15 décembre 2013 et le 15 juin 2014.

Pour chaque projet, nous disposons notamment de :
- sa date de départ
- sa date de fin prévue
- quand son objectif a été atteint
- si l'objectif a été atteint
- l'objectif financier
- le nombre de financeurs
- la catégorie du projet (art, cuisine, technologie, ...)
- informations sur le projet
