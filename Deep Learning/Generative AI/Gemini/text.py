import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


model = genai.GeneraiveModel('gemini-pro')
input = "what is data science"

response = model.generate_content(input)
print(response.text)