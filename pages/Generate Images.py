import requests
import streamlit as st
from openai import OpenAI

st.subheader("Enter Your OpenAI Key To Use All The Features")

open_ai_key = st.text_input("OpenAI Key (Press enter after putting your OpenAI API Key)")

client = OpenAI()
client.api_key = open_ai_key
client.organization = "org-bghRR0Lowkz6U0iE0yxHIq0a"

def makeimage(prompt: str):
    response = requests.post("https://api.openai.com/v1/images/generations", headers={"Content-Type": "application/json", "Authorization": "Bearer " + open_ai_key}, json={
        "model": "dall-e-3",
        "prompt": prompt,
        "n": 1,
        "size": "1024x1024"
    })
    
    image_url = response.data[0].url
    
    st.image(image_url)

st.subheader("Generate Images Using AI")

promptinput = st.text_input("Prompt")
if promptinput:
    makeimage(prompt=promptinput)