import os
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY is missing from the .env file")

client = genai.Client(api_key=API_KEY)

MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-flash-latest")
print("Gemini model being used:", MODEL_NAME)


class ScreenAnalysis(BaseModel):
    activity_summary: str
    category: str
    intent_alignment: Literal[
        "aligned",
        "potential_distraction",
        "uncertain"
    ]
    reason: str
    confidence: float = Field(ge=0.0, le=1.0)


def analyze_screenshot(image_bytes: bytes, intention: str):

    prompt = f"""
    You are the screen activity analysis component of IntentGuard AI.

    The user's declared intention is:
    {intention}

    Analyse the supplied computer screenshot.

    Identify:
    1. What activity appears to be happening?
    2. What category does it belong to?
    3. Does the activity align with the user's intention?
    4. Explain your decision briefly.

    Use "aligned" when the visible activity supports the intention.
    Use "potential_distraction" when there is clear evidence of
    unrelated activity.
    Use "uncertain" when the screenshot does not provide enough
    evidence to make a reliable decision.

    Do not assume that an application is distracting simply
    because of its name. Consider the visible context.

    Do not infer activity that cannot be established from the image.
    """

    image_part = types.Part.from_bytes(
        data=image_bytes,
        mime_type="image/png"
    )

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=[prompt, image_part],
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=ScreenAnalysis
        )
    )

    if response.parsed is not None:
        return response.parsed.model_dump()

    raise ValueError("Gemini did not return a valid structured response")