def distancia_hamming(seq1, seq2):
    if len(seq1) != len(seq2):
        raise ValueError("Las secuencias deben tener la misma longitud.")
    
    cont_hamming = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            cont_hamming += 1
    return cont_hamming

def leer_secuencias_desde_fasta(archivo_fasta):
    with open(archivo_fasta, 'r') as file:
        secuencia1 = ''
        secuencia2 = ''
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                continue  
            if not secuencia1:
                secuencia1 = line
            else:
                secuencia2 = line
                break  
    return secuencia1, secuencia2

archivo_fasta = 'xylefa8416.fasta'
try:
    secuencia1, secuencia2 = leer_secuencias_desde_fasta(archivo_fasta)
    dist = distancia_hamming(secuencia1, secuencia2)
    print("La distancia de Hamming entre las secuencias es:", dist)
except ValueError as error:
    print(error)
except IOError:
    print("Error al leer el archivo.")
