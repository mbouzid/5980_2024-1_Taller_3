def distancia_hamming(secuencia1, secuencia2):
  if len(secuencia1) != len(secuencia2):
    raise ValueError("Las secuencias deben tener la misma longitud")
  distancia = 0
  for i in range(len(secuencia1)):
    if secuencia1[i] != secuencia2[i]:
      distancia += 1
  return distancia
