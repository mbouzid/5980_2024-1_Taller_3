def distancia_hamming(secuencia_a, secuencia_b):
    # Verificar que las secuencias tengan la misma longitud
    if len(secuencia_a) != len(secuencia_b):
        raise ValueError("Las secuencias deben tener la misma longitud")

    # Inicializar la distancia de Hamming
    distancia = 0

    # Calcular la distancia de Hamming|
    for i in range(len(secuencia_a)):
        if secuencia_a[i] != secuencia_b[i]:
            distancia += 1

    return distancia

def distancia_hamming(secuencia_a, secuencia_b):
    # Verificar que las secuencias tengan la misma longitud
    if len(secuencia_a) != len(secuencia_b):
        raise ValueError("Las secuencias deben tener la misma longitud")

    # Inicializar la distancia de Hamming
    distancia = 0

    # Calcular la distancia de Hamming
    for i in range(len(secuencia_a)):
        if secuencia_a[i] != secuencia_b[i]:
            distancia += 1

    return distancia

secuencia_1 = "AGTCGATCGA"
secuencia_2 = "AGTGGOTCGA"

print("Secuencia 1:", secuencia_1)
print("Secuencia 2:", secuencia_2)
print("Distancia de Hamming:", distancia_hamming(secuencia_1, secuencia_2))

#la complejidad en tiempo del algoritmo es O(n) ya que el algoritmo recorre ambas secuencias una vez

#PRINCIPAL INCONVENIENTE: es util a la hora de comparar secuencias de igual longitud y detectar cambios puntuales
#entre ellas. Pero, si hablamos de secuencias de ADN, las mutaciones pueden incluir inserciones, eliminaciones
#y sustituciones de bases. La distancia de hamming no tiene en cuenta estas operaciones y solo mide la diferencia
#entre las secuencias en terminos de cambios puntuales. Por lo tanto, esta secuencia no es apta para la diversidad
#genetica o las relaciones evolutivas. 