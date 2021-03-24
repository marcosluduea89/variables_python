#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de práctica
---------------------------
Autor: Ludueña Marcos
Version: 1.5

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Ludueña Marcos"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.5"

def ej1():
    # Ejercicios de práctica numérica
    numero_1 = 5
    numero_2 = 7

    # Realizar la suma de las dos variables
    # numero_1 y numero_2
    # Almacenar el valor de la suma en una variable
    # ej:
    # operacion = .....
    operacion = numero_1 + numero_2
    # Imprimir en pantalla el resultado de la suma
    # print(....)
    print (operacion)

    # Repita el procedimiento para realizar la resta


def ej2():
    # Ejercicios de práctica numérica

    # Ahora los valores a operar deben ser ingresados por
    # consola con la función "input" como se ve a continuación
    print('Ingrese el primer número decimal a operar:')
    numero_1 = int(input())

    print('Ingrese el segundo número decimal a operar:')
    numero_2 = int(input())

    # Alumno: Imprima en pantalla los dos números decimales solicitados
    print(numero_1, numero_2)

    # Alumno: Calcule la suma, resta, división y multiplicación de los números ingresados
    # numero_1, numero_2
    # Imprima en pantalla todos los resultados con el siguiente formato de ejemplo:
    # El resultado de sumar 4 y 2 es 6
    # NOTA: No coloque usted los nùmeros y resultados, use las variables

    # Suma
    suma = numero_1 + numero_2
    print( "el resultado de sumar {} y {} es {} ".format(numero_1 , numero_2, suma))

    # Resta
    resta = numero_1 - numero_2
    print("el resultado de restasr {} y {} es {} ".format(numero_1 , numero_2, resta))
    
    # División
    division = numero_1 / numero_2
    print("el resultado de dividir {} y {} es {} ".format(numero_1 , numero_2, division))

    # Multiplicación
    multiplicaion = numero_1 * numero_2
    print( "el resultado de multiplicar {} y {} es {} ".format(numero_1 , numero_2, multiplicaion))


def ej3():
    # Ejemplos variables de texto

    # Ingrese primero su nombre y luego su apellido
    # Capture ambos datos e imprima su nombre completo
    print('Ingrese su nombre/s:')
    nombre = str(input())

    print('Ingrese su apellido/s:')
    apellido = str(input())

    # Imprima su nombre completo
    print(nombre , apellido)

    # Almacenar su nombre completo en una variable

    nombre_completo = (nombre,apellido)

    # Imprimir la cantidad de letras que posee su nombre completo

    cantidad = (len(nombre)+ len(apellido) )
    print(cantidad)

def ej4():
    # Ejemplos variables de texto

    # Ingrese tres palabras y arme un acrónimo con ellas
    # Si desea puede modificar el código para ingresar más palabras
    print('Ingrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())

    print('Ingrese palabra 3:')
    palabra_3 = str(input())

    # De cada palabra debe tomar la primera letra y armar el acrónimo
    acronimo = (palabra_1[0] + palabra_2[0] + palabra_3[0])
    
    print(acronimo)

    # Ejemplo: Alumbrado, barrido y limpieza --> ABL
    # Imprimir el resultado en pantalla


def ej5():
    # Ejemplos variables de texto

    # Ingrese dos palabras y arme combinaciones con ella
    print('Ingrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())

    # De la primera palabra tome las primeras tres letras, utilice el operador :
    # De la segunda palabra tome las últimas tres letras, utilice el operador :
    # Formar una nueva palabra con los recortes solicitados
    nueva_palabra = (palabra_1[:3]+ palabra_2[-3:])

    # Imprima en pantalla los resultados
    print(nueva_palabra)



if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
