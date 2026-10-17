import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

st.set_page_config(page_title="Estimation immobilière", page_icon="🏠")
st.title("Estimation du prix d'une maison")
st.write("Projet pédagogique de régression linéaire")

# Données fictives, prix en milliers de dirhams
data = pd.DataFrame({
    "superficie": [50, 60, 70, 80, 90, 100, 110, 120],
    "chambres": [1, 2, 2, 3, 3, 3, 4, 4],
    "anciennete": [20, 15, 12, 10, 8, 5, 4, 2],
    "prix": [400, 480, 530, 650, 700, 820, 850, 960]
})

st.subheader("1. Explorer les données")
st.dataframe(data, use_container_width=True)

st.subheader("2. Statistiques descriptives")
st.write(data.describe())

X = data[["superficie", "chambres", "anciennete"]]
y = data["prix"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

col1, col2 = st.columns(2)
col1.metric("Erreur absolue moyenne", f"{mae:.1f} kDH")
col2.metric("Score R² sur le test", f"{r2:.2f}")

st.subheader("3. Estimer une maison")
superficie = st.slider("Superficie (m²)", 30, 200, 85)
chambres = st.slider("Nombre de chambres", 1, 6, 3)
anciennete = st.slider("Ancienneté (années)", 0, 50, 10)

if st.button("Estimer le prix"):
    maison = pd.DataFrame([{
        "superficie": superficie,
        "chambres": chambres,
        "anciennete": anciennete
    }])
    prix = model.predict(maison)[0]
    st.success(f"Prix estimé : {prix:.1f} milliers de DH")
    st.caption(f"Soit environ {prix * 1000:,.0f} DH.")

st.caption(
    "Données fictives et très limitées : estimation uniquement pédagogique, "
    "à ne pas utiliser pour une transaction immobilière."
)
