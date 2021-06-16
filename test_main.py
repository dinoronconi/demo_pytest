from operaciones import suma
from prediccion_math import  implemento_modelo

def setup():
    # hago todo lo que necesito hacer siempre al inicio de lso tests
    print("Comienzo tests")
    
def teardown():
    # hago todo lo que necesito hacer siempre al final de los tests
    print("Finalizo tests")

def test_suma():
    assert suma(2, 2) == 4

def test_modelo():
    score = implemento_modelo('StudentsPerformance.csv')
    assert score > 0.2


