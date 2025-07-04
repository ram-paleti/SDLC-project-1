from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.watsonx_service import query_watsonx

router = APIRouter()

class PromptInput(BaseModel):
    prompt: str

@router.post("/generate-code")
def generate_code(input_data: PromptInput):
    try:
        print("Prompt received:", input_data.prompt)  # ✅ Add logging
        result = query_watsonx(prompt=input_data.prompt)
        print("AI response:", result)  # ✅ Add logging
        return {"generated_code": result}
    except Exception as e:
        print("❌ ERROR:", e)  # ✅ Show full error
        raise HTTPException(status_code=500, detail=str(e))
