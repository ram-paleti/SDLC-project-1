from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.ai_routes import router as ai_router

app = FastAPI(
    title="SmartSDLC",
    description="AI-enhanced SDLC Automation Platform",
    version="1.0.0"
)

# Allow requests from Streamlit (frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, use specific domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include AI route
app.include_router(ai_router, prefix="/ai")

@app.get("/")
def read_root():
    return {"message": "SmartSDLC backend is running"}
