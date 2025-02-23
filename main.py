import streamlit as st

from Fonction import display_notebook_charts

if __name__ == "__main__":
    st.title("Projet Statistique par Firas et Ayoub")
    notebook_file = "stat-inf-1.ipynb"
    display_notebook_charts(notebook_file)
