#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1
 
Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

def ej1():
    # Ejercicios de práctica con números

    '''
    Realice una calculadora, se ingresará por línea de comando dos números reales
    y se deberá calcular todas las operaciones entre ellos:
    - Suma
    - Resta
    - Multiplicación
    - División
    - Exponente/Potencia
    
    - Para todos los casos se debe imprimir en pantalla el resultado aclarando
      la operación realizada en cada caso y con que números se ha realizado la operación
      ej: La suma entre 4.2 y 6.5 es 10.7

    '''
    print('Ingrese el primer número real a operar:')
    numero_1 = float(input())

    print('Ingrese el segundo número real a operar:')
    numero_2 = float(input())

    print("El primer numero introducido es:", numero_1)
    print("El segudno numero introducido es:", numero_2)

    # Alumno: Calcule la suma, resta, división, multiplicación y potencia de los números ingresados
    # numero_1, numero_2

    suma = numero_1 + numero_2
    resta = numero_1 - numero_2
    division = numero_1 / numero_2
    multiplicacion = numero_1 * numero_2
    potencia = numero_1 ** numero_2

    print("El resultado de sumar \t\t{} y {} es {}".format(numero_1, numero_2, suma))
    print("El resultado de restar \t\t{} y {} es {}".format(numero_1, numero_2, resta))
    print("El resultado de dividir \t{} y {} es {}".format(numero_1,numero_2, division))
    print("El resultado de multiplicar \t{} y {} es {}".format(numero_1,numero_2, multiplicacion))
    print("El resultado de elevar \t\t{} a la {} es {}".format(numero_1, numero_2, potencia)) 

def ej2():

    # Ejercicios de práctica numérica y cadenas
    
    '''
    Realice un programa que consulte por consola:
    - El nombre completo de la persona
    - El DNI de la persona
    - La edad de la persona
    - La altura de la persona

    Finalmente el programa debe imprimir dos líneas de texto por separado
    - En una línea imprimir el nombre completo y el DNI, aclarando de que campo se trata cada uno
            Ej: Nombre Completo: Nombre Apellido , DNI:35205070,
    - En la segunda línea se debe imprimir el nombre completo, edad y altura de la persona
      Nuevamente debe aclarar el campo de cada uno, para el que lo lea entienda de que se
      está hablando.

    '''
    Nombre = str(input("Ingrese su nombre completo:\t\t "))
    DNI = int(input("Ingrese su número de D.N.I:\t\t "))
    Edad = int(input("Ingrese su edad actual:\t\t\t "))
    Altura = float(input("Ingrese su altura actual en metros:\t "))

    print("\nNombre Completo: {} \t D.N.I: {} \t Edad actual: {}rtf".format(Nombre, DNI, Edad))
    print(
      "\nSu nombre completo es: {} \t Su Numero de D.N.I es: {} \t Su Edad actual es: {} \t Su altura actual es: {} mts \n".format(Nombre, DNI, Edad, Altura)
      )

def ej3():
    # Ejercicios de práctica con cadenas

    '''
    Realice un programa que determine cual sería el apellido de una persona
    si se ingresaran los dos nombres completos de sus padres.
    Dicha persona deberá tener los apellidos de ambos padres

    - Primero el programa debe consultar el nombre completo del padre_1
    - Luego el programa debe consultar el nombre completo del padre_2
    - Luego debe consultar el nombre del hijo/a
    - Debe extraer los apellidos de los padres
    - Luego formar el nombre completo del hijo/a utilizando los apellidos de sus padres
      y el nombre ingresado de dicha persona
    - Imprimir en pantalla el resultado

    NOTA: Para extraer el apellido del nombre completo recomendamos usar el método "split"
    Mostraremos un ejemplo:
    
    direccion_completa = 'Monroe 2716'
    calle, altura = direccion_completa.split(' ')

    Les dejo por su cuenta a que busquen un poco más acerca de este método que seguramente
    utilizarán mucho de acá en adelante. Les dejamos un link con algunos ejemplos más:
    https://www.pythonforbeginners.com/dictionary/python-split

    Cualquier duda con el método split pueden consultarla por el campus
        
    '''
    Padre = str(input("Ingrese el nombre de su padre: "))
    Madre = str(input("Ingrese el nombre de su madre: "))
    Hijo = str(input("Ingrese su nombre: "))
    Padre, Apellido_Padre = Padre.split()
    Madre, Apellido_Madre = Madre.split()
    Nombre_Completo = Hijo + ' ' + Apellido_Madre + ' ' + Apellido_Padre
    print(Nombre_Completo)

def ej4():
    # Ejercicios de práctica con cadenas

    '''
    Realice un programa que determine si una persona_2 es pariente de la persona_1
    Para facilitar el ejercicio solo ingresar un nombre y un apellido por persona
    Ingresar dichos datos como Nombre Apellido, es decir, primero el nombre y luego
    el apellido, separado por un espacio.
    - El programa debe consultar primero el nombre completo de la persona_1
    - Luego debe consultar el nombre completo de la persona_2
    - Debe extraer el apellido de la persona_2
    - Luego preguntar si apellido de la persona_2 está contenido en el nombre completo
      de la persona_1
    - En caso de contenerlo, son parientes
    - Imprimir en pantalla el resultado

    NOTA: Para extraer el apellido del nombre recomendamos usar el método "split"
    Mostraremos un ejemplo:

    direccion_completa = 'Monroe 2716'
    calle, altura = direccion_completa.split(' ')

    Les dejo por su cuenta a que busquen un poco más acerca de este método que seguramente
    utilizarán mucho de acá en adelante. Les dejamos un link con algunos ejemplos más:
    https://www.pythonforbeginners.com/dictionary/python-split

    Cualquier duda con el método split pueden consultarla por el campus
    
        
    '''
    Persona_1 = str(input("Ingrese su nombre completo: "))
    Persona_2 = str(input("Ingrese el nombre completo de alguna persona: "))
    Persona_2, Apellido_Persona_2 = Persona_2.split()
    if Apellido_Persona_2 in Persona_1:
      print("Ambas personas son parientes")
    else:
      print("Estas personas no son parientes")

def ej5():
    # Ejercicios de práctica con cadenas
       
    '''
    Realice un programa que reciba por consola su nombre completo
    e imprima en pantalla su nombre en los siguientes formatos:
    - Todas las letras en minúsculas
    - Todas las letras en mayúsculas
    - Solo la primera letra del nombre en mayúscula

    NOTA: Para realizar este ejercicio deberá usar los siguientes métodos
    de strings:
    - lower
    - upper
    - capitalize

    Puede buscar en internet como usar en Python estos métodos.
    Les dejamos un el siguiente link que posee casos de uso de algunos de ellos:

    Link de referencia:
    https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/

    Cualquier duda con estos métodos pueden consultarla por el campus
    

    '''
    Nombre = str(input("Ingrese un nombre: "))
    print(Nombre.lower())
    print(Nombre.upper())
    print(Nombre.capitalize())


if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()