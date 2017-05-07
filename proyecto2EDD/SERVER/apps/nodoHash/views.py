# -*- coding: utf-8 -*-

from django.shortcuts import render

from django.http import HttpResponse
from django.http import request
import matriz
import Doble
import tablaHash
DOBLE= Doble.Lista()
MATRIZ = matriz.Matriz()
HASH = tablaHash.tabla()

# Create your views here.
def index(request):	
	return HttpResponse(MATRIZ.Insertar('1998','ABRIL','1','usu','contra'))
def insertarEvento(request):
	mes = request.GET.get('mes', 'None')
	ano = request.GET.get('ano', 'None')
	usuario = request.GET.get('usu','None')
	fecha = request.GET.get('fecha','None')
	desc = request.GET.get('desc','None')
	evento = request.GET.get('evento','None')
	direc = request.GET.get('direc','None')
	hora = request.GET.get('hora','None')
	eliminado = 'False'
	DOBLE.InsertarPrimero('usu','contra')
	MATRIZ.Insertar('1998','ABRIL','1','usu','contra')
	MATRIZ.Insertar('1996','MAYO','2','usu2','contra2')
	MATRIZ.insertarEvento('ABRIL','1996','usu','desc','evento','direc','hora','False')
	return HttpResponse("Ingresado")

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
	DOBLE.Listar()
	if verificacion == True:
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
	HASH.modificar('pablo','fecha','a','b','c','False','ab','ab','ab','ab','abc')
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
	
