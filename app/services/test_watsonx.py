import os
from dotenv import load_dotenv
import requests

load_dotenv()

WATSONX_API_KEY = os.getenv("WATSONX_API_KEY")
WATSONX_PROJECT_ID = os.getenv("WATSONX_PROJECT_ID")
WATSONX_MODEL_ID = os.getenv("WATSONX_MODEL_ID")

# Step 1: Get IAM Token from API key
def get_iam_token(api_key):
    url = "https://iam.cloud.ibm.com/identity/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
        "apikey": api_key
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code != 200:
        print("IAM Error:", response.text)
        raise Exception("Failed to get IAM token")
    return response.json()["access_token"]

# Step 2: Query Watsonx
def query_watsonx(prompt: str):
    token = get_iam_token(WATSONX_API_KEY)

    url = "https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2024-05-01"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
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

# Step 3: Test it
if __name__ == "__main__":
    print("Testing Watsonx API…")
    result = query_watsonx("Generate a Python function to check if a number is prime.")
    print("RESULT:", result)
