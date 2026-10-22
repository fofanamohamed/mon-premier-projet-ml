from fastapi import FastAPI
from prediction import predire_fleur
from pydantic import BaseModel

app = FastAPI()

class Fleur(BaseModel):
     longueur_sepal: float
     largeur_sepal: float
     longueur_petal: float
     largeur_petal: float


@app.post("/predict")
def predict(fleur: Fleur):
    prediction = predire_fleur(
	fleur.longueur_sepal,
	fleur.largeur_sepal,
	fleur.longueur_petal,
	fleur.largeur_petal
    )
    return {"prediction": prediction}	

@app.get("/")
def accueil():
    return {"message": "Bienvenue sur mon API Iris"}
