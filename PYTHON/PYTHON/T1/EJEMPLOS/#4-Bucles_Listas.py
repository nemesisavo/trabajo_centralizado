# Recorre lista y lo imprime
thislist = ["apple", "banana", "cherry"]
'''
for x in thislist:
  print(x)

# Accede a cada ele por índice
for i in range(len(thislist)):
  print(thislist[i])
'''
'''
Utilice el len()Función
para determinar la longitud
de la lista, Luego comience
en 0 y haga un bucle a través
de los elementos de la lista
haciendo referencia
a sus índices.
'''

i = 0
while i < len(thislist):
  print(thislist[i])
# Incremento de i
  i = i + 1

# Bucle usando la comprensión
#  de la lista

# List Comprension ofrece la
# sintaxis más corta para
# hacer looping con listas.

[print(x) for x in thislist]
