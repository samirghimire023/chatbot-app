from openai import OpenAI

# 1. Setup the client to point to Google instead of OpenAI
client = OpenAI(
    api_key="AIzaSyCDZA5Zm3kxMkssI1t0LTPdCtWS8JOu59s", # Replace with your actual Gemini API key
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
command = '''
[22:31, 07/02/2026] Niraj Khadka: College janxau hola ni temi
[22:31, 07/02/2026] Samir Ghimire: Tara space dherai hunxa
Space pani paisa pani Yetholm rent ka bata tirnu
[22:32, 07/02/2026] Samir Ghimire: College janxau hola ni temi
Umm jney ni
[22:32, 07/02/2026] Niraj Khadka: Space pani paisa pani Yetholm rent ka bata tirnu
Ahh
[16:53, 08/02/2026] Samir Ghimire: oee
[16:54, 08/02/2026] Niraj Khadka: Ha
[16:54, 08/02/2026] Samir Ghimire: kina naaako clz
[16:55, 08/02/2026] Niraj Khadka: Nidra pugya thiyena suteko yrr
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
