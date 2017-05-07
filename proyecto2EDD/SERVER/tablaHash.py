class NodoHash(object):
	"""docstring for ClassName"""
	def __init__(self,nombre,fecha,direc,desc,hora,eliminado):
		#super(NodoHash, self).__init__()
		self.nombre = nombre		
		self.fecha = fecha
		self.direc = direc
		self.desc = desc
		self.hora = hora
		self.eliminado = eliminado

	def getNombre(self):
		return self.nombre

class tabla(object):
	def __init__(self):
		super(tabla, self).__init__()
		#self.table = NodoHash
		self.table=[100]

		for i in range(100):
			self.table.append(None)											

	def returnAscii(self,id,fecha,direc,desc,hora,eliminado):
		salida=0
		#-----------CALCULO DE POSICION DE INSERCION
		datoAscii =''.join(str(ord(c)) for c in id)
		datoAscii= int(datoAscii)*int(datoAscii)
		datoString = str(datoAscii)
		for i in xrange(0,len(datoString)/2):
			salida = str(datoAscii)[i+1] +""+ str(datoAscii)[i+2]
		print("quiere insertar en:"+str(salida))
		#----------MANEJO DE COLISIONES
		contador = 0
		tablaAux = self.table
		if(tablaAux[int(salida)] is not None):
			datos = tablaAux[int(salida)].split(",")
			print (str(tablaAux[int(salida)]))+" ||||"+(str(datos[1])+" ,"+fecha)
		while (tablaAux[int(salida)] is not None) and ((datos[0] != id) or (datos[1]!=fecha) or (datos[2]!=direc) or (datos[3]!=desc) or (datos[4]!=hora)):
			contador = contador +1
			salida = int(salida) + contador
			print("COLISION guarda en:" + str(salida))
		return salida

	def insertar(self,nombre,fecha,direc,desc,hora,eliminado):
		eliminado = 'False'
		var = ""+str(nombre)+","+str(fecha)+","+str(direc)+","+str(desc)+","+str(hora)+","+str(eliminado)	
		self.table[int(self.returnAscii(nombre,fecha,direc,desc,hora,eliminado))]= var
		return var

	def listar(self):
		aux = self.table
		for i in xrange(1,100):
			if(aux[i] != None):				
				print("Indice:"+str(i)+" Dato: "+str(aux[i]))
	
	def eliminar(self,evento,fecha,direc,desc,hora,eliminado):
		aux = self.table
		pos = int(self.returnAscii(evento,fecha,direc,desc,hora,eliminado))
		print("quiere eliminar en: "+str(pos))
		if aux[pos] != None:
			valores = aux[pos].split(",")
			valores[5]="True"
			self.table[pos]=self.hacerString(valores)
			print("Eliminado pos"+str(pos)+" Evento: "+valores[0])
		return "error"

	def hacerString(self,valores):
		cadena=""
		for x in xrange(0,6):
			if x > 0:
				cadena = cadena+"," +valores[x]				
			else:
				cadena = cadena + valores[x]
		return cadena
	def modificar(self,evento,fecha,direc,desc,hora,eliminado,eventoN,fechaN,direcN,descN,horaN):
		aux = self.table
		pos = int(self.returnAscii(evento,fecha,direc,desc,hora,eliminado))
		print("quiere modificar en: "+str(pos))

		if aux[pos] != None:
			valores = aux[pos].split(",")
			if valores[5]!="False":
				return None
			valores[0]=eventoN
			valores[1]=fechaN
			valores[2]=direcN
			valores[3]=descN
			valores[4]=horaN			
			valores[5]="False"
			self.table[pos]= self.hacerString(valores)	
			print("modificacion pelada")