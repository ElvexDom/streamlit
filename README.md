# Application de Visualisation de Données CSV

## Description

Cette application **Streamlit** permet de charger un fichier CSV et de visualiser ses données de manière interactive et statique.
Elle offre plusieurs fonctionnalités pour explorer et analyser vos données, comme des tableaux, des graphiques et des composants interactifs.

---

## Fonctionnalités principales

* **Chargement et affichage de CSV** : affiche les données dans un tableau interactif et statique.
* **Interactions utilisateur** : boutons, cases à cocher, champs texte, menus déroulants, curseurs.
* **Organisation du contenu** : utilisation de colonnes, onglets et conteneurs extensibles (expanders).
* **Visualisation de données** :

  * Graphiques statiques avec **Matplotlib** (histogrammes).
  * Graphiques interactifs avec **Plotly** (scatter plots, histogrammes, boxplots).
  * Graphiques **Seaborn** (pairplots, heatmaps, boxplots).
* **Exemple de dataset intégré** : Dataset Iris pour démonstration des visualisations Seaborn.

---

## Installation

### Cloner le dépôt

```bash
git clone <URL_DU_DEPOT>
cd nom_du_projet
```

### Créer un environnement virtuel (optionnel mais recommandé)

```bash
python -m venv venv
# Sur macOS/Linux
source venv/bin/activate
# Sur Windows
venv\Scripts\activate
```

### Installer les dépendances

```bash
pip install -r requirements.txt
```

#### Exemple de `requirements.txt`

```
streamlit
pandas
matplotlib
seaborn
plotly
```

---

## Utilisation

1. Placer votre fichier CSV dans le dossier `data/`
   Exemple : `data/employes.csv`

2. Lancer l’application Streamlit :

```bash
streamlit run app.py
```

3. L’application s’ouvrira dans votre navigateur.

4. Explorez les différentes sections :

   * Tableaux interactifs
   * Visualisations
   * Composants interactifs

---

## Structure du projet

```
nom_du_projet/
│
├─ data/                  # Contient les fichiers CSV
│   └─ employes.csv
│
├─ app.py                 # Script principal Streamlit
├─ requirements.txt       # Dépendances Python
└─ README.md              # Documentation du projet
```

---

## Licence

MIT
