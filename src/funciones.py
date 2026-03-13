def cantidad_perdidas(notas):
    contador = 0

    for nota in notas:
        if nota < 3:
            contador += 1

    return contador
