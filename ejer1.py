class FastaSequence:
    def __init__(self, identifier, sequence):
        self.identifier = identifier
        self.sequence = sequence

def parse_fasta(file_path):
    sequences = {}
    with open(file_path, 'r') as file:
        current_identifier = None
        current_sequence = ""
        for line in file:
            line = line.strip()
            if line.startswith('>'):  # Encabezado de secuencia
                if current_identifier:
                    sequences[current_identifier] = FastaSequence(current_identifier, current_sequence)
                    current_sequence = ""
                current_identifier = line[1:]
            else:  # Datos de secuencia
                current_sequence += line
        # Guardar la última secuencia
        if current_identifier:
            sequences[current_identifier] = FastaSequence(current_identifier, current_sequence)
    return sequences

# Ejemplo de uso
fasta_file_path = r'C:\Users\jorge\Documents\Taller_3_SJJA\5980_2024-1_Taller_3\data\xylefa8416.fasta'
sequences = parse_fasta(fasta_file_path)

# Imprimir todas las secuencias
for identifier, sequence in sequences.items():
    print("Identificador:", identifier)
    print("Secuencia de ADN:", sequence.sequence)



def cargar_secuencia_desde_archivo(archivo):
   
    with open(archivo, "r") as f:
        # Saltamos la primera línea (encabezado)
        next(f)
        # Leemos la secuencia
        secuencia = f.read().replace("\n", "")
    return secuencia
 
def distancia_hamming(secuencia_a, secuencia_b):
   
    if len(secuencia_a) != len(secuencia_b):
        raise ValueError("Las secuencias deben tener la misma longitud.")
 
    distance = 0
    for i in range(len(secuencia_a)):
        if secuencia_a[i] != secuencia_b[i]:
            distance += 1
 
    return distance
 
# Ejemplo de uso:
archivo_fasta_a = r'C:\Users\jorge\Documents\Taller_3_SJJA\5980_2024-1_Taller_3\data\xylefa8416.fasta'
archivo_fasta_b = r'C:\Users\jorge\Documents\Taller_3_SJJA\5980_2024-1_Taller_3\data\xylefa8416 copy.fasta'
 
secuencia_a = cargar_secuencia_desde_archivo(archivo_fasta_a)
secuencia_b = cargar_secuencia_desde_archivo(archivo_fasta_b)
 
distancia = distancia_hamming(secuencia_a, secuencia_b)
print(f"La distancia de Hamming entre las secuencias es: {distancia}")



def read_fasta(fasta_file):
    sequences = {}
    with open(fasta_file, 'r') as file:
        lines = file.readlines()
        current_id = None
        current_sequence = ""
        for line in lines:
            line = line.strip()
            if line.startswith(">"):
                if current_id:
                    sequences[current_id] = current_sequence
                current_id = line[1:]
                current_sequence = ""
            else:
                current_sequence += line
        # Añadir la última secuencia
        if current_id:
            sequences[current_id] = current_sequence
    return sequences

def decompose_to_kmers(sequence, k):
    kmers = []
    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i+k]
        kmers.append(kmer)
    return kmers

def decompose_fasta_to_kmers(fasta_file, k):
    sequences = read_fasta(fasta_file)
    kmers_dict = {}
    for seq_id, sequence in sequences.items():
        kmers = decompose_to_kmers(sequence, k)
        kmers_dict[seq_id] = kmers
    return kmers_dict

# Ejemplo de uso:
fasta_file = r'C:\Users\jorge\Documents\Taller_3_SJJA\5980_2024-1_Taller_3\data\xylefa8417.fasta'
k = 10
kmers_dict = decompose_fasta_to_kmers(fasta_file, k)
#print(kmers_dict)
print(len(kmers_dict))


import time

def jaccard_index(listA, listB):
    intersection = len(set(listA) & set(listB))
    union = len(set(listA) | set(listB))
    jaccard_similarity = intersection / union
    return jaccard_similarity

def jaccard_index_kmers(kmers_A, kmers_B):
    intersection = len(kmers_A.intersection(kmers_B))
    union = len(kmers_A.union(kmers_B))
    jaccard_similarity = intersection / union
    return jaccard_similarity

def read_fasta(fasta_file):
    sequences = {}
    with open(fasta_file, 'r') as file:
        lines = file.readlines()
        current_id = None
        current_sequence = ""
        for line in lines:
            line = line.strip()
            if line.startswith(">"):
                if current_id:
                    sequences[current_id] = current_sequence
                current_id = line[1:]
                current_sequence = ""
            else:
                current_sequence += line
        # Add the last sequence
        if current_id:
            sequences[current_id] = current_sequence
    return sequences

def decompose_to_kmers(sequence, k):
    kmers = set()
    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i+k]
        kmers.add(kmer)
    return kmers

def similarity_matrix(fasta_file, k):
    sequences = read_fasta(fasta_file)
    sequence_ids = list(sequences.keys())
    num_sequences = len(sequence_ids)
    similarity_matrix = [[0] * num_sequences for _ in range(num_sequences)]

    # Calculate the k-mers for each sequence
    kmers_dict = {}
    for seq_id, sequence in sequences.items():
        kmers_dict[seq_id] = decompose_to_kmers(sequence, k)

    # Calculate Jaccard similarity for all pairs of sequences
    for i in range(num_sequences):
        for j in range(i + 1, num_sequences):
            seq1_id = sequence_ids[i]
            seq2_id = sequence_ids[j]
            similarity = jaccard_index_kmers(kmers_dict[seq1_id], kmers_dict[seq2_id])
            similarity_matrix[i][j] = similarity
            similarity_matrix[j][i] = similarity

    return similarity_matrix

# Ejemplo de uso con dos archivos FASTA
fasta_files = [r"C:\Users\jorge\Documents\Taller_3_SJJA\5980_2024-1_Taller_3\data\xylefa8416.fasta", r"C:\Users\jorge\Documents\Taller_3_SJJA\5980_2024-1_Taller_3\data\xylefaco6c.fasta"]
k_values = [7, 11]

for fasta_file in fasta_files:
    print(f"Archivo FASTA: {fasta_file}")
    for k in k_values:
        start_time = time.time()
        sim_matrix = similarity_matrix(fasta_file, k)
        execution_time = time.time() - start_time
        print(f"\nMatriz de similitud para k={k}:")
        for row in sim_matrix:
            print(row)
        print(f"Tiempo de ejecución para k={k}: {execution_time} segundos\n")
