import streamlit as st
import pandas as pd
import requests

st.title('Pokemon Explorer!(❁´◡`❁)')

pokemon_num = st.slider("Choose a pokemon!", 1, 1025)

pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_num}"
response = requests.get(pokemon_url).json()

pokemon_name = response['name']
pokemon_height = response['height']

st.title(pokemon_name.title())
st.write (f"This pokemon is {pokemon_height} meters tall!")

col1,col2,col3 = st.columns(3)
col1.write("Pokemon number")
col2.write("Name")
col3.write("Height")
with col1:
    st.write()