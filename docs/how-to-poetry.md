# Initialiser 
```bash
poetry init # suivre le tuto
```

# Installer une librairie
```bash
poetry add numpy # une seule
poetry add numpy pandas matplotlib # plusieurs
```
# Créer un environnement avec la bonne version de python
```bash
poetry env use "chemin vers le .exe de la bonne version de python"
```

# Installer les librairies à partir du pyproject.toml
```bash
poetry install
```
## Une dépendance pour le développement (n'est pas destinée à l'utilisateur)
```bash
poetry add black[jupyter] --group dev
```

# Exécuter un script avec le bon environnement python
```bash
cd "chemin du dossier du projet"
poetry run python mon_script.py
```
## Un jupyter notebook pour VSCode
CTRL + shift + P, "select interpreter", et sélectionner le bon kernel dans jupyter

# Formater un script / notebook avec black
```bash
poetry run black .
```
Tous les scripts contenus dans les étages inférieurs au chemin précisé sont formatés.