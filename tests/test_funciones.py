from src.funciones import cantidad_perdidas

def test_cantidad_perdidas():

    # caso normal
    assert cantidad_perdidas([4,2,1,5]) == 2

    # todas aprobadas
    assert cantidad_perdidas([3,4,5]) == 0

    # arreglo vacío
    assert cantidad_perdidas([]) == 0
