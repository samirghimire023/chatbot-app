import os
from openai import OpenAI

client = OpenAI(
    api_key= os.getenv("API_KEY"), # Replace with your actual API key
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

command = '''
[22:31, 07/02/2026] friend: Hi
[22:31, 07/02/2026] Me : hlo how can i help you
'''

completion = client.chat.completions.create(
        model="gemini-2.5-flash", # Use a Gemini model name here
        messages=[
            {"role": "system", "content": "You are a person named Samir who speak Nepali as well as English. He id from Nepal and he is learning coding. He is very good at coding and he is very helpful. you analyze chat history and speaks and respond like Samir"},
            {"role": "user", "content": command}
        ]
    )
answer = completion.choices[0].message.content
print(answer)
