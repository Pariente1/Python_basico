person = {
  'name': 'nico',
  'last_name': 'molina',
  'langs': ['python', 'javascript'],
  'age': 44
}

#print(person)

person ['name'] = 'Santi'
person['age'] -= 70
person['langs'].append('rust')
#print(person)

del person['last_name']
person.pop('age')
#print(person)


print(person)

'''
print('items \n' )
print(person.items())

print('keys \n')
print(person.keys())

print('values \n')
print(person.values())
'''