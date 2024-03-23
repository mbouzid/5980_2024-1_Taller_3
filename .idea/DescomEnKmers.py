import os
arch= os.path.join(os.getcwd())
arch+="/data/xylefa8416.fasta"

with open(arch,"r") as file:
    all=file.read()
    seccionado=all.split(">")
def DescKmers(tamaño,secuencia):
    Posiciones=[]
    Posiciones.append(seccionado[secuencia].find("T"))
    Posiciones.append(seccionado[secuencia].find("G"))
    Posiciones.append(seccionado[secuencia].find("A"))
    Posiciones.append(seccionado[secuencia].find("C"))
    Posiciones.sort()
    Descomponido=seccionado[secuencia][Posiciones[0]:]
    Caracteres=[x for x in Descomponido]
    borrar=Caracteres.count('\n')
    for i in range(borrar):
        Caracteres.remove('\n')
    limite=len(Caracteres)-tamaño+1
    ListaKmers=[""]*limite
    for i in range(limite):
        kmer=""
        for j in range(tamaño):
            kmer+=Caracteres[i+j]
        ListaKmers[i]=kmer
    return ListaKmers
a=DescKmers(3,127)
print(a)
b=DescKmers(5,127)
print(b)
