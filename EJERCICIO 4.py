def jaccard_index(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    intersection = len(set_a.intersection(set_b))
    union = len(set_a.union(set_b))
    return intersection / union if union != 0 else 0  # Para evitar división por cero


def jaccard_index_kmers(kmers_a, kmers_b):
    return jaccard_index(kmers_a, kmers_b)


def fasta_to_kmers(fasta_sequence, k):
    kmers = []
    for sequence in fasta_sequence:
        kmers.extend([sequence[i:i+k] for i in range(len(sequence) - k + 1)])
    return kmers


def similarity_matrix(fasta_sequences, k):
    num_sequences = len(fasta_sequences)
    similarity_mat = [[0] * num_sequences for _ in range(num_sequences)]
    for i in range(num_sequences):
        for j in range(i, num_sequences):
            kmers_i = fasta_to_kmers(fasta_sequences[i], k)
            kmers_j = fasta_to_kmers(fasta_sequences[j], k)
            similarity_mat[i][j] = jaccard_index_kmers(kmers_i, kmers_j)
            similarity_mat[j][i] = similarity_mat[i][j]
    return similarity_mat


# Datos de ejemplo de secuencias en formato fasta
fasta_sequences = [
    "ATCGATCGATCG",
    "ATCGATCGATCG",
    "ATCGATCGATCG",
    "ATCGATCGATCG"
]

# Calcular matriz similitud K = 7
import time

start_time = time.time()
similarity_mat_k7 = similarity_matrix(fasta_sequences, 7)
end_time = time.time()
print("Matriz de similitud para K = 7:")
for row in similarity_mat_k7:
    print(row)
print("Tiempo de ejecución para K = 7:", end_time - start_time, "segundos")

# Calcular matriz similitud K = 11
start_time = time.time()
similarity_mat_k11 = similarity_matrix(fasta_sequences, 11)
end_time = time.time()
print("\nMatriz de similitud para K = 11:")
for row in similarity_mat_k11:
    print(row)
print("Tiempo de ejecución para K = 11:", end_time - start_time, "segundos")
