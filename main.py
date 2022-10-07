import spacy
from fastapi import FastAPI
from pydantic import BaseModel
import warnings
warnings.filterwarnings('ignore')

nlp = spacy.load('ja_ginza_electra')

app = FastAPI()

class Received(BaseModel):
    text: str

@app.get("/")
def hello():
    return {"hello": "world!"}

@app.post("/")
def parse(rv: Received):
    return nlp(rv.text).to_json()