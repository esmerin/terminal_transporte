"""diccionario = {'nombre' : 'Carlos', 'edad' : 22, 'cursos': ['Python','Django','JavaScript'] }
for key in diccionario:
  print key, ":", diccionario[key]
  destino = ["bogota","medeillin",
            "cali","barranquilla","cartagena","cucuta",
            "villavicencio","popallan","buenaventura"]
"""

ciudades_col = {'bogota':['medellin','cali','cucuta','villavicencio','buenaventura'],
            'medellin':['cartagena','bogota','manizales'],
            'cali':['popayan','pereira','buenaventura','bogota'],
            'barranquilla':['cartagena'],
            'cartagena':['barranquilla','medellin', 'cucuta'],
            'cucuta':['bogota','cartagena'],
            'villavicencio':['bogota'],
            'popayan':['cali'],
            'buenaventura':["cali","pereira","bogota","medellin"],
            'pereira':['cali','buenaventura','manizales'],
            'manizales':['pereira','medellin']
            }
