import os
from google import genai


def generate_script(topic: str):
    try:
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            print("GEMINI_API_KEY not found.")
            return None

        client = genai.Client(api_key=api_key)

        prompt = f"""
Write a 60-second engaging YouTube narration script about {topic}.

Requirements:
- Strong hook
- Energetic tone
- Short punchy sentences
- No headings
- No explanations

At the very end, on a new line, write:

VISUAL_KEYWORDS: followed by 8 short stock-photo friendly keywords separated by commas.

Format exactly like this:

<spoken script here>

VISUAL_KEYWORDS: keyword1, keyword2, keyword3, keyword4, keyword5, keyword6, keyword7, keyword8
"""

        response = client.models.generate_content(
            model="models/gemini-2.5-flash",
            contents=prompt,
        )

        if not response or not response.text:
            print("Empty response from Gemini.")
            return None

        return response.text.strip()

    except Exception as e:
        print("Script Error:", e)
        return None
