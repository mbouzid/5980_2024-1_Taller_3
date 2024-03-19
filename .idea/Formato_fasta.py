import os
arch= os.path.join(os.getcwd())
arch+="/data/xylefa8416.fasta"
class fasta():
    def __init__(self,name,lon,sec):
        self.nombre=name
        self.longitud=lon
        self.secuencia=sec

with open(arch,"r") as file:
    all=file.read()
    #print(all)
    Fastas=[]
    seccionado=all.split(">")
    num_fastas=len(seccionado)
    print(seccionado[128])
