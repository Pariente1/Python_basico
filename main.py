user_option = input('piedra, papel o tijera => ')
user_option = user_option.lower()

computer_option = 'tijera'
print(f'La computadora escogió {computer_option} y tu escogiste {user_option}')

if user_option == computer_option:
  print('empate')
elif user_option == 'piedra':
  if computer_option == 'tijera':
    print('piedra gana a tijera')
    print('Ganaste')
  else:
    print('papel gana a piedra, perdiste')
elif user_option == 'papel': 
  if computer_option == 'piedra': 
    print ('ganaste, papel gana a piedra')
  else: 
    print('perdiste')
elif user_option == 'tijera':
  if computer_option == 'papel':
    print('ganaste, tijera gana a papel')
  else: 
    print('perdiste, manco')