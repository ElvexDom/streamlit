import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# === TITRE PRINCIPAL ===
st.title("Application de visualisation de données CSV")

# === INTRODUCTION ===
st.header("Présentation")
st.subheader("Introduction")
st.write("Cette application permet de charger un fichier CSV et d'afficher son contenu de manière interactive ou statique.")
st.markdown("Vous pouvez visualiser les données sous forme de **tableau interactif** ou de **tableau statique** pour une lecture rapide.")

# === CHARGEMENT DES DONNÉES ===
st.header("Chargement des données")
st.write("Le fichier CSV chargé sera affiché ci-dessous.")
test_df = pd.read_csv("data/employes.csv")

# === TABLEAU INTERACTIF ===
st.header("Visualisation interactive")
st.subheader("DataFrame")
st.markdown("Le tableau ci-dessous est **interactif**, vous pouvez trier et scroller horizontalement si nécessaire.")
st.dataframe(test_df)

# === TABLEAU STATIQUE ===
st.header("Visualisation statique")
st.subheader("Table")
st.markdown("Le tableau ci-dessous est **statique**, utile pour un aperçu rapide des données.")
st.table(test_df)

# === ÉLÉMENTS INTERACTIFS SUPPLÉMENTAIRES ===
st.header("Interactions utilisateur")

# Bouton
if st.button("Cliquez ici"):
    st.write("Vous avez cliqué sur le bouton !")

# Case à cocher
if st.checkbox("Cochez-moi"):
    st.write("La case est cochée !")

# Champ de saisie de texte
texte_utilisateur = st.text_input("Entrez un texte ici :")
if texte_utilisateur:
    st.write(f"Vous avez saisi : {texte_utilisateur}")

# Sélecteur déroulant
option = st.selectbox(
    "Choisissez une option :",
    ["Option 1", "Option 2", "Option 3"]
)
st.write(f"Vous avez choisi : {option}")

# Curseur
valeur = st.slider(
    "Sélectionnez une valeur :", 
    min_value=0, 
    max_value=100, 
    value=50
)
st.write(f"Valeur sélectionnée : {valeur}")

# === COLONNES ===
st.header("Utilisation des colonnes")
col1, col2, col3 = st.columns(3)

with col1:
    st.write("Colonne 1")
    if st.button("Bouton Col 1"):
        st.write("Vous avez cliqué sur le bouton Col 1 !")

with col2:
    st.write("Colonne 2")
    if st.checkbox("Checkbox Col 2"):
        st.write("Checkbox de la colonne 2 cochée !")

with col3:
    st.write("Colonne 3")
    valeur_col3 = st.slider("Slider Col 3", 0, 100, 25)
    st.write(f"Valeur du slider Col 3 : {valeur_col3}")

# === EXPANDER ===
st.header("Utilisation d'un conteneur extensible")
with st.expander("Cliquez pour afficher plus d'options"):
    st.write("Ici, vous pouvez mettre du contenu supplémentaire comme des instructions, graphiques ou filtres.")
    texte_expander = st.text_input("Saisissez un texte dans l'expander :")
    if texte_expander:
        st.write(f"Vous avez saisi : {texte_expander}")
    option_expander = st.selectbox("Choisissez une option dans l'expander :", ["A", "B", "C"])
    st.write(f"Option choisie : {option_expander}")

# === ONGLET ===
st.header("Utilisation des onglets")
tab1, tab2 = st.tabs(["Onglet 1", "Onglet 2"])

with tab1:
    st.subheader("Contenu de l'Onglet 1")
    st.write("Vous pouvez mettre ici un tableau, un graphique ou tout autre composant.")
    st.dataframe(test_df.head())

with tab2:
    st.subheader("Contenu de l'Onglet 2")
    st.write("Contenu alternatif dans le deuxième onglet.")
    st.table(test_df.head())

# === VISUALISATION DE DONNÉES ===
st.header("Visualisation de données")

# --- Graphique Matplotlib ---
st.subheader("Graphique Matplotlib : Histogramme des revenus")
fig, ax = plt.subplots()
ax.hist(test_df['Revenu'], bins=10, color='skyblue', edgecolor='black')
ax.set_title("Histogramme des revenus")
ax.set_xlabel("Revenu")
ax.set_ylabel("Fréquence")
st.pyplot(fig)

# --- Graphiques interactifs Plotly ---
st.subheader("Graphiques interactifs Plotly")

# Scatter plot : Âge vs Revenu, couleur par Sexe (sans taille)
fig_scatter = px.scatter(
    test_df,
    x="Âge",
    y="Revenu",
    color="Sexe",
    hover_data=["Nom", "Prénom", "Ville"],
    title="Scatter plot : Âge vs Revenu"
)
st.plotly_chart(fig_scatter)

# Histogramme interactif : distribution des âges
fig_hist = px.histogram(
    test_df,
    x="Âge",
    color="Sexe",
    barmode="overlay",
    nbins=10,
    title="Distribution des âges par sexe"
)
st.plotly_chart(fig_hist)

# Boxplot interactif : Revenu par Ville
fig_box = px.box(
    test_df,
    x="Ville",
    y="Revenu",
    color="Sexe",
    title="Boxplot : Revenu par Ville et Sexe"
)
st.plotly_chart(fig_box)

# --- Graphiques Seaborn ---
st.subheader("Graphiques Seaborn pour le CSV enrichi")
sns.set_theme(style="ticks")

# Pairplot des colonnes numériques avec hue='Sexe'
fig_pair = sns.pairplot(test_df, vars=["Âge", "Revenu", "Score"], hue="Sexe", height=2.5)
st.pyplot(fig_pair.fig)

# Heatmap de corrélation
st.subheader("Carte de corrélation (Heatmap)")
corr = test_df[["Âge", "Revenu", "Score"]].corr()
fig_heat, ax = plt.subplots()
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig_heat)

# Boxplot pour comparer les revenus selon le sexe
st.subheader("Boxplot Revenu par Sexe")
fig_box_sns, ax = plt.subplots()
sns.boxplot(data=test_df, x="Sexe", y="Revenu", palette="Set2", ax=ax)
st.pyplot(fig_box_sns)

# --- Exemple avec dataset Iris pour Seaborn (optionnel) ---
st.subheader("Exemple Seaborn : Dataset Iris")
df_iris = sns.load_dataset('iris')
pair_iris = sns.pairplot(df_iris, hue='species')
st.pyplot(pair_iris.figure)
