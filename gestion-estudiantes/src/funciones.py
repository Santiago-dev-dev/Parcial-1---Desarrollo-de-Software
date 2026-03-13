# src/funciones.py

def hallar_maxima_nota(notas):
    if not notas:
        return None  
    
   
    notas_validas = [nota for nota in notas if isinstance(nota, (int, float)) and 0 <= nota <= 5]
    
 
    if not notas_validas:
        return None

    
    return max(notas_validas)
