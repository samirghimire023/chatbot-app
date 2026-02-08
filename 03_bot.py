import pyautogui
import pyperclip
import time
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

if not os.getenv("API_KEY"):
    raise ValueError("API_KEY not found. Check your .env file")


client = OpenAI(
    api_key= os.getenv("API_KEY"), # Replace with your API key
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Small delay so we can switch to the target window
time.sleep(2)

# 1. Click on the icon at (1074, 1049)
pyautogui.click(1078, 1047)
time.sleep(0.3)

# 2. Drag to select text (from x1,y1 to x2,y2)
pyautogui.moveTo(738, 195)
pyautogui.dragTo(1904, 956, duration=1.0, button='left')

time.sleep(0.2)

# 3. Copy selected text 
pyautogui.hotkey('ctrl', 'c')
pyautogui.click(1272, 740)
time.sleep(0.2)

# 4. Get text from clipboard into a variable
chat_history = pyperclip.paste()
 
print("Chat history:")
print(chat_history)

completion = client.chat.completions.create(
        model="gemini-2.5-flash", # Use a Gemini/Open ai model name here
        messages=[
            {"role": "system", "content": "You are a person named Samir who speak Nepali as well as English. He id from Nepal and he is learning coding. He is very good at coding and he is very helpful. you analyze chat history and speaks and respond like Samir"},
            {"role": "user", "content": chat_history}
        ]
    )

response = completion.choices[0].message.content
print(response)  
pyperclip.copy(response)


# Click at the chat box coordinates
pyautogui.click(904, 955)

# Paste the text (Ctrl+V)
pyautogui.hotkey('ctrl', 'v')

# Press Enter to send
pyautogui.press('enter')

