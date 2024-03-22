import os
arch= os.path.join(os.getcwd())
arch+="/data/xylefa8416.fasta"
class fasta():
    def __init__(self,nom,length,sec):
        self.nombre=nom
        self.longitud=length
        self.secuencia=sec
    def __str__(self):
        return self.nombre+" len="+str(self.longitud)+"\n"+self.secuencia
with open(arch,"r") as file:
    all=file.read()
    #print(all)
    Fastas=[]
    seccionado=all.split(">")
    num_fastas=len(seccionado)
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

    print(seccionado[127][0:18])
    print(len(Fastas))
    print(Fastas[127].nombre)

