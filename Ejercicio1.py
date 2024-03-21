def load_fasta(filename):
    with open(filename, 'r') as file:
        sequences = {}
        sequence = ""
        header = ""
        for line in file:
            if line.startswith('>'):
                if header:
                    sequences[header] = sequence
                header = line.strip()
                sequence = ""
            else:
                sequence += line.strip()
        if header:
            sequences[header] = sequence
        lsequences = list(sequences.values())
        return lsequences[127]

print(load_fasta("xylefa8416.fasta"))