# pip install fastapi uvicorn pydantic typing yake
# python3 -m uvicorn main_api:app --reload
# Importing Necessary modules
from operator import le
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import (List)
from deep_translator import GoogleTranslator

from transformers import pipeline
import re
import yake

# Declaring our FastAPI instance
app = FastAPI()
translator = GoogleTranslator(source='auto', target='en') 
kwExtractor = yake.KeywordExtractor()
generator = pipeline('text-generation', model='./gpt-neo-125M')
# Declaring the request sample Modal
class request(BaseModel):
  titles: List[str] = None
# Defining path operation for root endpoint
@app.get('/')
def main():
    return { 'message': 'Welcome to HaiNH Intelligent API!' }
 
@app.post('/autofill')
async def autofill(data: request):
  titles = data.titles
  paragraph = ''
  for item in titles:
    englishVersion = translator.translate(item)
    paragraph += f"{englishVersion}. "  
  keywords = kwExtractor.extract_keywords(paragraph)
  candidateKeyword = ''
  generateDescription = ''
  if (len(keywords) > 0):
    candidateKeyword = keywords[0][0]
    if (candidateKeyword.find("is") == -1):
      candidateKeyword = "%s%s" % (candidateKeyword[0].upper(), candidateKeyword[1:]) #upper case first letter
    descript = generator(f"{candidateKeyword} is", do_sample = True, max_new_tokens = 30)
    if (len(descript) > 0):
      generateDescription = descript[0]['generated_text']
      generateDescription.rsplit(' ', 1)[0] # remove last word
      generateDescription+='...'
  return {
    'candidate': candidateKeyword,
    'description': generateDescription,
  }
if __name__ == "__main__":
    uvicorn.run("main_api:app", port=5077, log_level="info")