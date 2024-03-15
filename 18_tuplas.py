numbers = (1,2,3,5)
strings = ('nico', 'zuke', 'santi')
print(numbers)
print('0 => ', numbers[-1])
print(type(numbers))

print(strings)
print(type(strings))

# CRUD create, read, update, delete.

#[].append # En una lista tenemos estos metodos. 
# pero las tuplas son inmutables entonces
# no tienen acceso a estos metodos.

#numbers.append(10)
#numbers[1] = 'change'

# anteriormente salio error porque es una tupla y no una lista

# Las tuplas solo pueden leerse mas no pueden hacer nada mas. 

print(strings)
print(strings.index('zuke'))
print(strings.count('nico'))

# las tuplas SI se pueden cambiar sus tipos de datos.

my_list = list(strings) # aqui convertimos la tupla strings a una lista.
print(my_list)
print(type(my_list)) # aqui nos va a imprimir el tipo lista. 

my_list[1]='juli'
print(my_list)

my_tuple = tuple(my_list) #aqui la convertimos en tupla.
print(type(my_tuple))