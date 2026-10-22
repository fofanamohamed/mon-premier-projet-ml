

from prediction import predire_fleur

def test_prediction_setosa():
    assert predire_fleur(5.1, 3.5, 1.4, 0.2) == "setosa"


def test_prediction_virginica():
    assert predire_fleur(6.5, 3.0, 5.2, 2.0) == "virginica"
    
def test_prediction_versicolor():
    assert predire_fleur(5.7, 2.8, 4.1, 1.3) == "versicolor"
