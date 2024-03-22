import time


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
            if line.startswith('>'):
                if current_identifier is not None:
                    sequences[current_identifier] = FastaSequence(current_identifier, current_sequence)
                current_identifier = line[1:].split()[0]
                current_sequence = ""
            else:
                current_sequence += line
        if current_identifier is not None:
            sequences[current_identifier] = FastaSequence(current_identifier, current_sequence)
    return sequences


def hamming_distance(seq1, seq2):
    if len(seq1.sequence) != len(seq2.sequence):
        print("Las secuencias tienen longitudes diferentes")
        return
    distance = 0
    for char1, char2 in zip(seq1.sequence, seq2.sequence):
        if char1 != char2:
            distance += 1
    return distance


def generate_kmers(sequence, k):
    kmers = set()
    for i in range(len(sequence) - k + 1):
        kmers.add(sequence[i:i + k])
    return kmers


def jaccard_index_list(list_a, list_b):
    intersection = len(set(list_a) & set(list_b))
    union = len(set(list_a) | set(list_b))
    return intersection / union if union != 0 else 0


def jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union != 0 else 0


def calculate_jaccard_similarity_for_n_files(file_paths, k):
    similarities = {}
    kmer_sets = {}
    for file_path in file_paths:
        sequences = parse_fasta(file_path)
        all_kmers = set()
        for sequence in sequences.values():
            all_kmers.update(generate_kmers(sequence.sequence, k))
        kmer_sets[file_path] = all_kmers

    for i in range(len(file_paths)):
        for j in range(i + 1, len(file_paths)):
            file1 = file_paths[i]
            file2 = file_paths[j]
            similarity = jaccard_similarity(kmer_sets[file1], kmer_sets[file2])
            similarities[(file1, file2)] = similarity

    return similarities


def print_similarity_matrix(similarities, file_paths):
    print("Similarity Matrix:")
    print("\t" + "\t".join(file_paths))
    for file1 in file_paths:
        row = [file1]
        for file2 in file_paths:
            if file1 == file2:
                row.append("1.0")
            elif (file1, file2) in similarities:
                row.append("{:.4f}".format(similarities[(file1, file2)]))
            else:
                row.append("-")
        print("\t".join(row))


file_paths = ["data/xylefa8416.fasta", "data/xylefa8417.fasta", "data/xylefaco6c.fasta",
              "data/xylefaco32.fasta", "data/xylefaco33.fasta", "data/xylefacodi.fasta"]
k = 11

start_time = time.time()
similarities = calculate_jaccard_similarity_for_n_files(file_paths, k)
end_time = time.time()
execution_time = end_time - start_time
print_similarity_matrix(similarities, file_paths)
print("Tiempo de ejecución:", execution_time, "segundos")