
import streamlit as st

st.title("My first app")

nombre = st.text_input("¿Cómo te llamas?")

st.write("Hola", nombre)
