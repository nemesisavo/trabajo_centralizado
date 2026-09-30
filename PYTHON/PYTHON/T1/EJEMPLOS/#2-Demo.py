
# Operadores Booleanos

'''
# Evalúa una cadena y número
print(bool("Hello"))
print(bool(15))

# Evalúa dos variables
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# Operadores Aritméticos

+  -> Suma
-  -> Resta
*  -> Producto
/  -> División (devuelve float)
%  -> Módulo
** -> Exponente
// -> Div.entera (devuelve
resultado redondeado, abajo)


x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)


# Operadores Asignación
# Asignan valores a variables

Operador


=	Asigna un valor a una variable.
+=	Suma un valor a la variable y asigna el resultado.
-=	Resta un valor a la variable y asigna el resultado.
*=	Multiplica la variable por un valor y asigna el resultado.
/=	Divide la variable por un valor y asigna el resultado.
//=	Realiza una división entera y asigna el resultado.
%=	Calcula el resto de una división y asigna el resultado.
**=	Eleva la variable a una potencia y asigna el resultado.
&=	Realiza una operación AND bit a bit y asigna el resultado.
`	=`
^=	Realiza una operación XOR bit a bit y asigna el resultado.
<<=	Desplaza los bits hacia la izquierda y asigna el resultado.
>>=	Desplaza los bits hacia la derecha y asigna el resultado.
:=	Asigna un valor dentro de una expresión.


# Operadores Comparación
# comparan dos valores


Igual ==
No Igual !=
> Mayor que
< Menor que
>= Mayor o Igual que
<= Menor o Igual que


# Ejemplo

x = 5

print(x < 5 or x > 10)

x = 5

print(not(x < 5 and x > 10))

# Operadores lógicos
# para combinar declaraciones
# condicionales:

and: Devuelve True
si todas las condiciones son verdaderas.
or:	Devuelve True si al menos
una condición es verdadera.
not: Invierte el valor lógico
de una condición.'''

edad=40

# Uso if(operadores comparacion)
if 10 <= edad <=30:

    print("la persona se encuentra entre 10 y 30 años.")

elif 40 <= edad <=60:

    print("la persona se encuentra entre 40 y 60 años.")

# Bucle FOR (Arrays o Matrices)

for i in range(5):
    print(f" {i} ")
# Repasar claúsula end=" " ?

for i in range(10,20):
    print(f" {i} ")

# Operadores identidad
# is / is not
# comparar los objetos,
# no si son iguales,
# si en realidad son
# el mismo objeto,
# con la misma ubicación
# de memoria:

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)


'''
Operadores Membresía se utilizan para probar si una secuencia se presenta en un objeto:
'''

# Bucle con una lista; Operador In
mesa = ["taza", "lápiz", "estuche"]

if "silla" not in mesa:
    print("La taza se encuentra en la mesa")

else:
    print("la taza puede ser que se haya caído de la mesa")
