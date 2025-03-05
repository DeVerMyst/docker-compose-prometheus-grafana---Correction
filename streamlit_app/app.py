from loguru import logger
import streamlit as st
import requests
import os

# Récupération de l'URL de l'API depuis les variables d'environnement
api_url = f"http://api:{os.getenv('FASTAPI_PORT', '8080')}"
log_file = "logs/app.log"

# Configuration de Loguru pour sauvegarder les logs
logger.add(log_file, rotation="10 MB", retention="7 days", level="INFO")

st.title("Data Sender")

choices = ["Red", "Blue", "Green", "Yellow"]
selected_data = st.selectbox("Choose a data", choices)

if st.button("Send Data"):
    logger.info(f"Sent data: {selected_data}")
    try:
        response = requests.post(f"{api_url}/data", data={"data": selected_data})
        st.write(response.json())
    except requests.exceptions.RequestException as e:
        logger.error(f"Error sending data: {selected_data}")
        st.error(f"Error: {e}")
