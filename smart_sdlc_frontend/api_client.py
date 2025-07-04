import requests

BASE_URL = "http://127.0.0.1:8000"

def generate_code(prompt: str):
    try:
        response = requests.post(
            f"{BASE_URL}/ai/generate-code",
            json={"prompt": prompt}
        )
        response.raise_for_status()
        return response.json()["generated_code"]
    except Exception as e:
        return f"❌ Error: {str(e)}"
