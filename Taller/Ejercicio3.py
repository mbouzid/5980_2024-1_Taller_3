def leer_fasta(archivo):
    secuencias = {}
    with open(archivo, 'r') as file:
        lineas = file.readlines()
        id_actual = None
        secuencia_actual = ''
        for linea in lineas:
            linea = linea.strip()
            if linea.startswith('>'):
                if id_actual:
                    secuencias[id_actual] = secuencia_actual
                id_actual = linea[1:]
                secuencia_actual = ''
            else:
                secuencia_actual += linea
        if id_actual:
            secuencias[id_actual] = secuencia_actual
    return secuencias

def descomponer_kmers(secuencia, k):
    kmers = []
    for i in range(len(secuencia) - k + 1):
        kmers.append(secuencia[i:i+k])
    return kmers

def obtener_cantidad_kmers(secuencia, k):
    return len(secuencia) - k + 1

def complejidad_descomposicion_kmers(secuencia, k):
    return len(secuencia) - k + 1

archivo_fasta = "xylefa8416.fasta"
secuencias = leer_fasta(archivo_fasta)
k = 3

for id_secuencia, secuencia in secuencias.items():
    kmers_secuencia = descomponer_kmers(secuencia, k)
    cantidad_kmers = obtener_cantidad_kmers(secuencia, k)
    complejidad = complejidad_descomposicion_kmers(secuencia, k)
    
    print(f"Secuencia: {id_secuencia}")
    print("K-mers:", kmers_secuencia)
    print("Cantidad de k-mers:", cantidad_kmers)
    print("Complejidad en tiempo de la descomposición en k-mers:", complejidad)
    print()
