#!usr/bin/env python
#-*- coding: utf-8 -*- 

#conding-----------
import os
import time
#operative system
#cls windows
#clear linux, MacOS
def menu():	
	a=True
	while a==True:
		os.system("cls")
		print "---------sistema que permite verificar que tipo de jubilacion posee-----------"
		print "------------Menu--------------"
		print "seleccione una de nuestras opciones"
		print "1. edad mayor a 60 años"
		print "2. menos de 60 años y 20 o más años de trabajo realizado"


	#si ingresa a la opcion invalida que regrese al menu y si esta bien que continue con el procedimiento
	
	
		Noopcion = raw_input("ingrese numero de opcion")
		if Noopcion == "1":
			os.system("cls")
			print "seleccionaste edad mayor a 60 años"
			a=False		
			je()
		elif Noopcion == "2":
			os.system("cls")
			print "seleccionaste menos de 60 años y 20 o más años de trabajo realizado"
			a=False
			jt()
		
				

	


	
def je():
	
	print "tu jubilación es: Jubilación por edad  "
	


def jt():
	
	print "tu jubilación es: Jubilación por tiempo de trabajo "
	
	









menu()
