class NodoAVL:
	def __init__(self):
		self.ID=""
		self.nombre=""
		self.descripcion=""
		self.izquierda=None
		self.derecha=None
		self.padre=None
		self.balance=0
		self.rentado=False
class ArbolAVL:
	def __init__(self):
		self.raiz=None
		self.resultado=""
	def insertar(self,ID,nombre,descripcion):
		raiz=self.raiz
		if raiz==None:
			raiz=NodoAVL()
			raiz.ID=ID
			raiz.nombre=nombre
			raiz.descripcion=descripcion
			self.raiz=raiz
		else:
			aux=raiz
			while aux:
				if ID>aux.ID and aux.derecha==None:
					nuevo=NodoAVL()
					nuevo.ID=ID
					nuevo.nombre=nombre
					nuevo.descripcion=descripcion
					aux.derecha=nuevo
					nuevo.padre=aux
					self.balancear(nuevo.padre,1)
					break
				elif ID<aux.ID and aux.izquierda==None:
					nuevo=NodoAVL()
					nuevo.ID=ID
					nuevo.nombre=nombre
					nuevo.descripcion=descripcion
					aux.izquierda=nuevo
					nuevo.padre=aux
					self.balancear(nuevo.padre,-1)
					break
				#ESTE SE PUEDE BORRAR
				elif ID==aux.ID:
					break
				#HASTA ACA
				elif ID>aux.ID:
					aux=aux.derecha
				elif ID<aux.ID:
					aux=aux.izquierda
	def balancear(self,nodo,incremento):
		caso=-1
		while nodo:
			nodo.balance=nodo.balance+incremento
			#print(nodo.balance)
			if nodo.balance==0:
				break
			else:
				caso=self.tipo(nodo)
				if caso==0:
					if nodo.padre!=None:
						
						if nodo.ID<nodo.padre.ID:
							incremento=-1
						else:
							incremento=1
					nodo=nodo.padre
				if caso==1:
					self.izquierdaizquierda(nodo,nodo.derecha)
					break
				if caso==2:
					self.derechaderecha(nodo.derecha,nodo.derecha.izquierda)
					self.izquierdaizquierda(nodo,nodo.derecha)
					break
				if caso==3:
					self.derechaderecha(nodo,nodo.izquierda)
					break
				if caso==4:
					self.izquierdaizquierda(nodo.izquierda,nodo.izquierda.derecha)
					self.derechaderecha(nodo,nodo.izquierda)
					break

	def tipo(self,nodo):
		if nodo.balance==2:
			if nodo.derecha.balance==0 or nodo.derecha.balance==1:
				return 1
			elif nodo.derecha.balance==-1:
				return 2
		elif nodo.balance==-2:
			if nodo.izquierda.balance==0 or nodo.izquierda.balance==-1:
				return 3
			elif nodo.izquierda.balance==1:
				return 4
		return 0
	def izquierdaizquierda(self,nodo,derecha):
		aux=derecha.izquierda
		if nodo==self.raiz:
			self.raiz=derecha
			derecha.padre=None
		else:
			if nodo.ID>nodo.padre.ID:
				nodo.padre.derecha=derecha
			else:
				nodo.padre.izquierda=derecha
			derecha.padre=nodo.padre
		derecha.izquierda=nodo
		nodo.derecha=aux
		nodo.padre=derecha
		if aux!=None:
			aux.padre=nodo
		numero=nodo.balance
		nodo.balance=(numero-1)-max(derecha.balance,0)
		balance2=min(numero-2,numero+derecha.balance-2)
		derecha.balance=min(balance2,derecha.balance-1)
	def derechaderecha(self,nodo,izquierda):
		aux=izquierda.derecha
		if nodo==self.raiz:
			self.raiz=izquierda
			izquierda.padre=None
		else:
			if nodo.ID>nodo.padre.ID:
				nodo.padre.derecha=izquierda
			else:
				nodo.padre.izquierda=izquierda
		izquierda.padre=nodo.padre
		izquierda.derecha=nodo
		nodo.izquierda=aux
		nodo.padre=izquierda
		if aux!=None:
			aux.padre=nodo
		numero=nodo.balance
		nodo.balance=numero+1-min(izquierda.balance,0)
		balance2=min(numero+2,numero-izquierda.balance+2)
		izquierda.balance=max(balance2,izquierda.balance+1)
	def buscar(self,ID):
		if self.raiz!=None:
			actual=self.raiz
			print(ID)
			print(actual.ID)
			while actual:
				if actual.ID==ID:
					print("si")
					return actual
				elif ID<actual:
					print("izquierda")
					actual=actual.izquierda
				elif ID>actual:
					print("drecha")
					actual=actual.derecha
				else:
					actual=None
			return actual
	def eliminar(self,ID):
		if self.raiz!=None:
			self.raiz=None

	def graficar(self):
		self.resultado=""
		if self.raiz!=None:
			self.preorder(self.raiz)
			if self.raiz.derecha==None and self.raiz.izquierda==None:
				self.resultado="\""+str(self.raiz.ID)+"\""
	def activos(self):
		self.resultado=""
		if self.raiz!=None:
			self.preorder2(self.raiz)
		return self.resultado
	def activosDisp(self):
		self.resultado=""
		if self.raiz!=None:
			self.preorder4(self.raiz)
		return self.resultado
	def buscar(self,ID):
		self.resultado=""
		if self.raiz!=None:
			self.preorder3(self.raiz,ID)
		return self.resultado
