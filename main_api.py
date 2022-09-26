# pip install fastapi uvicorn asyncio pydantic typing yake
# python3 -m uvicorn main_api:app --reload
# Importing Necessary modules
from operator import le
from fastapi import FastAPI
import uvicorn
import asyncio
from pydantic import BaseModel
from typing import (List)
from googletrans import Translator
from transformers import pipeline
import re
import yake

# Declaring our FastAPI instance
app = FastAPI()
translator = Translator() 
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
  titlesToEnglish = translator.translate(titles, dest='en')
  paragraph = ''
  for translated in titlesToEnglish:
    if (translated.text):
      plainText = re.sub(r'[^\w]', ' ', translated.text).strip()
      paragraph += f"{plainText}. "   
  keywords = kwExtractor.extract_keywords(paragraph)
  candidateKeyword = ''
  generateDescription = ''
  if (len(keywords) > 0):
    candidateKeyword = keywords[0][0]
    if (candidateKeyword.find("is") == -1):
      candidateKeyword += ' is'
      candidateKeyword = "%s%s" % (candidateKeyword[0].upper(), candidateKeyword[1:]) #upper case first letter
    descript = generator(candidateKeyword, do_sample = True, max_new_tokens = 60)
    if (len(descript) > 0):
      generateDescription = descript[0]['generated_text']
      # generateDescription = generateDescription.strip('\n')
      # generateDescription = generateDescription.strip('\t')
      # generateDescription = re.sub('\s+', ' ', generateDescription)
      generateDescription.rsplit(' ', 1)[0] # remove last word
      generateDescription+='...'
  return {
    'candidate': candidateKeyword,
    'description': generateDescription,
  }
if __name__ == "__main__":
    uvicorn.run("main_api:app", port=5077, log_level="info")