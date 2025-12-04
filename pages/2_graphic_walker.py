import streamlit as st
import pandas as pd
from panel_gwalker import GraphicWalker
import logging
logging.getLogger('bokeh').setLevel(logging.WARNING)

st.title("Analyse interactive avec GraphicWalker")

# Upload CSV
uploaded_file = st.file_uploader("Choisissez un CSV", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Aperçu des données")
    st.dataframe(df.head())

    # Intégration de GraphicWalker
    gwalker = GraphicWalker(df)
    gwalker.show()
