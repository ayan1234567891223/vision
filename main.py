import base64
import requests
import streamlit as st
import pandas as pd
import numpy as np

st.title('AI Vision')

image_bin = st.file_uploader("Upload image files", )

def inimg(imagepath):
  # Function to encode the image
  def encode_image(image_path):
      return base64.b64encode(image_bin.read()).decode('utf-8')

  # Getting the base64 string
  base64_image = encode_image(image_bin)

  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer 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"
  }

  payload = {
    "model": "gpt-4-vision-preview",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "What’s in this image?"
          },
          {
            "type": "image_url",
            "image_url": {
              "url": f"data:image/jpeg;base64,{base64_image}"
            }
          }
        ]
      }
    ],
    "max_tokens": 300
  }

  response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
  st.write(response.json())

if image_bin is not None:
  inimg(image_bin)
