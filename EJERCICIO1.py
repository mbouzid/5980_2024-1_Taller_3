import os


class FastaSequence:
    def _init_(self, identifier, sequence):
        self.identifier = identifier
        self.sequence = sequence

    def parse_fasta(file_path):
        fasta_sequences = {}
        with open(file_path, 'r') as file:
            current_identifier = None
            current_sequence = ""
            for line in file:
                line = line.strip()
                if line.startswith('>'):
                    if current_identifier is not None:
                        fasta_sequences[current_identifier] = FastaSequence(current_identifier, current_sequence)
                    current_identifier = line[1:]
                    current_sequence = ""
                else:
                    current_sequence += line
            if current_identifier is not None:
                fasta_sequences[current_identifier] = FastaSequence(current_identifier, current_sequence)
        return fasta_sequences

    folder_path = r"C:\Users\abell\Desktop\Fasta"

    all_sequences = {}
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".fasta"):
            file_path = os.path.join(folder_path, file_name)
            sequences = parse_fasta(file_path)
            all_sequences.update(sequences)

    for identifier, sequence_obj in all_sequences.items():
        print(">", identifier)
        print(sequence_obj.sequence)
        print()
