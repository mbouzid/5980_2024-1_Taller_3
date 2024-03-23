def decompose_to_kmers(sequence, k):
    kmers = []
    for i in range(len(sequence) - k + 1):
        kmers.append(sequence[i:i+k])
    return kmers

def fasta_to_kmers_dict(fasta_sequences, k):
    kmers_dict = {}
    for header, sequence in fasta_sequences.items():
        kmers_dict[header] = decompose_to_kmers(sequence, k)
    return kmers_dict

# Datos de ej de secuencias en formato fasta
fasta_sequences = {
    "seq1": "ATCGATCGATCG",
    "seq2": "CGATCGATCGAT",
    "seq3": "GATCGATCGATC",
    "seq4": "ATCGATCGATCG"
}

# Punto 1
k = 3
kmers_dict = fasta_to_kmers_dict(fasta_sequences, k)
print("K-mers generados por secuencia:")
for header, kmers in kmers_dict.items():
    print(header, ":", kmers)

# Punto 2
sequence_length = len(fasta_sequences["seq1"])
num_kmers_generated = sequence_length - k + 1
print("\nCantidad de k-mers generados por una secuencia de longitud", sequence_length, ":", num_kmers_generated)

# Punto 3
print("\nLa complejidad en tiempo del algoritmo de descomposición en k-mers es O(|S| * k)")