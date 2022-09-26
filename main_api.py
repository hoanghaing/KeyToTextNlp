# pip install fastapi uvicorn asyncio pydantic typing
# python3 -m uvicorn main_api:app --reload
# Importing Necessary modules
from fastapi import FastAPI
import uvicorn
import asyncio
from pydantic import BaseModel
from typing import (List)

# Declaring our FastAPI instance
app = FastAPI()
 
# Declaring the request sample Modal
class request(BaseModel):
  titles: List[str] = None
# Defining path operation for root endpoint
@app.get('/')
def main():
    return { 'message': 'Welcome to HaiNH Intelligent API!' }
 
@app.post('/autofill')
def autofill(data: request):
  titles = data.titles
  paragraph = ''
  for title in titles:
    paragraph += f"{title}. "
  print(paragraph)
  return {
    'candidate': 'textIsHere',
    'description': 'thisIsDescription'
  }
if __name__ == "__main__":
    uvicorn.run("main_api:app", port=5077, log_level="info")