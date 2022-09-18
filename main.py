import spacy
from fastapi import FastAPI
from pydantic import BaseModel
import warnings
warnings.filterwarnings('ignore')

nlp = spacy.load('ja_ginza_electra')

app = FastAPI()

class Text(BaseModel):
    text: str

@app.get("/")
def hello():
    return {"hello": "world!"}

@app.post("/")
def parse(text: Text):
    doc = nlp(text.text)
    return doc.to_json()