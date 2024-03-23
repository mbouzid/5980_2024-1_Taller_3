import os
import time
arch= os.path.join(os.getcwd())
arch+="/data/xylefa8416.fasta"
class fasta():
    def __init__(self,nom,length,sec):
        self.nombre=nom
        self.longitud=length
        self.secuencia=sec
    def __str__(self):
        return self.nombre+" len="+str(self.longitud)+"\n"+self.secuencia
tiempoinicio=time.time()
with open(arch,"r") as file:
    all=file.read()
    Fastas=[]
    seccionado=all.split(">")
    for i in range(1,len(seccionado)):
        Posiciones=[]
        Posiciones.append(seccionado[i].find("T"))
        Posiciones.append(seccionado[i].find("G"))
        Posiciones.append(seccionado[i].find("A"))
        Posiciones.append(seccionado[i].find("C"))
        Posiciones.sort()
        HEAD=seccionado[i][0:Posiciones[0]]
        ID=HEAD[0:9]
        LEN=HEAD[14:]
        SECUENCIA=seccionado[i][Posiciones[0]:]
        nuevaFasta= fasta(ID,LEN,SECUENCIA)
        Fastas.append(nuevaFasta)

        Posiciones.clear()
def DescKmers(tamaño,secuencia):

    Caracteres=[x for x in Fastas[secuencia].secuencia]
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
def Jaccard(secuenciaA,secuenciaB,k):
    A=DescKmers(k,126)
    B=DescKmers(k,127)
    if len(A)>len(B):
        M=len(A)
        n=len(B)
    else:
        M=len(B)
        n=len(A)
    interseccion=0
    for i in range(M):
        for j in range(n):
            if A[i]==B[j]:
                interseccion+=1
    Union=M+n
    IndiceJ=interseccion/Union
    return "El indice de Jaccard entre las dos secuencias es de: "+str(IndiceJ)


def similitudMatriz(secuanciaA,secuenciaB,k):
    tiempoiniciomatriz=time.time()
    A=DescKmers(k,126)
    B=DescKmers(k,127)
    if len(A)>len(B):
        M=len(A)
        n=len(B)
    else:
        M=len(B)
        n=len(A)

    Matriz=[None]*(M*n)
    pos=0
    for i in range(M):
        for j in range(n):
            if A[i]==B[j]:
                interseccion=1
            else:
                interseccion=0
            Matriz[pos]=[A[i],B[j],interseccion]
            pos+=1
    tiempofinmatriz=time.time()
    print("Tiempo desde que inicia la funcion "+ str(tiempofinmatriz-tiempoiniciomatriz))
    return Matriz

mat=similitudMatriz(1,2,11)

tiempofin=time.time()
print("Tiempo desde que inicia todo el programa "+str(tiempofin-tiempoinicio))
