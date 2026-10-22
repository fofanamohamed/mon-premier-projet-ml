from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_accueil():
        reponse = client.get("/")
        assert reponse.status_code == 200
        assert reponse.json() == {"message": "Bienvenue sur mon API Iris"}
	


def test_prediction_api():
        fleur ={
           "longueur_sepal":5.1,
           "largeur_sepal": 3.5,
           "longueur_petal": 1.4,
           "largeur_petal": 0.2
        }
        reponse = client.post("/predict", json=fleur)
        assert reponse.status_code == 200
        assert reponse.json() == {"prediction": "setosa"}
