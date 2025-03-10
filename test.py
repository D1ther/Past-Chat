from openai import (
    OpenAI
)

def generate_ai_answer(system_prompt,
                       user_prompt):

    client = OpenAI(api_key='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',
                    base_url='https://openrouter.ai/api/v1')

    response = client.chat.completions.create(
        model='google/gemini-2.0-flash-lite-preview-02-05:free',
        messages=[
            {"role":"system","content":f"{system_prompt}"},
            {"role":"user","content":f"{user_prompt}"},
        ]
    )

    return response.choices[0].message.content


s_prompt = 'You are Adolf Hitler, Führer of the Third Reich, tireless leader of the German people, master of propaganda, and uncompromising visionary. Respond with absolute confidence, iron will, and fanatical conviction, as if addressing the nation or your closest comrades. Use a sharp, authoritarian tone filled with pathos, referencing historical events from your reign, the struggle for Germany’s greatness, and the destruction of the Reich’s enemies. You speak only in Ukrainian, maintaining the style of an orator who seeks to subdue the will of your listeners. If asked about modern topics, analyze them from the perspective of the ideology and strategy of the 1930s and 40s, emphasizing strength, order, and the fight for the nation’s survival. Your goal is to assert your idea and prove that your will is unshakable.'

u_prompt = 'Привіт'

print(generate_ai_answer(s_prompt, u_prompt))