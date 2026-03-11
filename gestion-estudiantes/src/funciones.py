def maxima_nota(notas):
    if not notas:  # Si la lista está vacía, devolvemos 0 o un mensaje adecuado
        return 0
    return max(notas)  # Usamos la función max para obtener la máxima nota
