import os
class Nodo(object):
	
	def __init__(self,id,nombre,descripcion,idActivo):
		self.id = id
		self.nombre = nombre
		self.descripcion = descripcion		
		self.idActivo=idActivo
		self.fe =0 
		self.hijoDerecho = None
		self.hijoIzquierdo = None

	def getNombre(self):
		return self.nombre

class Arbol(object):
	def __init__(self):
		self.raiz = None
		self.length = 0

#--------------------------------------------- Metodo Buscar
	def buscar(self,id,raiz):
		if raiz == None:
			return None
		elif int(raiz.id) == int(id):
			return raiz
		elif int(raiz.id) < int(id) : 
			return self.buscar(id,raiz.hijoDerecho)
		else :
			return self.buscar(id,raiz.hijoIzquierdo)
#--------------------------------------------- Metodo para el Fe
	def obtenerFE(self,nodo):
		if nodo==None:
			return -1
		else:
			return nodo.fe

	def max(num1,num2):
		if num1 > num2:
			return num1
		else:
			return num2
#--------------------------------------------- Rotaciones		
	#--------------------------------------------- Rotacion simple Izquierda
	def rotacionIzquierda(self,nodo):
		aux = nodo.hijoIzquierdo
		nodo.hijoIzquierdo = aux.hijoDerecho
		aux.hijoDerecho = nodo
		nodo.fe = max(self.obtenerFE(nodo.hijoIzquierdo),self.obtenerFE(nodo.hijoDerecho)) + 1;
		aux.fe = max(self.obtenerFE(aux.hijoIzquierdo),self.obtenerFE(aux.hijoDerecho)) + 1;
		return aux

	#--------------------------------------------- Rotacion simple Izquierda
	def rotacionDerecha(self,nodo):
		aux = nodo.hijoDerecho
		nodo.hijoDerecho = aux.hijoIzquierdo
		aux.hijoIzquierdo = nodo
		nodo.fe = max(self.obtenerFE(nodo.hijoIzquierdo),self.obtenerFE(nodo.hijoDerecho)) + 1;
		aux.fe = max(self.obtenerFE(aux.hijoIzquierdo),self.obtenerFE(aux.hijoDerecho)) + 1;
		return aux

	#--------------------------------------------- Rotacion doble a la Izquierda
	def rotacionDobleIzquierda(self,nodo):
		nodo.hijoIzquierdo = rotacionDerecha(nodo.hijoIzquierdo)
		aux = rotacionIzquierda(nodo)
		return aux

	#--------------------------------------------- Rotacion doble a la Dereccha
	def rotacionDobleDerecha(self,nodo):
		nodo.hijoDerecho = rotacionIzquierda(nodo.hijoDerecho)
		aux = rotacionDerecha(nodo)
		return aux
#--------------------------------------------- Insertar
	def insertar(self,nuevo,subarbol):		
		nuevoPadre = subarbol
		if int(nuevo.id) < int(subarbol.id) :
			if subarbol.hijoIzquierdo == None:
				subarbol.hijoIzquierdo = nuevo
			else:
				subarbol.hijoIzquierdo = self.insertar(nuevo,subarbol.hijoIzquierdo)
				if (self.obtenerFE(subarbol.hijoIzquierdo) - self.obtenerFE(subarbol.hijoDerecho)) == 2 :
					if int(nuevo.id) < int(subarbol.hijoIzquierdo.id) :
						nuevoPadre = self.rotacionIzquierda(subarbol)
					else:
						nuevoPadre = self.rotacionDobleIzquierda(subarbol)
		elif int(nuevo.id) > int(subarbol.id) :
			if subarbol.hijoDerecho == None:
				subarbol.hijoDerecho = nuevo
			else:
				subarbol.hijoDerecho =self.insertar(nuevo,subarbol.hijoDerecho)
				if (self.obtenerFE(subarbol.hijoDerecho) - self.obtenerFE(subarbol.hijoIzquierdo)) == 2 :
					if int(nuevo.id) > int(subarbol.hijoDerecho.id):
						nuevoPadre = self.rotacionDerecha(subarbol)
					else:
						nuevoPadre = self.rotacionDobleDerecha(subarbol)
		else:
			print("Nodo duplicado")
		if (subarbol.hijoIzquierdo == None) and (subarbol.hijoDerecho != None):
			subarbol.fe= subarbol.hijoDerecho.fe + 1
		elif (subarbol.hijoIzquierdo != None) and (subarbol.hijoDerecho == None):
			subarbol.fe = subarbol.hijoIzquierdo.fe + 1 
		else:
			subarbol.fe = max(self.obtenerFE(subarbol.hijoIzquierdo),self.obtenerFE(subarbol.hijoDerecho)) +1
		return nuevoPadre

	def insertarNUEVO(self,nombre,descripcion,idActivo):
		nuevo = Nodo(self.length,nombre,descripcion,idActivo)
		if self.raiz == None:
			self.raiz = nuevo
		else:
			self.raiz = self.insertar(nuevo,self.raiz);		
		self.length += 1
#--------------------------------------------- Recorrido
	#Retornar el nodo donde se encuentra el id que se le mando
	def inOrden(self,raiz):
		activos = ""
		if raiz != None:
			activos += self.inOrden(raiz.hijoIzquierdo)
			activos += str(raiz.id)+"[label=\""+raiz.nombre+"\"]"+"\n"
			activos += self.inOrden(raiz.hijoDerecho)
		return activos

	def activosIDS(self,raiz):
		activos = ""
		if raiz != None:
			activos += self.activosIDS(raiz.hijoIzquierdo)
			activos += str(raiz.idActivo)+","
			activos += self.activosIDS(raiz.hijoDerecho)
		return activos

	def punteros(self,raiz):
		activos = ""
		if raiz != None:
			if raiz.hijoIzquierdo!=None:
				activos += str(raiz.id) + "->" + self.punteros(raiz.hijoIzquierdo)
			if raiz.hijoDerecho!=None:
				activos += str(raiz.id) + "->" + self.punteros(raiz.hijoDerecho)
			activos += str(raiz.id) + "\n"
		return activos

	def getActivos(self,raiz):
		activos = ""
		if raiz!=None:
		
			activos += self.getActivos(raiz.hijoIzquierdo)
			activos += str(raiz.nombre) + "|"
			activos += self.getActivos(raiz.hijoDerecho)
		return activos

	def buscarIDactivo(self,palabra,raiz):
		if raiz != None:
			if self.buscarIDactivo(palabra,raiz.hijoIzquierdo) != None:
				return self.buscarIDactivo(palabra,raiz.hijoIzquierdo)
			if raiz.idActivo == palabra:
				return raiz
			if self.buscarIDactivo(palabra,raiz.hijoDerecho) != None:
				return self.buscarIDactivo(palabra,raiz.hijoDerecho)

#---------------------------------------------- Graficar
	def report(self,raiz):
		#avldot = open("avl.dot","w")
		nodos = self.inOrden(raiz)
		punteros = self.punteros(raiz)
		#avldot.write("digraph G { \n" +nodos +"\n" + punteros+"\n }")
		#avldot.close()
		return "digraph G { \n" +nodos +"\n" + punteros+"\n }"
		
		

#arbolAVL = Arbol()
#arbolAVL.insertarNUEVO("a","Esto es la prueba 1","ds")
#arbolAVL.insertarNUEVO("b","Esto es la prueba 2","d")
#arbolAVL.insertarNUEVO("c","Esto es la prueba 3","kdk")
#arbolAVL.insertarNUEVO("d","Esto es la prueba 4","fjfjf")
#arbolAVL.insertarNUEVO("e","Esto es la prueba 5","jdjdjdjd")
#arbolAVL.insertarNUEVO("f","Esto es la prueba 6","jajaja")
#arbolAVL.insertarNUEVO("j","Esto es la prueba 7","jajaja")
#arbolAVL.insertarNUEVO("a","Esto es la prueba 1","ds")
#arbolAVL.insertarNUEVO("b","Esto es la prueba 2","d")
#arbolAVL.insertarNUEVO("c","Esto es la prueba 3","kdk")
#arbolAVL.insertarNUEVO("d","Esto es la prueba 4","fjfjf")
#arbolAVL.insertarNUEVO("e","Esto es la prueba 5","jdjdjdjd")
#arbolAVL.insertarNUEVO("f","Esto es la prueba 6","jajaja")
#arbolAVL.insertarNUEVO("j","Esto es la prueba 7","jajaja")
#arbolAVL.report(arbolAVL.raiz)
#print(arbolAVL.buscarIDactivo("b",arbolAVL.raiz).id)

