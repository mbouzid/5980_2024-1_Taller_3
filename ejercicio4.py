import time
from collections import Counter
from itertools import combinations

def jaccard_index_listas(A, B):
    intersection = len(set(A).intersection(B))
    union = len(set(A).union(B))
    return intersection / union if union != 0 else 0

def jaccard_index_kmers(A, B):
    intersection = len(A.intersection(B))
    union = len(A.union(B))
    return intersection / union if union != 0 else 0

def obtener_kmers(secuencia, k):
    return set([secuencia[i:i+k] for i in range(len(secuencia) - k + 1)])

def matriz_similitud(fasta, k):
    secuencias = fasta.values()
    n = len(secuencias)
    matriz = [[0] * n for _ in range(n)]
    for i, seq1 in enumerate(secuencias):
        for j, seq2 in enumerate(secuencias):
            kmers_seq1 = obtener_kmers(seq1, k)
            kmers_seq2 = obtener_kmers(seq2, k)
            similarity = jaccard_index_kmers(kmers_seq1, kmers_seq2)
            matriz[i][j] = similarity
    return matriz

# Uso
fasta = {
    "secuencia1": "ATCGATCGATCGATCG",
    "secuencia2": "ATCGATCGATCGATCG",
    "secuencia3": "ATCGATCGATCGATCG",
}

# Calcular para K=7
k_7_start_time = time.time()
matriz_similitud_k7 = matriz_similitud(fasta, k=7)
k_7_end_time = time.time()
print("Matriz de similitud para K=7:")
for row in matriz_similitud_k7:
    print(row)
print(f"Tiempo de ejecución para K=7: {k_7_end_time - k_7_start_time} segundos")

# Calcular para K=11
k_11_start_time = time.time()
matriz_similitud_k11 = matriz_similitud(fasta, k=11)
k_11_end_time = time.time()
print("\nMatriz de similitud para K=11:")
for row in matriz_similitud_k11:
    print(row)
print(f"Tiempo de ejecución para K=11: {k_11_end_time - k_11_start_time} segundos")