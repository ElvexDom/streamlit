import logging
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# === CONFIGURATION DU LOGGING ===
logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)
logger = logging.getLogger(__name__)
logger.info("Application Streamlit démarrée")

# === TITRE PRINCIPAL ===
st.title("Application de visualisation de données CSV")
logger.info("Titre principal affiché")

# === INTRODUCTION ===
st.header("Présentation")
st.subheader("Introduction")
st.write("Cette application permet de charger un fichier CSV et d'afficher son contenu de manière interactive ou statique.")
st.markdown("Vous pouvez visualiser les données sous forme de **tableau interactif** ou de **tableau statique** pour une lecture rapide.")
logger.info("Introduction affichée")

# === CHARGEMENT DES DONNÉES ===
st.header("Chargement des données")
st.write("Le fichier CSV chargé sera affiché ci-dessous.")
try:
    test_df = pd.read_csv("data/employes.csv", encoding="utf-8")
    logger.info("Fichier CSV chargé avec succès : data/employes.csv")
except Exception as e:
    st.error("Erreur lors du chargement du fichier CSV.")
    logger.error(f"Erreur lors du chargement du CSV : {e}")
    st.stop()

# === TABLEAU INTERACTIF ===
st.header("Visualisation interactive")
st.subheader("DataFrame")
st.markdown("Le tableau ci-dessous est **interactif**, vous pouvez trier et scroller horizontalement si nécessaire.")
st.dataframe(test_df)
logger.info("Tableau interactif affiché")

# === TABLEAU STATIQUE ===
st.header("Visualisation statique")
st.subheader("Table")
st.markdown("Le tableau ci-dessous est **statique**, utile pour un aperçu rapide des données.")
st.table(test_df)
logger.info("Tableau statique affiché")

# === ÉLÉMENTS INTERACTIFS SUPPLÉMENTAIRES ===
st.header("Interactions utilisateur")

# Bouton
if st.button("Cliquez ici"):
    st.write("Vous avez cliqué sur le bouton !")
    logger.info("Bouton principal cliqué")

# Case à cocher
if st.checkbox("Cochez-moi"):
    st.write("La case est cochée !")
    logger.info("Checkbox cochée")

# Champ de saisie de texte
texte_utilisateur = st.text_input("Entrez un texte ici :")
if texte_utilisateur:
    st.write(f"Vous avez saisi : {texte_utilisateur}")
    logger.info(f"Texte saisi par l'utilisateur : {texte_utilisateur}")

# Sélecteur déroulant
option = st.selectbox(
    "Choisissez une option :",
    ["Option 1", "Option 2", "Option 3"]
)
st.write(f"Vous avez choisi : {option}")
logger.info(f"Option sélectionnée : {option}")

# Curseur
valeur = st.slider(
    "Sélectionnez une valeur :", 
    min_value=0, 
    max_value=100, 
    value=50
)
st.write(f"Valeur sélectionnée : {valeur}")
logger.info(f"Valeur du slider sélectionnée : {valeur}")

# === COLONNES ===
st.header("Utilisation des colonnes")
col1, col2, col3 = st.columns(3)

with col1:
    st.write("Colonne 1")
    if st.button("Bouton Col 1"):
        st.write("Vous avez cliqué sur le bouton Col 1 !")
        logger.info("Bouton Col 1 cliqué")

with col2:
    st.write("Colonne 2")
    if st.checkbox("Checkbox Col 2"):
        st.write("Checkbox de la colonne 2 cochée !")
        logger.info("Checkbox Col 2 cochée")

with col3:
    st.write("Colonne 3")
    valeur_col3 = st.slider("Slider Col 3", 0, 100, 25)
    st.write(f"Valeur du slider Col 3 : {valeur_col3}")
    logger.info(f"Slider Col 3 sélectionné : {valeur_col3}")

# === EXPANDER ===
st.header("Utilisation d'un conteneur extensible")
with st.expander("Cliquez pour afficher plus d'options"):
    st.write("Ici, vous pouvez mettre du contenu supplémentaire comme des instructions, graphiques ou filtres.")
    texte_expander = st.text_input("Saisissez un texte dans l'expander :")
    if texte_expander:
        st.write(f"Vous avez saisi : {texte_expander}")
        logger.info(f"Texte saisi dans expander : {texte_expander}")
    option_expander = st.selectbox("Choisissez une option dans l'expander :", ["A", "B", "C"])
    st.write(f"Option choisie : {option_expander}")
    logger.info(f"Option choisie dans expander : {option_expander}")

# === ONGLET ===
st.header("Utilisation des onglets")
tab1, tab2 = st.tabs(["Onglet 1", "Onglet 2"])

with tab1:
    st.subheader("Contenu de l'Onglet 1")
    st.write("Vous pouvez mettre ici un tableau, un graphique ou tout autre composant.")
    st.dataframe(test_df.head())
    logger.info("Onglet 1 affiché")

with tab2:
    st.subheader("Contenu de l'Onglet 2")
    st.write("Contenu alternatif dans le deuxième onglet.")
    st.table(test_df.head())
    logger.info("Onglet 2 affiché")

# === VISUALISATION DE DONNÉES ===
st.header("Visualisation de données")
logger.info("Section visualisation de données affichée")

# --- Graphique Matplotlib ---
st.subheader("Graphique Matplotlib : Histogramme des revenus")
fig, ax = plt.subplots()
ax.hist(test_df['Revenu'], bins=10, color='skyblue', edgecolor='black')
ax.set_title("Histogramme des revenus")
ax.set_xlabel("Revenu")
ax.set_ylabel("Fréquence")
st.pyplot(fig)
logger.info("Histogramme Matplotlib affiché")

# --- Graphiques interactifs Plotly ---
st.subheader("Graphiques interactifs Plotly")

# Scatter plot : Âge vs Revenu
fig_scatter = px.scatter(
    test_df,
    x="Âge",
    y="Revenu",
    color="Sexe",
    hover_data=["Nom", "Prénom", "Ville"],
    title="Scatter plot : Âge vs Revenu"
)
st.plotly_chart(fig_scatter)
logger.info("Scatter Plot Plotly affiché")

# Histogramme interactif
fig_hist = px.histogram(
    test_df,
    x="Âge",
    color="Sexe",
    barmode="overlay",
    nbins=10,
    title="Distribution des âges par sexe"
)
st.plotly_chart(fig_hist)
logger.info("Histogramme Plotly affiché")

# Boxplot interactif
fig_box = px.box(
    test_df,
    x="Ville",
    y="Revenu",
    color="Sexe",
    title="Boxplot : Revenu par Ville et Sexe"
)
st.plotly_chart(fig_box)
logger.info("Boxplot Plotly affiché")

# --- Graphiques Seaborn ---
st.subheader("Graphiques Seaborn pour le CSV enrichi")
sns.set_theme(style="ticks")

# Pairplot
fig_pair = sns.pairplot(test_df, vars=["Âge", "Revenu", "Score"], hue="Sexe", height=2.5)
st.pyplot(fig_pair.fig)
logger.info("Pairplot Seaborn affiché")

# Heatmap
st.subheader("Carte de corrélation (Heatmap)")
corr = test_df[["Âge", "Revenu", "Score"]].corr()
fig_heat, ax = plt.subplots()
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig_heat)
logger.info("Heatmap Seaborn affichée")

# Boxplot Seaborn
st.subheader("Boxplot Revenu par Sexe")
fig_box_sns, ax = plt.subplots()
sns.boxplot(data=test_df, x="Sexe", y="Revenu", hue="Sexe", palette="Set2", legend=False, ax=ax)
st.pyplot(fig_box_sns)
logger.info("Boxplot Seaborn affiché")

# --- Exemple avec dataset Iris ---
st.subheader("Exemple Seaborn : Dataset Iris")
df_iris = sns.load_dataset('iris')
pair_iris = sns.pairplot(df_iris, hue='species')
st.pyplot(pair_iris.figure)
logger.info("Pairplot Iris affiché")

# === FILTRES ET INTERACTIONS ===
st.header("Filtres et interactions utilisateur")

# Affichage détaillé d'un élément
st.subheader("Détails d'un élément")
if "Nom" in test_df.columns:
    nom_selectionne = st.selectbox("Sélectionnez un nom :", test_df["Nom"].unique())
    st.write(test_df[test_df["Nom"] == nom_selectionne])
    logger.info(f"Utilisateur a affiché les détails de : {nom_selectionne}")

# Filtrer les colonnes à afficher
st.subheader("Sélection des colonnes à afficher")
colonnes_disponibles = test_df.columns.tolist()
colonnes_selectionnees = st.multiselect(
    "Choisissez les colonnes à afficher :", colonnes_disponibles, default=colonnes_disponibles
)
df_colonnes = test_df[colonnes_selectionnees]
st.write(df_colonnes)
logger.info(f"Colonnes sélectionnées par l'utilisateur : {colonnes_selectionnees}")

# Filtrer les lignes selon une colonne
st.subheader("Filtrer les lignes")
col_filtre = st.selectbox("Choisissez une colonne pour filtrer :", colonnes_disponibles)

if test_df[col_filtre].dtype == "object":
    valeurs_filtre = st.multiselect("Choisissez les valeurs :", test_df[col_filtre].unique())
    df_filtre = test_df[test_df[col_filtre].isin(valeurs_filtre)]
else:
    min_val = float(test_df[col_filtre].min())
    max_val = float(test_df[col_filtre].max())
    plage = st.slider("Sélectionnez une plage :", min_val, max_val, (min_val, max_val))
    df_filtre = test_df[(test_df[col_filtre] >= plage[0]) & (test_df[col_filtre] <= plage[1])]

st.write(df_filtre)
logger.info(f"Filtrage appliqué sur la colonne {col_filtre}")

# === GESTION DES FICHIERS ===
st.header("Gestion des fichiers")

# Télécharger le DataFrame filtré
st.subheader("Télécharger les données filtrées")
csv_filtre = df_filtre.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Télécharger CSV filtré",
    data=csv_filtre,
    file_name='donnees_filtrees.csv',
    mime='text/csv'
)
logger.info("Fichier filtré prêt au téléchargement")


# Uploader un nouveau fichier CSV
st.subheader("Télécharger un fichier CSV")
fichier_upload = st.file_uploader("Choisissez un fichier CSV", type=["csv"])
if fichier_upload:
    try:
        df_upload = pd.read_csv(fichier_upload)
        st.success("Fichier chargé avec succès !")
        st.dataframe(df_upload)
        logger.info(f"Fichier CSV uploadé : {fichier_upload.name}")
    except Exception as e:
        st.error("Erreur lors du chargement du fichier CSV.")
        logger.error(f"Erreur CSV upload : {e}")
