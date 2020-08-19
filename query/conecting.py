#!/usr/bin/python3
"""
import pymysql

# Open database connection
db = pymysql.connect("localhost","root","adminesmerin2","terminal" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database version : %s " % data)

# disconnect from server
db.close()
"""


sql=' select cl.nombre,cl.apellido ,vb.id_bus,cl.cedula from cliente cl inner join viajes_clientes_join vj on  cl.id_cliente = vj.id_cliente inner join viajes_en_bus vb on vb.id_viaje = vj.id_viaje where vb.destino = "pereira" group by cl.cedula limit 10;'
import pymysql
db = pymysql.connect("localhost","root","adminesmerin2","terminal")
cursor = db.cursor()
try :
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        nombre = row[0]
        apellido = row[1]
        id_bus = row[2]
        cedula = row[3]
        print(nombre,apellido,id_bus,cedula)
except:
    print("unable to open :c ")
db.close()
