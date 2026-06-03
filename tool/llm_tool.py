from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv
load_dotenv(
)
llm = init_chat_model(
    model="llama-3.3-70b-versatile",
    model_provider="groq",
    temperature=0.7,
    api_key=os.getenv("GROQ_API_KEY")
)