from openai import (
    OpenAI
)

from app import (
    AI_API_KEY
)

def generate_ai_answer(system_prompt,
                       user_prompt):

    client = OpenAI(api_key=AI_API_KEY,
                    base_url='https://openrouter.ai/api/v1')

    response = client.chat.completions.create(
        model='google/gemini-2.0-flash-lite-preview-02-05:free',
        messages=[
            {"role":"system","content":f"{system_prompt}"},
            {"role":"user","content":f"{user_prompt}"},
        ]
    )

    return response.choices[0].message.content