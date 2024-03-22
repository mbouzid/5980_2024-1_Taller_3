def hamming_distance(seq1, seq2):
    if len(seq1) != len(seq2):
        raise ValueError("Las secuencias deben tener la misma longitud.")
    hamming_dist = 0

    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            hamming_dist += 1

    return hamming_dist


seq1 = input("Ingrese la primera secuencia: ")
seq2 = input("Ingrese la segunda secuencia: ")

try:
    distance = hamming_distance(seq1, seq2)
    print("La distancia de Hamming entre las secuencias es:", distance)
except ValueError as e:
    print(e)
