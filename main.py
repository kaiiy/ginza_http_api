import spacy
from fastapi import FastAPI
from pydantic import BaseModel
from pymagnitude import Magnitude, MagnitudeUtils
import warnings
warnings.filterwarnings('ignore')

vectors = Magnitude(MagnitudeUtils.download_model("chive-1.2-mc90", remote_path="https://sudachi.s3-ap-northeast-1.amazonaws.com/chive/", download_dir="./.magnitude"))


nlp = spacy.load('ja_ginza_electra')

app = FastAPI()

class Received(BaseModel):
    text: str

@app.get("/")
def hello():
    return {"hello": "world!"}

@app.post("/")
def parse(rv: Received):
    doc_json = nlp(rv.text).to_json()

    # add word vectors
    doc_json["vecs"] = []
    for token in doc_json["token"]:
        doc_json["vecs"].append({
            "id": token["id"],
            "vec": vectors.query(token["lemma"])
        })

    return doc_json 