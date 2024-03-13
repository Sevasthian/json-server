import json

plantilla = '{"nombre": "miguel" }'
#
plantilla = json.loads(plantilla)

exame = list(

)

#
exame = json.dumps(exame, indent=4)

print(exame)









































# import requests
# empleadoNuevo = {
#     "codigo":10,
#     "nombre": "Sevas",
#     "apellido": "verdugo"
# }
# obtener = requests.get("http://172.16.100.145:55005", data=json.dumps(empleadoNuevo))
# print(obtener.json())

# eliminar = requests.delete("http://172.16.100.145:55005")
# print(eliminar)

#como levantar un servidor json-sever