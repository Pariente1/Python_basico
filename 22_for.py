'''

for element in range(1, 21):
  print(element)



my_list = [23, 45, 67, 89, 43]

for i in my_list:
  print(i)

my_tuple = (11,12,24,22,25)

for i in my_tuple:
  print(i)


product = {
  'name': 'Camisa',
  'precio': 100,
  'stock': 89
}


for i in product:
  print(i, ' tantos ', product[i])

for key, value in product.items():
  print(key, '=', value)

'''

people = [
  {
    'name': 'Nico',
    'age': 34
  },
  {
    'name': 'zule',
    'age': 45
  },
  {
    'name': 'santi',
    'age': 4
  } 
]

for person in people:
  print('name =', person['name'])