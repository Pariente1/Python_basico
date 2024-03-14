
if True:
  print('Deberia ejecutarse')

if False:
  print('Este print nunca se ejecuta')

pet = input('que mascota tienes?')

if pet == 'perro':
  print('genial, tienes buen gusto')
elif pet == 'gato':
  print('Tener un gato es lo máximo, pero tener 2 es mejor')
elif pet == 'pez':
  print('que hueva wey')
else:
  print('no tienes mascota')


stock = int(input ('Digita el stock => '))

if stock >= 100 and stock <= 1000:
  print('El stock es correcto')
else: 
  print('El stock es incorrecto')
  


#Par o Impar

numero = int(input('Ingresa un número: '))
result = numero % 2

if (result == 0 ):
  print('El numero es par')
else: 
  print('el numero es impar')
