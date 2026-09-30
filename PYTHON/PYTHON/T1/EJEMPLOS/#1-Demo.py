
# Comentarios línea (#) y en bloque(''' ''')

# Comments can be used to explain Python code.

'''

Comments can be used to make the code more readable.

Comments can be used to prevent execution when testing code.



# Ingresar por pantalla (Mensaje o Cadena de Caracteres) - Input

mensaje = input("Ingresa un mensaje: ");


# Imprime por pantalla mensaje - Print

print("Hola Mundo");
#print("Estoy aprendiendo Python");

# Imprime un Numero


print(1);

# Imprime la Suma de Numeros
print("La suma es: ", 120+280);
print("La resta es: ", 30-20);
print("El producto es: ", 7*14);
print("La división es: ", 450/16);


# Imprimir varios tipos de datos

print("Me gusta un cuaderno verde", 35, 11.1)
'''

# Variables (es una relación de asignar un valor a un objeto)

numero = 5;
nombre = "John";
cadena = "Es una variable contiene una cadena";

# Un Valor para múltiples variables

pvar = svar = tvar = "valor"

print(pvar)
print(svar)
print(tvar)
'''

# Revisar Salto Línea ?
print("\n",numero,"\n",nombre,"\n",cadena);


# Tipos Básicos

# Casting - Modificar Tipos Datos Variables
# Cadena, Entero, Decimal, Booleano o Lógico 
c = str(3);
e = 5;
d = float(90);
b = True;

print(c,e,d,b);

# Imprime cada tipo de dato según variable

print (type(c));
print (type(e));
print (type(d));
print (type(b));

# Se puede concatenar la salida de variables de distinto tipo

# Cadena con Booleano
print (c,b);
# Entero con Decimal
print (e,d);


# Variables Globales - No se ve todavía

 
# Cadenas(Strings) y Métodos

PVariable = "Primer Mensaje";
SVariable = "Segundo Mensaje";

# 1 Opción - Imprimir Valores en una misma línea de Variables
print(PVariable, SVariable);

# 2 Opción - Concatenar esos Valores de las Variables
print(PVariable + SVariable);

# Imprimir Longitud Cadena (Aplica Print)

print(len(PVariable+SVariable))

NMensaje = "Mensaje de Prueba";
print(len(NMensaje));

# Indexación (Elegir un carácter de la cadena)

print(NMensaje[1]);

print(NMensaje[1:3]);

print(NMensaje[6:10]);

print(NMensaje[:3]);

print(NMensaje[11:]);

# Indexación Negativa; Operador - ?

print(NMensaje[-5:-10]);

# Modificar Cadenas

pstr = "Cadena prueba"

# Mayúscula o Minúscula
print(pstr.upper())
print(pstr.lower())


# Reemplaza espacio por guión bajo
print(pstr.replace(" ", "_"))

# Split divide en subcadenas encontrando
# instancias del separador

print(pstr.split(" "));

h = "Ejemplo";
m = "Concatenar";
t = h + " " + m + "."

print(t)



# F(Formatear) - preferido para cadenas 

edad = 36;
txt = f"Mi nombre es John, y tengo {edad}";
print(txt);


precio = 300;
txt1 = f"El precio del producto es {precio:.2f} euros";
print(txt1);

'''

# Desempaquetar una colección, Python extrae valores en variables

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)






