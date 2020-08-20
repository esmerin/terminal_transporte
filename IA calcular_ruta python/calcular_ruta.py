#ruta terminal busqueda en amplitud

from arbol import Nodo
from ciudades_dic import ciudades_col
import pymysql
#ask if two nodes are valid by the number of tickets intead of if there a route
def valid_ruta_ciudad(actual,destino):
	try :
		sql = 'select ability from tickets_ability where actual = "'+actual+'" and destino="'+destino+'";'
		cursor.execute(sql)
		r = cursor.fetchone()
		if (r[0] == "False"):
			return False
		else:
			if (r[0] == "True"):
				return True
			else:
				print("logic error in the sql table reult query ",r[0],len(r[0]))
				return False
	except:
		print(sql)
		print("unable to open :'v")
		return -1
#ask the database if this route is posble by the moment
def valid_route(ruta):
	resultado = []
	nodo = ruta
	while nodo.get_padre() != None:
		resultado.append(nodo.get_datos())
		nodo = nodo.get_padre()
	resultado.append(estado_inicial)
	resultado.reverse()
	for i in range(0,len(resultado)-1):
		try :
			sql = 'select id_ticket,ability from tickets_ability where actual = "'+ resultado[i]+'" and destino="'+resultado[i+1]+'";'
			cursor.execute(sql)
			r = cursor.fetchone()
			print(resultado[i],resultado[i+1],r[1])
			if (r[1] == "False"):

				return False
		except:
			print(sql,i,len(resultado))
			print("unable to open :'v")
			return -1
	return True

def buscar_solucion_BFS(conexiones, estado_inicial, solucion):
	sql = "select ability from tickets_ability where"
	solucionado = False
	nodos_visitados=[]
	nodos_frontera=[]
	nodoInicial = Nodo(estado_inicial)
	nodos_frontera.append(nodoInicial)
	while (not solucionado) and len(nodos_frontera) !=0 :
		nodo=nodos_frontera[0]

		#extraer nodo y añadirlo a visitados
		nodos_visitados.append(nodos_frontera.pop(0))
		if nodo.get_datos() == solucion:
			# comprobar que cada uno de los nodos si tenga ticketes disponibles n
			#solucion encontrada
			solucionado = True
			return nodo
		else:
			#expandir ciudades hijos (ciudades con coneccion)
			dato_nodo = nodo.get_datos()
			lista_hijos=[]
			for un_hijo in conexiones[dato_nodo]:
				#en alguna parte de este codigo tengo que hacer la comprobacion de si la ruta es valida
				# de no ser valida no dejar que se reprodusca con la funcion
				# and valid_route(nodo)
				#aprovechano que es un bucle for hago la comprobacion y doy un continue si es negativa
				if valid_ruta_ciudad(dato_nodo,un_hijo):
					hijo=Nodo(un_hijo)
				else:
					continue
				lista_hijos.append(hijo)
				if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera) :
					nodos_frontera.append(hijo)
			nodo.set_hijos(lista_hijos)

	#si llego aqui significa que no encontre ruta
	print("ruta no encontrada")
	return -1
if __name__ == "__main__":
	#inicio la base de datos
	db = pymysql.connect("localhost","root","t","terminal" )
	cursor = db.cursor()

	#base de datos inicialisada
	c = ["bogota","medellin","cali","barranquilla","cartagena","cucuta","villavicencio","popayan","buenaventura","manizales","pereira"]
	print("ciudades validas: ")
	for ciudad in c:
		print(ciudad)
	estado_inicial= input("inserte donde esta:")
	solucion = input("inserte para donde va: ")
	nodo_solucion = buscar_solucion_BFS(ciudades_col,estado_inicial,solucion)
	#mostrar resultado
	resultado = []
	nodo=nodo_solucion
	if nodo == -1:
		print("not solution")
	else:
		while nodo.get_padre() != None:
			resultado.append(nodo.get_datos())
			nodo = nodo.get_padre()
		resultado.append(estado_inicial)
		resultado.reverse()
		print(resultado)
#basado en la implementacion de alberto garcia serrano
