#Web service -> Conjunto de protocolos y estándares que sirven para intercambair datos entre aplicaciones.

#JSON -> JavaScript Object Notacion (Notacion de Objetos de JavasCript)
#Es un formato de intercambio de datos. Independiente del lenguaje.

import json

json_datos = '{"persona1":{"direccion":"Universidad 128, CDMX","nombre":"Rodrigo","telefono":"56789546"},"persona2":{"direccion":"Colpilco 532, CDMX", "nombre" : "Juan", "Telefono":"12346789"}}'

print(type(json_datos))
#Para convertir JSON a un diccionario
obj = json.loads(json_datos)

print(obj)
print(type(obj))
print("\n\n\n")

#Para convertir de un diccionario a formato JSON
jason_d = json.dumps(obj)
print(jason_d)
print(type(jason_d))
