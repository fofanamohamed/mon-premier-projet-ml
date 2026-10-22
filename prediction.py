
import pandas as pd
import joblib
from pathlib import Path


dossier_projet = Path(__file__).resolve().parent
chemin_modele = dossier_projet / "models" / "modele_iris_joblib.pth"

modele= joblib.load(chemin_modele
)

def predire_fleur(longueur_sepal, largeur_sepal, longueur_petal, largeur_petal):

    colonnes = [
        "sepal length (cm)",
        "sepal width (cm)",
        "petal length (cm)",
        "petal width (cm)"
    ]

    df_fleur = pd.DataFrame(
        [[longueur_sepal, largeur_sepal, longueur_petal, largeur_petal]],
        columns=colonnes
    )

    y_fleurs = modele.predict(df_fleur)

    noms_fleurs = ["setosa", "versicolor", "virginica"]

    return noms_fleurs[y_fleurs[0]]
