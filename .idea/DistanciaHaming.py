def CalcularDistanciaDeHamming(PrimeraSecuencia,SegundaSecuencia):
    A=[x for x in PrimeraSecuencia.lower()]
    B=[x for x in SegundaSecuencia.lower()]
    if len(A)!= len(B):
        return "Las Secuencias no tienen el mismo tamaño"
    else:
        diferencias=0
        for i in range(len(A)):
            if A[i]!=B[i]:
                diferencias+=1
        return "Los cantidad de caracteres diferentes son: "+str(diferencias)
Uno="ABCDEFGHI"
DOS="Abcedario"
res=CalcularDistanciaDeHamming(Uno,DOS)
print(res)