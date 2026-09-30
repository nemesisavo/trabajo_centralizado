# Las listas se utilizan para almacenar
# varios elementos en una sola variable.

# Los elementos de la lista se ordenan, se pueden cambiar y permiten valores duplicados.
# Los elementos de la lista están indexados, el primer elemento tiene índice [0],
# El segundo elemento tiene índice [1]etc.

# Ordenado, el orden nunca cambia.
# Modificable, podemos hacer lo que agregar,eliminar y cambiar elementos.

ejemplo = ["Pelemento", "Selemento", "Telemento"]
# Imprime lista
print(ejemplo)
# Imprime elemento
print(ejemplo[0])
# Devolver tipo
print(type(ejemplo))

list1 = ["abc", 34, True, 40, "male"]
print(type(ejemplo))

# List() es una función de Python que crea
# una lista a partir de un objeto iterable.

thislist = list(("apple", "banana", "lemon", "orange", "kiwi"))
print(type(thislist))

# Mostrar un rango

print("Rango de lista:",thislist[1:4])

# Generar nueva lista a partir de un rango

nueva_lista = thislist[0:4]
print("Nueva_lista:", nueva_lista)

'''




Colecciones de Python (Arrays)

Hay cuatro tipos de datos de colección en el lenguaje de programación Python:

    La lista es una colección que se ordena y se puede cambiar. Permite miembros duplicados.
    La tupla es una colección que se ordena y no se puede cambiar. Permite miembros duplicados.
    Set es una colección que no está ordenada, Inmutable*, y sin indexar. Sin miembros duplicados.
    El diccionario es una colección que está ordenada** Y cambiable. Sin miembros duplicados.
'''

# Acceso Dato Lista
# o Cadena convertida como tal

'''
print(thislist[0])
print(thislist[1])
print(thislist[2])
print(thislist[3])
print(thislist[4])
'''
# Con Indexación Negativa

'''
print(thislist[-1])
print(thislist[-2])
print(thislist[-3])
print(thislist[-4])
print(thislist[-5])
'''
print(thislist[2:])
print(thislist[3:5])
print(thislist[-3])

# Comprueba si existe
'''
if "apple" in thislist:
    print("Si 'apple', está en esta lista")
'''
# Comprueba si la lista
# tiene elementos

if len(thislist) != 0:
    print("Contiene elementos.")
else:
    print("La lista está vacía.")

print("Longitud lista: ", len(thislist))

# Cambiar elemento

thislist[1] = "blackcurrant"
print(thislist)

thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Métodos Listas

# Insertar elemento
thislist.insert(2, "watermelon")
print(thislist)

# Append: Añadir final elemento

thislist.append("orange")
print(thislist)

# Extend: Añadir elementos
# otra lista, puede agregar
# cualquier elemento iterable
# (tuplas,diccionarios, conjuntos,etc.).

# Remove: Elimina elemento
# por su valor
# Del o 
thislist.remove("watermelon")
print(thislist)

# Pop elimina último elemento 
# sino especifica índice

thislist.pop(4)
print(thislist)

del thislist[0]
print(thislist)

# Clear - vacía lista