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


from collections import Counter
import time

def jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union != 0 else 0

def kmerize(sequence, k):
    return set(sequence[i:i+k] for i in range(len(sequence) - k + 1))

def jaccard_index_kmers(kmers_A, kmers_B):
    return jaccard_similarity(kmers_A, kmers_B)

def fasta_to_kmers_similarity_matrix(fasta_file, k):
    sequences = {}
    kmers = {}
    similarity_matrix = {}

    # Leer el archivo fasta y obtener kmers para cada secuencia
    with open(fasta_file, "r") as f:
        sequence_id = ""
        sequence = ""
        for line in f:
            if line.startswith(">"):
                if sequence_id:
                    sequences[sequence_id] = sequence
                    kmers[sequence_id] = kmerize(sequence, k)
                sequence_id = line.strip()[1:]
                sequence = ""
            else:
                sequence += line.strip().upper()
        # Agregar el último registro
        if sequence_id:
            sequences[sequence_id] = sequence
            kmers[sequence_id] = kmerize(sequence, k)

    # Calcular la similitud para cada par de secuencias
    for id_A, kmers_A in kmers.items():
        similarity_matrix[id_A] = {}
        for id_B, kmers_B in kmers.items():
            similarity_matrix[id_A][id_B] = jaccard_index_kmers(kmers_A, kmers_B)

    return similarity_matrix

# Ejemplo de uso con archivos fasta de conjuntos A y B
fasta_file_A = r"C:\Users\jorge\Documents\Taller_3_SJJA\5980_2024-1_Taller_3\data\xylefaco33.fasta"
fasta_file_B = r"C:\Users\jorge\Documents\Taller_3_SJJA\5980_2024-1_Taller_3\data\xylefacodi.fasta"

# Calcular la matriz de similitud para k=7
k_value = 7
start_time = time.time()
similarity_matrix_k7 = fasta_to_kmers_similarity_matrix(fasta_file_A, k_value)
end_time = time.time()
print("Matriz de similitud para k=7:")
for id_A, sim_row in similarity_matrix_k7.items():
    print(id_A, sim_row)
print("Tiempo de ejecución para k=7:", end_time - start_time, "segundos")

# Calcular la matriz de similitud para k=11
k_value = 11
start_time = time.time()
similarity_matrix_k11 = fasta_to_kmers_similarity_matrix(fasta_file_A, k_value)
end_time = time.time()
print("\nMatriz de similitud para k=11:")
for id_A, sim_row in similarity_matrix_k11.items():
    print(id_A, sim_row)
print("Tiempo de ejecución para k=11:", end_time - start_time, "segundos")