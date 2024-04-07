import streamlit as st
from openai import OpenAI

st.subheader("Enter Your OpenAI Key To Use All The Features")

open_ai_key = st.text_input("OpenAI Key (Press enter after putting your OpenAI API Key)")

client = OpenAI(api_key=open_ai_key, organization="org-bghRR0Lowkz6U0iE0yxHIq0a")

def makeimage(prompt: str):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url
    
    st.image(image=image_url, caption=prompt)

st.subheader("Generate Images Using AI")

promptinput = st.text_input("Prompt")
if promptinput:
    makeimage(prompt=promptinput)