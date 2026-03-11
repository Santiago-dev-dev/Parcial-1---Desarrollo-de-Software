from src.funciones import promedio_notas

def test_arreglo_vacio():
    assert promedio_notas([]) == 0

def test_promedio_normal():
    notas = [3, 4, 5]
    assert promedio_notas(notas) == 4

def test_notas_extremos():
    notas = [0, 5]
    assert promedio_notas(notas) == 2.5