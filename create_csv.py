#use this file to create the data to make sure everything works correctly
#fuente para las rutas https://www.trendtic.cl/2016/03/activacion-de-la-nueva-ruta-submarina-del-pacifico-de-level-3-mejora-la-conexion-de-colombia-con-las-principales-ciudades-de-las-americas-europa-y-asia/
import csv
import random
from ciudades_dic import ciudades_col
def rand_destino(numero):
	#esto da un destino aleatorio
	n = len(destino)
	numero = numero%n
	ciudad = destino[numero]
	return ciudad
def rand_actual(ciudad):
	#esto recibe un destino y devuelve un lugar actual valido y random
	n = len(ciudades_col[ciudad])
	return ciudades_col[ciudad][random.randint(0,n-1)]

def rand_fecha():
	#fechas aleatorias entre diciembre   y enero
	n1 = random.randint(0,1)
	n2 = random.randint(1,31)
	if n1 == 1:
		n1 = "2019-12"
	else:
		n1 = "2020-01"
	return n1 + "-" + str(n2)
popular_name = [("Luciana","M"),(" Santiago","H"),(" Maria Jose","M"),(" Juan Jose","H"),(" Isabella","M"),(" Salome","M"),(" Antonella","M"),("Jeronimo","H"),(" Emmanuel","H"),("Emiliano","H")]
popular_last_name = ["Rodriguez"," Gomez","Lopez","Gonzalez"," Garcia","Martinez"," Ramirez"," Sanchez"," Hernandez"," Diaz","Perez"]
table =[]
index = 8000
cedula = 1080000001
#genero clientes
for name in popular_name:
	for last_name in popular_last_name:
		table.append([index,name[0],last_name,str(cedula),name[1],random.randint(7,99) ])
		index = index+1
		cedula = cedula +10
with open ("tabla_cliente.csv","w",newline='') as file:
	writer=csv.writer(file)
	writer.writerows(table)
#create viajes_en_bus
index = 1000
destino = ["bogota","medeillin","cali","barranquilla","cartagena","cucuta","villavicencio","popayan","buenaventura","manizales","pereira"]
# random.randinit()
table2 = []
for viaje in range(1,1000):
	table2.append([index,random.randint(1,100),random.randint(1,110),rand_destino(index),rand_actual(rand_destino(index)),rand_fecha(),random.randint(20,30)])
	#             id viaje,id bus             ,id conductor,         destino ,           actual,                          fecha ,          n_pasajeros
	index += 1
with open ("tabla_viaje.csv","w",newline='') as file:
	writer2 = csv.writer(file)
	writer2.writerows(table2)
#leo el numero de pasajeros por viaje y le doy un valor aleatorio se que estos empiezan en el
# 	8000 y terminan en 8109
table3 = []
for viaje in table2:
	pasajeros = viaje[6]
	for i in range(0,pasajeros):
		 table3.append([viaje[0],random.randint(8000,8109)])

with open ("viajes_clientes_join.csv","w",newline = '') as file:
	writer3 = csv.writer(file)
	writer3.writerows(table3)

# tabla de placas de los buses  son 100
table4 = []
for i in range(5,105):
	table4.append([i,random.randint(1111,9999),"2022-12-05",random.randint(0,50),30])
with open ("bus.csv","w",newline = '') as file:
	writer4 = csv.writer(file)
	writer4.writerows(table4)

#after creating all this and uploading it to the sql only remains to add the foregins keys
#now the table that tells if there is or not route have destino, and actual , and bool true or false
table5 = []
index = 1
for D in destino:
	for actual in ciudades_col[D]:
		#set probability in 90% of true, to have tickets if false means there is no tickets
		n = random.randint(0,100)
		if n>90:
			ability = False
		else:
			ability = True
		table5.append([index,actual,D,ability])
		index += 1
with open ("tickets_bol.csv","w",newline ='') as file:
	writer5 = csv.writer(file)
	writer5.writerows(table5)
