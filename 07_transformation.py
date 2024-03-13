"""
name = 'Nicolas'
print(type(name))

name = 12
print(type(name))

name = True
print(type(name))
print('Nicolas' + ' Molina')
print(10 + 20)
#print('Nicolas' + 12) Esto sale error porque son diferentes tipos de datos. 

age = 12
print('Mi edad es ' + str(age)) 
# con esto la estamos convirtiendo a string el valor de age. Por eso en consola sí sale.

print(f'Mi edad es {age}')

age = input('Escribe tu edad => ')
print(type(age))
age = int(age)
age += 10
print(f'Tu edad en 10 años será {age}')

"""      

name = input('escribe tu nombre: ')
print(name)
age = input('escribe tu edad: ')
age = int(age)
print(age)
total= age + 10 


template = f"Hola mi nombre es {name}, tengo {age} y en 10 años tendré {total} años"
print(template)


