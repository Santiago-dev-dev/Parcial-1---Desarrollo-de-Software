def cantidad_perdidas(notas):
    return sum(1 for nota in notas if nota < 3)
