import time
import numpy as np

def leer_fasta(archivo):
    secuencias = {}
    with open(archivo, 'r') as file:
        lineas = file.readlines()
        id_actual = None
        secuencia_actual = ''
        for linea in lineas:
            linea = linea.strip()
            if linea.startswith('>'):
                if id_actual:
                    secuencias[id_actual] = secuencia_actual
                id_actual = linea[1:]
                secuencia_actual = ''
            else:
                secuencia_actual += linea
        if id_actual:
            secuencias[id_actual] = secuencia_actual
    return secuencias

def indice_jaccard(A, B):
    interseccion = len(set(A).intersection(set(B)))
    union = len(set(A).union(set(B)))
    return interseccion / union

def indice_jaccard_kmers(kmers_A, kmers_B):
    interseccion = len(set(kmers_A).intersection(set(kmers_B)))
    union = len(set(kmers_A).union(set(kmers_B)))
    return interseccion / union

def obtener_kmers(secuencia, k):
    return [secuencia[i:i+k] for i in range(len(secuencia) - k + 1)]

def matriz_similitud_fasta(archivo, k):
    secuencias = leer_fasta(archivo)
    ids_secuencias = list(secuencias.keys())
    num_secuencias = len(ids_secuencias)
    matriz_similitud = np.zeros((num_secuencias, num_secuencias))

    for i in range(num_secuencias):
        for j in range(i, num_secuencias):
            jaccard = indice_jaccard_kmers(obtener_kmers(secuencias[ids_secuencias[i]], k), 
                                           obtener_kmers(secuencias[ids_secuencias[j]], k))
            matriz_similitud[i][j] = jaccard
            matriz_similitud[j][i] = jaccard  
    
    return matriz_similitud

archivo_fasta = "xylefa8416.fasta"
valores_k = [7, 11]

for k in valores_k:
    print(f"\nArchivo: {archivo_fasta}. Similitud para k = {k}:")
    inicio = time.time()
    matriz_similitud = matriz_similitud_fasta(archivo_fasta, k)
    fin = time.time()
    tiempo=fin-inicio
    print(matriz_similitud)
    print(f"Tiempo de ejecución para k = {k}: {tiempo} segundos")
    
