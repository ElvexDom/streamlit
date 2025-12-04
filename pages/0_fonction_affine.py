import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
# Titre principal
# ------------------------------
st.title("Visualisation interactive d'une fonction affine")
st.write("Cette application permet de visualiser la fonction : y = a x + b")

# ------------------------------
# Sliders pour les paramètres
# ------------------------------
a = st.slider(
    "Valeur de a (pente)",
    min_value=-10.0,
    max_value=10.0,
    value=1.0,
    step=1.0
)

b = st.slider(
    "Valeur de b (ordonnée à l'origine)",
    min_value=-10.0,
    max_value=10.0,
    value=0.0,
    step=1.0
)

# ------------------------------
# Bonus : Intervalle de x
# ------------------------------
xmin = st.slider(
    "Valeur minimale de x",
    min_value=-50.0,
    max_value=0.0,
    value=-10.0,
    step=1.0
)

xmax = st.slider(
    "Valeur maximale de x",
    min_value=0.0,
    max_value=50.0,
    value=10.0,
    step=1.0
)

# ------------------------------
# Bonus : Couleur de la courbe
# ------------------------------
couleur = st.color_picker("Choisir la couleur de la courbe", "#1f77b4")

# ------------------------------
# Génération des valeurs
# ------------------------------
x = np.linspace(xmin, xmax, 400)
y = a * x + b

# ------------------------------
# Affichage de l'équation
# ------------------------------
st.markdown(f"### Équation actuelle :  \n**y = {a}x + {b}**")

# ------------------------------
# Création du graphique
# ------------------------------
fig, ax = plt.subplots()
ax.plot(x, y, color=couleur)

# Personnalisation du graphique
ax.set_title("Courbe de la fonction affine")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(True)

# ------------------------------
# Affichage dans Streamlit
# ------------------------------
st.pyplot(fig)
