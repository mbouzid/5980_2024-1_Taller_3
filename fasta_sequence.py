#PUNTO 1
#LAS ESTRUCTURAS DEFINIDAS FUERON UNA CLASE FASTASEQUENCE Y UNA LISTA DE ESTOS OBJETOS
class FastaSequence:
    def __init__(self, header = None, sequence = None):
        self.header = header
        self.sequence = sequence

file = open("fasta.txt", "r")

listaTxt = list()
listaFasta = list()

for line in file.readlines():
    listaTxt.append(line.strip())
file.close()


for c in range(0,len(listaTxt)-1,2):
    listaFasta.append(FastaSequence(listaTxt[c], listaTxt[c+1]))

#PUNTO2:K-MERS
#LA ESTRUCTURA DE DATOS DEFINIDA FUE UNA LISTA DE OBJETOS DE LA CLASE KMERS

class Kmer:
    def __init__(self,cadena, k):
        self.cadena=cadena
        self.k=k

    def descomponer(self):
        lista2 = list()
        subcadena=list()
        for i in range(0, len(self.cadena)): 
            subcadena=self.cadena[i:i+self.k]
            if len(subcadena)==self.k:
                lista2.append(subcadena)
        return lista2

print("Cuando K=7")
kmer1=Kmer(listaFasta[0].sequence,7)
listaKmers1 = kmer1.descomponer()
print(listaKmers1)

print("Cuando K=11")
kmer1=Kmer(listaFasta[1].sequence,11)
listaKmers1 = kmer1.descomponer()
print(listaKmers1)

#Para saber cuantos k-mers se generan es importante primero establecer el k, sin embargo, para una secuencia de longitud S se generan S-(K-1) k-mers
#EJEMPLO: Para una secuencia de longitud 88 con k=7, se generan (88)-((7)-1). Es decir, se generan 82 k-mers
#EJEMPLO: Para una secuencia de longitud 44 con k=11, se generan (44)-((11)-1). Es decir, se generan 34 k-mers

#La complejidad es de O(n*k) para una secuencia |S| dada