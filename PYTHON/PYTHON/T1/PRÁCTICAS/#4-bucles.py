
for i in range(5):

    print(f" {i} ")


for i in range(5):

    print(f" {i} ", end=" ")


for i in range(10, 20):

    print(f" {i} ")

# Suma números
suma = 0    #acumulador
limite = 5
for i in range ( limite + 1 ):
    suma = suma + i
print( "\nSuma:", suma )


# while 

while True:

    numero = int(input("Introduce otro numero 0 (para terminar): "))
    if numero==0:
        break
    print("Has introducido:", numero)

print("Fin de programa")

''' 
Suma números

suma = 0 
limite = 5

ini = int (input(“inicio: ”))
fin = int (input(“fin: ”))
for i in range(10,20):
for i in range(ini,fin+1):

	suma=suma + i 
print(“/n Suma:” + suma)

Python Lists
 '''

