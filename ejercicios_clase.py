#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1
 
Descripcion:
Programa creado para poner a prueba los conocimientos adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

def ej1():
    # Ejercicios de práctica numérica
    
    # Operadores con números decimales
    print('Ingrese el primer número decimal a operar:')
    numero_1 = int(input())

    print('Ingrese el segundo número decimal a operar:')
    numero_2 = int(input())
    
    # Alumno: Imprima en pantalla los dos números decimales solicitados
    print("El primer numero introducido es:", numero_1)
    print("El segudno numero introducido es:", numero_2)

    # Alumno: Calcule la suma, resta, división y multiplicación de los números ingresados
    # numero_1, numero_2
    suma = numero_1 + numero_2
    resta = numero_1 - numero_2
    division = numero_1 / numero_2
    multiplicacion = numero_1 * numero_2
    # Imprima en pantalla todos los resultados con el siguiente formato de ejemplo:
    # El resultado de sumar 4 y 2 es 6

    # Suma
    print("El resultado de sumar \t\t{} y {} es {}".format(numero_1, numero_2, suma))
    # Resta
    print("El resultado de restar \t\t{} y {} es {}".format(numero_1, numero_2, resta))
    # División
    print("El resultado de dividir \t{} y {} es {}".format(numero_1,numero_2, division))
    # Multiplicación
    print("El resultado de multiplicar \t{} y {} es {}".format(numero_1,numero_2, multiplicacion))

def ej2():
    # Ejercicios de práctica numérica

    # Operadores con números reales
    print('Ingrese el primer número real a operar:')
    numero_3 = float(input())

    print('Ingrese el segundo número real a operar:')
    numero_4 = float(input())

    # Alumno: Imprima en pantalla los dos números reales solicitados
    # print(....)
    print("El primer numero introducido es:", numero_3)
    print("El segudno numero introducido es:", numero_4)

    # Alumno: Calcule la suma, resta, división y multiplicación de los números ingresados
    # numero_3, numero_4
    suma = numero_3 + numero_4
    resta = numero_3 - numero_4
    division = numero_3 / numero_4
    multiplicacion = numero_3 * numero_4
    # Imprima en pantalla todos los resultados con el siguiente formato de ejemplo:
    # El resultado de sumar 4 y 2 es 6
    # Suma
    print("El resultado de sumar \t\t{} y {} es {}".format(numero_3, numero_4, suma))
    # Resta
    print("El resultado de restar \t\t{} y {} es {}".format(numero_3, numero_4, resta))
    # División
    print("El resultado de dividir \t{} y {} es {}".format(numero_3,numero_4, division))
    # Multiplicación
    print("El resultado de multiplicar \t{} y {} es {}".format(numero_3,numero_4, multiplicacion))

def ej3():
    # Ejemplos variables de texto

    # Ingrese primero su nombre y luego su apellido
    # Capture ambos datos e imprima su nombre completo
    print('Ingrese su nombre/s:')
    nombre = str(input())

    print('Ingrese su apellido/s:')
    apellido = str(input())

    # Imprima su nombre completo
    # Almacenar su nombre completo en una variable
    # nombre_completo = .....
    nombre_completo = nombre + ' ' + apellido
    print(nombre_completo)
    # Imprimir la cantidad de letras que posee su nombre completo
    print("Mi nombre tiene",str(len(nombre_completo)),"letras")

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
    # Ejemplo: Alumbrado, barrido y limpieza --> ABL
    # Imprimir el resultado en pantalla
    acronimo = palabra_1[0] + palabra_2[0] + palabra_3[0]
    print("El acronimo resultante es:", acronimo)

def ej5():
    # Ejemplos variables de texto

    # Ingrese dos palabras y arme combinaciones con ella
    print('Ingrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())

    # De la primera palabra tome las primeras tres letras, utilice el operador :
    recorte_1 = palabra_1[:3]
    
    # De la segunda palabra tome las últimas tres letras, utilice el operador :
    recorte_2 = palabra_2[-3:]

    
    # Formar una nueva palabra con los recortes solicitados
    nueva_palabra = recorte_1 + recorte_2
    # Imprima en pantalla los resultados
    print("El primer recorte es:\t\t", recorte_1)
    print("El segundo recorte es:\t\t", recorte_2)
    print("La palabra resultante es:\t", nueva_palabra)

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()