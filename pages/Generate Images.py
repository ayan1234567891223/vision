import requests
import streamlit as st

st.subheader("Enter Your OpenAI Key To Use All The Features")

open_ai_key = st.text_input("OpenAI Key (Press enter after putting your OpenAI API Key)")

def makeimage(prompt: str):
    response = requests.post("https://api.openai.com/v1/images/generations", headers={"Content-Type": "application/json", "Authorization": "Bearer " + open_ai_key}, json={
        "model": "dall-e-3",
        "prompt": prompt,
        "n": 1,
        "size": "1024x1024"
    })
    
    image_url = response
    
    st.write(image_url)

st.subheader("Generate Images Using AI")

promptinput = st.text_input("Prompt")

if promptinput:
    makeimage(prompt=promptinput)