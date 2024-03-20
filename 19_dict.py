my_dict = {}
print(type(my_dict))

my_dict = {
  'avion': 'bla bla bla',
  'name': 'Nicolas',
  'last_name': 'Molina Monroy',
  'age': 87
}

print(my_dict)
print(len(my_dict))

print(my_dict['age']) #aqui puedo preguntar especificamente cual es el valor de la llave
#print(my_dict['asd']) #aqui sale error porque no lo encuentra
print(my_dict.get('age')) #aqui consulta si la llave existe
#De no existir imprimira 'none'
print(my_dict.get('asdasd')) # aqui no sale error gracias al .get



print('avion' in my_dict) # aqui sabemos si existe o no, de existir imprimira True

print('asdasd' in my_dict) # de no existir imprimira false.