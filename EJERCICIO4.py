import time

def jaccard_index(A, B):
    intersection = len(set(A).intersection(B))
    union = len(set(A).union(B))
    return intersection / union if union != 0 else 0

def calculate_jaccard_index(k_mers_A, k_mers_B):
    return jaccard_index(k_mers_A, k_mers_B)

def read_fasta(file_path):
    sequences = {}
    current_sequence = ""
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if current_sequence:
                    sequences[sequence_name] = current_sequence
                    current_sequence = ""
                sequence_name = line[1:]
            else:
                current_sequence += line
        if current_sequence:
            sequences[sequence_name] = current_sequence
    return sequences

def get_k_mers(sequence, k):
    k_mers = []
    for i in range(len(sequence) - k + 1):
        k_mers.append(sequence[i:i + k])
    return k_mers

def calculate_similarity_matrix(sequences, k):
    similarity_matrix = {}
    for name1, sequence1 in sequences.items():
        similarity_matrix[name1] = {}
        k_mers1 = set(get_k_mers(sequence1, k))
        for name2, sequence2 in sequences.items():
            k_mers2 = set(get_k_mers(sequence2, k))
            similarity_matrix[name1][name2] = calculate_jaccard_index(k_mers1, k_mers2)
    return similarity_matrix

# Lectura de datos fasta y cálculo de la matriz de similitud para K=7 y K=11
sequences = read_fasta("ejercicio_4.fasta")

start_time_k7 = time.time()
similarity_matrix_k7 = calculate_similarity_matrix(sequences, 7)
end_time_k7 = time.time()

start_time_k11 = time.time()
similarity_matrix_k11 = calculate_similarity_matrix(sequences, 11)
end_time_k11 = time.time()

# Impresión de la matriz de similitud y tiempos de ejecución
print("Matriz de similitud para K=7:")
for name, sim in similarity_matrix_k7.items():
    print(name, sim)

print("\nMatriz de similitud para K=11:")
for name, sim in similarity_matrix_k11.items():
    print(name, sim)

# Tiempos de ejecución
print(f"\nTiempo de ejecución para K=7: {end_time_k7 - start_time_k7} segundos")
print(f"Tiempo de ejecución para K=11: {end_time_k11 - start_time_k11} segundos")