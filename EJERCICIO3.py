class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]


    def _hash(self, key):
        return sum(ord(char) for char in key) % self.size


    def insert(self, key, value):
        index = self._hash(key)
        self.table[index].append((key, value))


def parse_fasta(file_path, k):
    kmer_table = HashTable(100000)
    with open(file_path, 'r') as file:
        data = file.read()
    sequences = data.strip().split('\n>')
    for sequence in sequences:
        lines = sequence.split('\n')
        header = lines[0]
        seq = ''.join(lines[1:])
        store_kmers(seq, k, header, kmer_table)
    return kmer_table


def store_kmers(sequence, k, header, kmer_table):
    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i+k]
        kmer_table.insert(kmer, header)


def print_kmers(kmer_table):
    for bucket in kmer_table.table:
        for kmer, header in bucket:
            print(f"{kmer}: {header}")


fasta_data = 'C:/Users/juanf/OneDrive/Escritorio/Estructura/xylefa8416.fasta'
k = 5
kmer_table = parse_fasta(fasta_data, k)
print_kmers(kmer_table)
