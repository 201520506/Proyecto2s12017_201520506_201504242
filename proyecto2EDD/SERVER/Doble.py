import matriz
import B
class Nodo:
	def __init__(self,dato,contra):
		self.siguiente = None
		self.anterior = None
		self.usuario = dato
		self.pas = contra
		self.MATRIZ = matriz.Matriz()
		self.arbol = B.ArbolB()

	def verusuario(self):
		return self.usuario

	def verContra(self):
		return self.pas

class Lista(object):

	def __init__ (self):
		self.cabeza = None
		self.cola = None


	def vacia (self):
		if self.cabeza==None:
			return True
		else:
			return False

	def InsertarPrimero (self,dato,contra):
		temporal = Nodo(dato,contra)
		if self.vacia()==True:
			self.cabeza = temporal
			self.cola = temporal
			#print("Ingreso primer dato a doble")
			return True
		else: 
			temporal.siguiente=self.cabeza
			self.cabeza.anterior=temporal
			self.cabeza=temporal
			#print("Ingreso dato a doble")
			return True
		

	def Listar (self):
		print ("...............")
		temporal=self.cabeza
		var =""
		while temporal != None:
			print(temporal.verusuario()+" "+temporal.verContra())
			var = var + temporal.verusuario()
			temporal=temporal.siguiente	
		return var	

	def login (self,usu,contra):
		temporal=self.cabeza
		while temporal != None:
			if temporal.verContra() == contra and temporal.verusuario() == usu:
				return	True
			temporal=temporal.siguiente	
			

	def listarCola (self):
		print ("...............")
		temporal=self.cola
		while temporal != None:
			temporal=temporal.anterior

	def BorrarPrimero (self):
	
		if self.vacia()==False:
			self.cabeza = self.cabeza.siguiente
			self.cabeza.anterior=None

	def Borrarultimo(self):
		if self.cola.anterior==None:
			self.cabeza=None
			self.cola=None
		else:
			self.cola = self.cola.anterior
			self.cola.siguiente=None

	def buscarUsuario(self,usuario):
		
		auxiliar = self.cabeza
		#print(usuario+"BUSQUEDA"+auxiliar.usuario)
		while auxiliar != None:
			if auxiliar.usuario == usuario:
				#print("retornara"+auxiliar.usuario)
				return auxiliar

			auxiliar = auxiliar.siguiente
		return None												
