def busqueda_lineal(matriz, elemento):
  """
  Función que realiza una búsqueda lineal en un arreglo bidimensional.

  Parámetros:
    matriz: El arreglo bidimensional en el que se realiza la búsqueda.
    elemento: El elemento que se busca.

  Retorno:
    Una lista con las posiciones (fila, columna) donde se encuentra el elemento buscado.
  """
  posiciones = []
  for i, fila in enumerate(matriz):
    for j, columna in enumerate(fila):
      if columna == elemento:
        posiciones.append((f"Fila {i+1}", f"Columna {j+1}"))
  return posiciones

#Arreglo Bidimensional 3x3
matriz =[
    [81,50,65],
    [9,5,6],
    [8,9,8]
]
elemento = 81

posiciones = busqueda_lineal(matriz, elemento)

if posiciones:
  print(f"El elemento {elemento} se encuentra en las posiciones:", posiciones)
else:
  print(f"El elemento {elemento} no se encuentra en la matriz.")

  #subir