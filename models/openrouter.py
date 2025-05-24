from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

model_client = OpenAI(
        api_key=os.getenv("MODEL_API_KEY"),
        base_url="https://openrouter.ai/api/v1"
    )
