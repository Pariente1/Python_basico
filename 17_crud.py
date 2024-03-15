# crud create, read, update & delete

numbers = [1,2,3,4,5] #Create
print(numbers[1]) # read
numbers[-1]=10 # update
print(numbers) # read

numbers.append(700) # inserta al final 
print(numbers)

numbers.insert(0, 'hola')
'''
inserta en la posicion especifica con el primer parametro  y el segundo parametro lo usa
para poder el texto
'''
print(numbers)

numbers.insert(3, 'change')
print(numbers)

#Se pueden combinar listas de esta manera:
tasks = ['todo 1', 'todo 2', 'todo 3']
new_list = numbers + tasks
print(new_list)

print(new_list.index('todo 2')) # Con esto sabemos su posicion
index = new_list.index('todo 2') # creamos una nueva variable que se asigne la posicion
new_list[index] = 'todo changed' # Cambiamos el contenido que esta en index.
print(new_list) #imprimimos

#Remover elementos:

new_list.remove('todo 1') #Esto es para eliminar
print(new_list)

new_list.pop() # Este espara eliminar el ultimo elemento de la lista
print(new_list)

new_list.pop(0) # Si le asignamos un parametro entonces removera el asignado ahi.
print(new_list)

new_list.reverse() # esto es para voltear los elementos de la lista
print(new_list)

numbers_a=[1,4,5,6,3]
numbers_a.sort() # esto es para ordenar de menos a mayor
print(numbers_a)

strings = ['re', 'ab', 'ed']
strings.sort() # tambien sirve para ordenar de la a a la z.
print(strings)

#El .sort no se puede usar cuando los tipos de datos son diferentes en el array.

''' Aqui hay mas:

append(): Añade un ítem al final de la lista.

clear(): Vacía todos los ítems de una lista.

extend(): Une una lista a otra.

count(): Cuenta el número de veces que aparece un ítem.

index(): Devuelve el índice en el que aparece un ítem (error si no aparece).

insert(): Agrega un ítem a la lista en un índice específico.

pop(): Extrae un ítem de la lista y lo borra.

remove(): Borra el primer ítem de la lista cuyo valor concuerde con el que indicamos.

reverse(): Le da la vuelta a la lista actual.

sort(): Ordena automáticamente los ítems de una lista por su valor de menor a mayor.
'''








