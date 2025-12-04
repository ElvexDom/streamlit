import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------
# Titre et description
# ------------------------------
st.title("Création d'un outil d'analyse de données interactif")
st.write("""
Chargez un fichier CSV (par exemple le dataset 'video game sales') pour explorer les données,
visualiser des relations entre variables et filtrer les données selon différents critères.
""")

# ------------------------------
# Upload du fichier CSV
# ------------------------------
uploaded_file = st.file_uploader(
    "Choisissez un fichier CSV",
    type=["csv"],
    help="Téléversez le fichier CSV contenant les données."
)

use_demo = st.checkbox("Utiliser un jeu de données de démonstration si aucun fichier n'est fourni", value=False)

@st.cache_data
def load_csv(file) -> pd.DataFrame:
    return pd.read_csv(file)

# Gestion des données
if uploaded_file is None and use_demo:
    st.info("Aucun fichier chargé — utilisation d'un petit jeu de démonstration.")
    demo = pd.read_csv("data/vgsales.csv")
    data = demo
elif uploaded_file is not None:
    try:
        data = load_csv(uploaded_file)
    except Exception as e:
        st.error(f"Erreur lors de la lecture du CSV: {e}")
        st.stop()
else:
    st.warning("Aucune donnée chargée. Téléversez un CSV ou cochez l'option de démonstration.")
    st.stop()

# ------------------------------
# Exploration des données
# ------------------------------
st.header("Exploration des données")

st.subheader("Aperçu des premières lignes")
st.dataframe(data.head())

st.subheader("Statistiques descriptives")
st.write(data.describe(include='number'))

st.subheader("Types de données et valeurs manquantes")
info_df = pd.DataFrame({
    "Type": data.dtypes,
    "Valeurs manquantes": data.isnull().sum(),
    "Pourcentage manquant": data.isnull().mean() * 100
})

st.dataframe(info_df)

# ------------------------------
# Sélection de colonnes à afficher
# ------------------------------
st.subheader("Sélection de colonnes")
all_columns = list(data.columns)
cols_to_show = st.multiselect("Choisir les colonnes à afficher", options=all_columns, default=all_columns[:5])
if cols_to_show:
    st.dataframe(data[cols_to_show].head(200))

# ------------------------------
# Filtrage des données
# ------------------------------
st.header("Filtrage des données")

# Choisir une colonne pour filtrer
filter_col = st.selectbox("Choisir une colonne pour filtrer", options=[None] + all_columns)

# On commence avec toutes les lignes
filtered_data = data.copy()

if filter_col:
    # Récupérer toutes les valeurs uniques de la colonne
    unique_vals = data[filter_col].dropna().unique()
    
    # L'utilisateur choisit les valeurs à afficher
    chosen_vals = st.multiselect(
        f"Choisir les valeurs de {filter_col}",
        options=sorted(unique_vals),
        default=list(unique_vals[:5])
    )
    
    # Filtrer les données selon le choix
    if chosen_vals:
        filtered_data = data[data[filter_col].isin(chosen_vals)]

st.subheader("Aperçu des données filtrées")
st.dataframe(filtered_data.head(200))

@st.cache_data
def convert_df_to_csv(df: pd.DataFrame) -> bytes:
    return df.to_csv(index=False).encode('utf-8')

csv_bytes = convert_df_to_csv(filtered_data)
st.download_button("Télécharger les données filtrées (CSV)", data=csv_bytes, file_name="filtered_data.csv", mime="text/csv")

# ------------------------------
# Visualisation interactive
# ------------------------------
st.header("Visualisation")
chart_type = st.selectbox("Type de graphique", options=["Nuage de points (scatter)", "Histogramme"]) 

numeric_cols = list(data.select_dtypes(include=[np.number]).columns)
cat_cols = list(data.select_dtypes(include=['object', 'category']).columns)

if chart_type == "Nuage de points (scatter)":
    st.subheader("Nuage de points")
    
    if len(numeric_cols) < 2:
        st.warning("Pas assez de colonnes numériques pour un nuage de points.")
    else:
        # Choix des colonnes X et Y
        x_col = st.selectbox("Colonne X", options=numeric_cols, index=0)
        y_col = st.selectbox("Colonne Y", options=numeric_cols, index=1)

        # Création du graphique
        fig, ax = plt.subplots()
        sns.scatterplot(data=filtered_data, x=x_col, y=y_col, ax=ax)  # plus de hue
        ax.set_title(f"Scatter: {y_col} vs {x_col}")
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        ax.grid(True)

        # Affichage dans Streamlit
        st.pyplot(fig)

elif chart_type == "Histogramme":
    st.subheader("Histogramme")
    if not numeric_cols:
        st.warning("Aucune colonne numérique disponible pour l'histogramme.")
    else:
        hist_col = st.selectbox("Choisir la colonne pour l'histogramme", options=numeric_cols)
        bins = st.slider("Nombre de bacs (bins)", min_value=5, max_value=200, value=20)
        fig, ax = plt.subplots()
        ax.hist(filtered_data[hist_col].dropna(), bins=bins)
        ax.set_title(f"Histogramme de {hist_col}")
        ax.set_xlabel(hist_col)
        ax.set_ylabel("Fréquence")
        st.pyplot(fig)

# ------------------------------
# Résumé final
# ------------------------------
st.header("Résumé")
st.write(f"Nombre total de lignes : {len(data)}")
st.write(f"Nombre de lignes après filtrage : {len(filtered_data)}")

if st.checkbox("Afficher une table pivot d'exemple (moyenne des ventes par platform)"):
    if 'Global_Sales' in data.columns and 'Platform' in data.columns:
        pivot = filtered_data.groupby('Platform', dropna=False)['Global_Sales'].mean().reset_index()
        pivot.columns = ['Platform', 'Moyenne Global_Sales']
        st.table(pivot)
    else:
        st.info("Les colonnes 'Platform' et 'Global_Sales' ne sont pas présentes dans le dataset.")
