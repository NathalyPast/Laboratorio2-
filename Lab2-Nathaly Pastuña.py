#Modulo 
import os
#Modulo matematico
import math

#definir funcion
def menu():
	num1=int()
	
#Menu
while menu:
	print (" ------ SELECCIONAR UNA OPCION --------- ")
	print ("     [1] =  Operacion raiz cuadrada    ")
	print ("     [2] =  Salir de programa          ")
	opcion= input(' ESCOGA UNA OPCION DEL 1 AL 2: ')

    #Si escoge la opcion 1
	if opcion=="1":
		print("    HAZ ESCOGIDO LA OPCION 1.")
		#Ingreso de datos
		num1=float(input("     Ingrese un numero:   "))
		#proceso
		math.sqrt(num1)
		#Salida de resultado
		print("La raiz cuadrada del numero ingeso es: ", math.sqrt(num1))
		print("=======================================================")

    #Si escoge la opcion 2
	elif opcion=="2":
		print("    HAZ ESCOGIDO LA OPCION 2 SALIR  ")
		print("             TEN LINDO DIA          ")
		exit(0)

	#Si no escoge niguna de las opciones 1 al 2
	else:
		print ("")
		input(" HAZ PULSADO UNA OPCION INCORRECTA INTENTALO NUEVAMENTE: ")
	
