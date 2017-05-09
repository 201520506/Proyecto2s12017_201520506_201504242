# -*- coding: utf-8 -*-

from django.shortcuts import render

from django.http import HttpResponse
from django.http import request
import matriz
import Doble
import tablaHash
import pyqrcode
import sys
import png
import os
import B

DOBLE= Doble.Lista()
MATRIZ = matriz.Matriz()
HASH = tablaHash.tabla()
ARBOLB = B.ArbolB(5)
# Create your views here.
def CrearCarpeta(request):

	return HttpResponse("llego")
def index(request):
	# url = pyqrcode.create('http://uca.edu')
	# url.svg(sys.stdout, scale=1)
	# url.svg('uca.svg', scale=4)
	# number = pyqrcode.create("http://localhost:8080/GoogleCalendar/principal.jsp")
	# number.png('big-number.png')
	#MATRIZ.Insertar('2000','DICIEMBRE','16','pablo','contra')	
	#MATRIZ.Insertar('1998','ENERO','1','usu','contra')	

	ar = request.GET.get('ar','None')
# En primer lugar debemos de abrir el fichero que vamos a leer.
	infile = open('C:\Users\p_ab1\Desktop\Raton.txt','r')
# Mostramos por pantalla lo que leemos desde el fichero
	print('>>> Lectura completa del fichero')
	print(infile.read())
# Cerramos el fichero.
	infile.close()

	#outfile = open('holis.txt', 'w') # Indicamos el valor 'w'.
	#outfile.write('Fusce vitae leo purus, a tempor nisi.\n')
	#outfile.close()

	return HttpResponse("ok")#MATRIZ.Insertar('1996','SEPTIEMBRE','1','usu','contra'))
def crearQR(request):
	datos = request.GET.get('datos','None')
	url = pyqrcode.create('http://uca.edu')
	url.svg(sys.stdout, scale=1)
	url.svg('uca.svg', scale=4)
	number = pyqrcode.create(datos)
	number.png('QRevento.png')
	return HttpResponse("qrGenerado")
def eliminarEvento(request):
	usuario = request.GET.get('usu','None')
	var = DOBLE.buscarUsuario(usuario)
	evento= request.GET.get('evento','None')
	dia = request.GET.get('dia','None')
	mes = request.GET.get('mes', 'None')
	ano = request.GET.get('ano', 'None')
	direc = request.GET.get('direc', 'None')
	desc = request.GET.get('desc', 'None')
	hora = request.GET.get('hora', 'None')
	eli = request.GET.get('eli', 'None')

	#DOBLE.InsertarPrimero('usu','contra')
	#MATRIZ.Insertar('1998','enero','10','usu','contra')
	#var = DOBLE.buscarUsuario('usu')	
	#MATRIZ.insertarEvento('1998','enero',var,'10','desc','evento','direc','hora','False')

	#MATRIZ.eliminarEvento(var,'evento','10','enero','1998','direc','desc','hora','False')
	MATRIZ.eliminarEvento(var,evento,dia,mes,ano,direc,desc,hora,eli)
	
	return HttpResponse(0)
def modificarEvento(request):
	usuario = request.GET.get('usu','None')
	var = DOBLE.buscarUsuario(usuario)
	#antiguos
	Aevento = request.GET.get('Aevento','None')
	Adia = request.GET.get('Adia','None')
	Ames = request.GET.get('Ames', 'None')
	Aano = request.GET.get('Aano', 'None')
	Adirec = request.GET.get('Adirec','None')
	Ahora = request.GET.get('Ahora','None')
	Adesc = request.GET.get('Adesc','None')
	Aestado = request.GET.get('Aestado','None')
	#nuevos
	Nevento = request.GET.get('Nevento','None')
	Nfecha =  request.GET.get('Nfecha','None')
	Ndirec =  request.GET.get('Ndirec','None')
	Ndesc =  request.GET.get('Ndesc','None')
	Nhora =  request.GET.get('Nhora','None')
	#DOBLE.InsertarPrimero('usu','contra')
	#MATRIZ.Insertar('1998','JUNIO','10','usu','contra')
	#MATRIZ.Insertar('1998','enero','10','usu','contra')
	#var = DOBLE.buscarUsuario('usu')	
	#MATRIZ.insertarEvento('1998','enero',var,'10','desc','evento','direc','hora','False')
	MATRIZ.modEvento(var,Aevento,Aano,Ames,Adia,Adirec,Adesc,Ahora,Aestado,Nevento,Nfecha,Ndirec,Ndesc,Nhora)
	return HttpResponse("pelado")

def getNodoEvento(request):
	#,evento,dia,m,a,usuario
	evento = request.GET.get('evento','None')
	dia = request.GET.get('dia','None')
	mes = request.GET.get('mes', 'None')
	ano = request.GET.get('ano', 'None')
	usuario = request.GET.get('usu','None')
	var = DOBLE.buscarUsuario(usuario)
	#DOBLE.InsertarPrimero('pablo','contra')
	#MATRIZ.Insertar('2000','enero','16','pablo','contra')	
	
	#MATRIZ.insertarEvento('2000','enero',var,'16','desc','evento','direc','hora','False')
		
	#print(MATRIZ.obtenerEventos('evento','16','enero','2000',var))
	return HttpResponse(MATRIZ.obtenerEventos(evento,dia,mes,ano,var))

def insertarEvento(request):
	mes = request.GET.get('mes', 'None')
	ano = request.GET.get('ano', 'None')
	usuario = request.GET.get('usu','None')
	fecha = request.GET.get('fecha','None')
	desc = request.GET.get('desc','None')
	evento = request.GET.get('evento','None')
	direc = request.GET.get('direc','None')
	hora = request.GET.get('hora','None')
	contra = request.GET.get('contra','None')
	dia = request.GET.get('dia','None')
	eliminado = 'False'

	#DOBLE.InsertarPrimero('usu','contra')
	#DOBLE.InsertarPrimero('usu2','123')
	MATRIZ.Insertar(ano,mes,dia,usuario,contra)
	#MATRIZ.Insertar('1998','JUNIO','10','usu','contra')
	#MATRIZ.Insertar('1998','ABRIL','1','usu','contra')
	#MATRIZ.Insertar('1996','MAYO','15',usuario,contra)
	var = DOBLE.buscarUsuario(usuario)
	#usuario = DOBLE.buscarUsuario('usu2')
	MATRIZ.insertarEvento(ano,mes,var,dia,desc,evento,direc,hora,eliminado)	
#	MATRIZ.insertarEvento('1996','MAYO',var,'15','desc','evento','direc','hora','False')
	#HASH.listar()
	#MATRIZ.report()
	#DOBLE.Listar()
	return HttpResponse("ok")

def prueba(request):
	
	txt1 = request.GET.get('txt1', 'None')
	dia = request.GET.get('d', 'None')
	mes = request.GET.get('m', 'null')
	ano = request.GET.get('a', 'null')

	MATRIZ.Insertar('1998','ABRIL','c','c','None')
	MATRIZ.Insertar('1998','ABRIL','OTRO','c','b')
	MATRIZ.Insertar('1998','ABRIL','OTRO','c','b')
	MATRIZ.Insertar('1999','ABRIL','h','i','c',)

	return HttpResponse("ENTRO A PRUEBA CON: "+dia+" "+mes+" "+ano)
def login(request):
	usu = request.GET.get('usu','None')
	contra = request.GET.get('contra','None')
	
	verificacion = DOBLE.login(usu,contra)
	if verificacion == True:
		return HttpResponse('SI')
	else:
		return HttpResponse('NO')

def registro(request):
	usu = request.GET.get('usu','None')
	contra = request.GET.get('contra','None')
	
	verificacion = DOBLE.InsertarPrimero(usu,contra)
	
	#DOBLE.buscarUsuario('pablo')
	if verificacion == True:
		DOBLE.Listar()
		return HttpResponse('Correcto')
	else:
		return HttpResponse('InCorrecto')

def tHash(request):
	HASH.insertar('nombre','fecha','dire','des','hora','False')
	HASH.insertar('pablo','fecha','a','b','c','False')
	HASH.insertar('juan','fecha','a','b','c','False')
	HASH.insertar('aaa','fecha','a','b','c','False')
	HASH.insertar('aaa','otraFecha','a','b','c','False')	

	HASH.eliminar('nombre','fecha','dire','des','hora','False')
	HASH.insertar('aaa','fecha2','a','b','c','False')
	HASH.insertar('aaa','otraFecha2','a','b','c','False')
	HASH.eliminar('juan','fecha','a','b','c','False')
	HASH.modificar('nombre','fecha','dire','des','hora','True','ab','ab','ab','ab','abc')
	HASH.listar()
	
	#HASH.listar()
	#print(HASH.eliminar('nombre'))
	#HASH.insertar('aaa','fecha2','a','b','c',False)	
	
	#HASH.listar()
	# a=H.crearHash()
	# H.agregar(a,5)
	# print(H.contiene(a,5))
	return HttpResponse("-------TERMINO-------------")
	#return HttpResponse(HASH.returnAscii('aaa'))
# def index(request):
	# if request.POST:
	# 	txt1 = request.POST['txt1']
	# 	return HttpResponse("todo")
	# if request.method == 'POST':
	# 	return HttpResponse("a")
	# else:
	# 	return	HttpResponse("b")
	
