# pip install fastapi uvicorn pydantic typing yake
# python3 -m uvicorn main_api:app --reload
# Importing Necessary modules
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import (List)
from deep_translator import GoogleTranslator
import yake

# Declaring our FastAPI instance
app = FastAPI()
translator = GoogleTranslator(source='auto', target='en') 
kwExtractor = yake.KeywordExtractor(n=2, lan='en', top=5)
# Declaring the request sample Modal
class request(BaseModel):
  titles: List[str] = None
  description: str
# Defining path operation for root endpoint
@app.get('/')
def main():
    return { 'message': 'Welcome to HaiNH Intelligent API!' }
import time 
@app.post('/autofill')
async def autofill(data: request):
  titles = data.titles
  description = data.description
  paragraph = ''
  keywords = ''
  for item in titles:
    englishVersion = translator.translate(item)
    paragraph += f"{englishVersion}. "
  if (description and len(description) > 10):
    description = translator.translate(description)
    paragraph += description
  keywords = kwExtractor.extract_keywords(paragraph)
  candidateKeyword = ''
  if (len(keywords) > 0):
    candidateKeyword = keywords[0][0]
  return {
    'candidate': candidateKeyword,
  }
if __name__ == "__main__":
    uvicorn.run("main_api:app", port=5077, log_level="info")