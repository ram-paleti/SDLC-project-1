import os
from dotenv import load_dotenv
import requests

load_dotenv()

WATSONX_API_KEY = os.getenv("WATSONX_API_KEY")
WATSONX_PROJECT_ID = os.getenv("WATSONX_PROJECT_ID")
WATSONX_MODEL_ID = os.getenv("WATSONX_MODEL_ID")

def query_watsonx(prompt: str):
    url = f"https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2024-05-01"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {WATSONX_API_KEY}"
    }

    payload = {
        "input": prompt,
        "model_id": WATSONX_MODEL_ID,
        "project_id": WATSONX_PROJECT_ID,
        "parameters": {
            "decoding_method": "greedy",
            "max_new_tokens": 300
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        print("Watsonx Error Response:", response.text)
        raise Exception(f"Watsonx error: {response.status_code}")

    return response.json().get("results", [{}])[0].get("generated_text", "")
