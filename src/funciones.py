def promedio_notas(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)