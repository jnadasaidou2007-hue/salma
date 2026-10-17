# Estimation du prix d'une maison

Mini-projet pédagogique (BTS IA) : analyse statistique d'un jeu de données
immobilier et prédiction du prix d'une maison avec le Machine Learning,
via une application web Streamlit.

**Démo en ligne :** https://TON-APP.streamlit.app

## Ce que fait le projet

- Analyse de 8 maisons fictives (prix en milliers de dirhams) :
  moyenne, médiane, minimum, maximum, étendue, prix au m²
- Corrélation et nuage de points entre superficie et prix
- Modèle de régression linéaire (scikit-learn), évalué avec MAE et R²
- Estimation du prix selon la superficie, le nombre de chambres et l'ancienneté

## Technologies

Python, pandas, matplotlib, scikit-learn, Streamlit

## Structure

- `analyse.py` : analyse statistique et graphique
- `app.py` : application Streamlit avec le modèle
- `requirements.txt` : bibliothèques à installer

## Lancer le projet en local

```bash
pip install -r requirements.txt
python analyse.py
streamlit run app.py
```

L'application s'ouvre sur http://localhost:8501

## Limites

Le jeu de données ne contient que 8 exemples fictifs. Le découpage
entraînement/test est donc instable et les métriques ne prouvent pas
la fiabilité du modèle. Les estimations sont uniquement pédagogiques
et ne doivent pas servir pour une transaction immobilière.

## Auteure

Nada Saidou
