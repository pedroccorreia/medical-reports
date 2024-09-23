#!/bin/bash
source .venv/bin/activate
echo '1'

pip install -r requirements.txt
export  GOOGLE_APPLICATION_CREDENTIALS="secrets/credentials.json"
streamlit run home.py