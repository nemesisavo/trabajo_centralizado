
# Ejemplo uso format print

nombre = "Alfredo Zumberg"
edad = 23
altura = 1.915

print(nombre, "edad es", edad, "y altura", altura)
# con format
print(f"{nombre} su edad es {edad} y altura {altura:.2f}")

# Algunos métodos de string

'''
saludo = "Hola Mundo"
print("saludo:", saludo)

print("saludo.lower()" ,saludo.lower())
print("saludo:", saludo)
# No modifica cadena original.

#Si queremos modificar - se necesita asignación
saludo = saludo.lower();
print("saludo", saludo)
'''