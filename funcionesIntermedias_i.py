#1.-Actualizar valores en diccionarios y listas

x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
	{'first_name':  'Michael', 'last_name' : 'Jordan'},
	{'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
	'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
	'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
x[1][0] = 15
print(type(x[1]))
print(x[1][0])

"""
def xChanger(x):
	for el in x:
		for i, n in enumerate(el):
			if n == 10:
				el[i] = 15
	return x

print(xChanger(x))
"""

#Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
estudiantes[0]['last_name']="Bryant"
print(estudiantes)

#En el directorio_deportes, cambia "Messi" por "Andrés".

directorio_deportes['fútbol'][0] ='Andres'
print(directorio_deportes)

#Cambia el valor 20 en z a 30.

z[0]['y'] = 30
print (z)

#2.-Iterar a través de una lista de diccionarios
# Crea una función iterateDictionary(some_list)para que, dada una lista de diccionarios, la función recorra cada diccionarios de la lista e imprima cada llave y el valor asociado.

estudiantes = [
		{'first_name':  'Michael', 'last_name' : 'Jordan'},
		{'first_name' : 'John', 'last_name' : 'Rosales'},
		{'first_name' : 'Mark', 'last_name' : 'Guillen'},
		{'first_name' : 'KB', 'last_name' : 'Tonel'}
	]
def iterateDictionary(data_entrada):
	for iterador in data_entrada:
		for llave, valor in iterador.items():
			print(f"{llave} - {valor}")

iterateDictionary(estudiantes)

def iterateDictionary(data_entrada):
	for iterador in data_entrada:
		valor = list(iterador.items())
		print(valor[0][0]," - ", valor[0][1], ",", valor[1][0]," - ", valor[1][1])

# print(valor[1][0])

iterateDictionary(estudiantes)

# debería devolver: (está bien si cada par clave-valor termina en 2 líneas separadas;
# un bonus para que aparezcan exactamente como se muestra a continuación)
#first_name - Michael, last_name - Jordan
#first_name - John, last_name - Rosales
#first_name - Mark, last_name - Guillen
#first_name - KB, last_name - Tonel


#3.-Obtener valores de una lista de diccionarios
#Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, la función imprima el valor almacenado en esa clave para cada diccionario. Por ejemplo, iterateDictionary2('name', estudiantes) debería generar:

def iterateDictionary2(key_name, some_list):
	for item in some_list:
		print(item[key_name])

iterateDictionary2('first_name', estudiantes)

iterateDictionary2('last_name', estudiantes)

#Iterar a través de un diccionarios con valores de lista
#Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todos listas, imprima el nombre de cada clave junto con el tamaño de su lista, y luego imprima los valores asociados dentro de la lista de cada clave

dojo = {
	'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
	'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
	for item in some_dict:
		print(len(some_dict[item]), item.upper())
		for list in some_dict[item]:
			print(list)

printInfo(dojo)