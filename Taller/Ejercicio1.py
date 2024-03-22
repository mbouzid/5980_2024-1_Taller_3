class FastaSequence:
    def __init__(self, identifier, sequence):
        self.identifier = identifier
        self.sequence = sequence

def parse_fasta(file_path):
    sequences = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        identifier = ''
        sequence = ''
        for line in lines:
            line = line.strip()
            if line.startswith('>'):
                if identifier and sequence:
                    sequences.append(FastaSequence(identifier, sequence))
                identifier = line[1:]
                sequence = ''
            else:
                sequence += line
        if identifier and sequence:
            sequences.append(FastaSequence(identifier, sequence))
    return sequences

file_path = 'xylefa8416.fasta'
fasta_sequences = parse_fasta(file_path)
for seq in fasta_sequences:
    print(f'Identifier: {seq.identifier}')
    print(f'Sequence: {seq.sequence}')
    print()