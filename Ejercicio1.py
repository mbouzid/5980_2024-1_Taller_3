def leer_fasta(archivo):
  secuencias = {}
  with open(archivo, "r") as f:
    for line in f:
      if line.startswith(">"):
        nombre = line.strip()[1:]
        secuencias[nombre] = ""
      else:
        secuencias[nombre] += line.strip()
  return secuencias

secuencias = leer_fasta("xylefa8416.fasta")

#You could print however it's a really long one