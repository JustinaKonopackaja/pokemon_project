import streamlit as st
import pandas as pd
import requests
import altair as alt

st.title('Pokemon Explorer!(❁´◡`❁)')

pokemon_num = st.slider("Choose a pokemon!", 1, 1025)

def get_response(poke_num):
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{poke_num}"
    return requests.get(pokemon_url).json()

pokemon_name = get_response(pokemon_num)['name']
poke_pic = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_num}.png"
roar = f"https://raw.githubusercontent.com/PokeAPI/cries/main/cries/pokemon/latest/{pokemon_num}.ogg"
pokemon_height = get_response(pokemon_num)['height']
pokemon_weight = get_response(pokemon_num)['weight']

st.title(pokemon_name.title())
st.image(poke_pic)
st.audio(roar)
st.write (f"This pokemon is {pokemon_height} meters tall!")
st.write (f"This pokemon weights {pokemon_weight} kg!")

col1,col2 = st.columns(2)
col1.write("Pokemon number:")
with col1:
    st.write("Name:")
    st.write("Height:")
col2.write(pokemon_num)
with col2:
    st.write(pokemon_name)
    st.write(pokemon_height)


height_data = pd.DataFrame({
    "Name": [pokemon_name, "Pidgey", "Victreebel"],
    "Height": [pokemon_height, get_response(16)['height'], get_response(71)['height']]
    })

height_chart = alt.Chart(height_data).mark_bar().encode(
    x = "Name",
    y = "Height",
)
st.altair_chart(height_chart, use_container_width=True)

weight_data = pd.DataFrame({
    "Name": [pokemon_name, "Pidgey", "Victreebel"],
    "Weight": [pokemon_weight, get_response(16)['weight'], get_response(71)['weight']]
    })

weight_chart = alt.Chart(weight_data).mark_bar().encode(
    x = "Name",
    y = "Weight",
)
st.altair_chart(weight_chart, use_container_width=True)