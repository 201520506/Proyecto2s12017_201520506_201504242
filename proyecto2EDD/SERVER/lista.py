import os
import avl
import tablaHash
class Nodo(object):
	"""docstring for Nodo"""
	def __init__(self, valor,indice,usuario,password):
		#Valor es igual al nombre para no editar todo
		self.valor=valor
		self.usuario = usuario
		self.password = password
		self.indice=indice
		self.siguiente = None
		self.arbol = avl.Arbol()
		self.tabla = tablaHash.tabla()
	def getValor(self):
		return self.valor

	def getIndice(self):
		return self.indice

	def getSiguiente(self):
		return self.siguiente
	
class Lista(object):
	"""docstring for Lista"""
	def __init__(self):
		self.primero = None
		self.length = 0

	def getLength(self):
		return self.length

	def getPrimero(self):
		return self.primero

	def insertar(self,valor,usuario,password):
		nuevo = Nodo(valor,self.length,usuario,password)
		if self.primero == None:
			self.primero = nuevo
		else:
			auxiliar = self.primero
			while auxiliar != None:
				if auxiliar.siguiente == None:
					break
				auxiliar = auxiliar.siguiente
			auxiliar.siguiente=nuevo
		self.length = self.length + 1

	def buscar(self,valor):
		auxiliar = self.primero
		while auxiliar != None:
			if auxiliar.getValor() == valor:
				return auxiliar
			auxiliar = auxiliar.siguiente
		return None

	def buscarUsuario(self,usuario):
		print(usuario)
		auxiliar = self.primero
		while auxiliar != None:
			print(auxiliar.usuario)
			if auxiliar.usuario == usuario:
				return auxiliar

			auxiliar = auxiliar.siguiente
		return None

	def login(self,usuario,password):
		auxiliar = self.primero
		while auxiliar != None:
			if (str(auxiliar.usuario) == str(usuario)) and (str(auxiliar.password) == str(password)) :
				return auxiliar
			auxiliar = auxiliar.siguiente
		return None

	def eliminar(self,valor):
		print("valor entrante: "+ valor)
		if valor == "0":
			self.primero = self.primero.siguiente
		else:
			auxiliar = self.primero
			while auxiliar != None:
				if auxiliar.siguiente.getIndice() == int(valor):
					auxiliar2 = auxiliar.siguiente
					auxiliar.siguiente = auxiliar2.siguiente
					auxiliar2.siguiente=None
					break
				auxiliar = auxiliar.siguiente
		print("Eliminado valor")

	def report(self):
		coladot = open("lista.dot","w")
		auxiliar = self.getPrimero()
		cadena = "rankdir=LR; \n node [shape=box];\n node [style=filled]; \n node [fillcolor=\"#31CEF0\"];\n node [color=\"#31CEF0\"];\n edge [color=\"#31CEF0\"];"
		apuntadores = ""
		while auxiliar!=None:
			cadena = cadena +"\n"+ str(auxiliar.getIndice()) + "[label=\"" + str(auxiliar.getValor()) + "\"];"
			if auxiliar.getSiguiente() != None:
				apuntadores = apuntadores + "\n" + str(auxiliar.getIndice()) + " -> " +str(auxiliar.getSiguiente().getIndice()) + ";"
			auxiliar = auxiliar.getSiguiente()

		coladot.write("digraph G { \n" + cadena + "\n" + apuntadores + "\n }")
		coladot.close()
		#os.system("lista.bat")

	def reporteActivos(self):
		auxiliar = self.primero
		activos =""
		while auxiliar!=None:
			activos += auxiliar.arbol.getActivos(auxiliar.arbol.raiz)
			auxiliar= auxiliar.getSiguiente()
		return activos

	def users(self):
		auxiliar = self.primero
		usuario =""
		while auxiliar!=None:
			if auxiliar.getSiguiente()!=None:
				usuario+= "\""+auxiliar.usuario+"\"" +","
			else:
				usuario+= "\""+auxiliar.usuario+"\""
			auxiliar= auxiliar.getSiguiente()
		return usuario