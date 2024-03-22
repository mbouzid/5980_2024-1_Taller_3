
#ESTEBAN BERNAL-NICOLAS ALMONACID-JUAN GOMEZ-FELIPE ABELLA
# Ejercicio 3

## 1. ¿Cuántos k-mers se generan por una secuencia de longitud |S|?

El número de k-mers se calcula utilizando la fórmula:

Número de k-mers = S - k + 1
                  = 304552 - 5 + 1 = 304548

## 2. ¿Cuál es la complejidad en tiempo del algoritmo de descomposición en k-mers de una secuencia S dada?

Dado que la longitud de la secuencia S es mucho mayor que la longitud de los k-mers k en este caso, se puede simplificar la complejidad a O(S). Entonces, la complejidad en tiempo del algoritmo sería aproximadamente O(304552), es decir, O(304552).

# Ejercicio 2

## 1. La complejidad en tiempo del algoritmo

La complejidad en tiempo del algoritmo es O(n), donde n es la longitud de las secuencias. Esto se debe a que el algoritmo recorre ambas secuencias una vez para calcular la distancia de Hamming.

## 2. Limitaciones del algoritmo de distancia de Hamming

La principal limitación es que la distancia de Hamming no tiene en cuenta las inserciones, eliminaciones o reordenamientos de bases en las secuencias de ADN. Es decir, solo mide la diferencia en caracteres en las mismas posiciones entre las secuencias. En biología molecular, las mutaciones y cambios genéticos pueden implicar no solo diferencias en bases individuales, sino también cambios estructurales en la secuencia. Por lo tanto, la distancia de Hamming puede subestimar la divergencia real entre las secuencias de ADN. Para tener en cuenta estas variaciones estructurales, se pueden utilizar otras medidas de similitud o distancia, como la distancia de Levenshtein o algoritmos de alineamiento de secuencias.