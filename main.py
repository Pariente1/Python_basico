import random

options = ('piedra', 'papel', 'tijera')
rounds = 1
computer_wins = 0
user_wins = 0

while True:

  print('*' * 10)
  print('ROUND', rounds)
  print('*' * 10)

  
  user_option = input('piedra, papel o tijera => ')
  user_option = user_option.lower()
  
  if not user_option in options:
    print('esa opcion no es valida; escoge: piedra, papel o   tijera')
  
  computer_option = random.choice(options)
  
  print(f'La computadora escogió {computer_option} y tu escogiste {user_option}')
  
  if user_option == computer_option:
    print('empate')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('piedra gana a tijera')
      print('Ganaste')
      user_wins += 1
    else:
      print('papel gana a piedra, perdiste')
      computer_wins += 1
  elif user_option == 'papel': 
    if computer_option == 'piedra': 
      print ('ganaste, papel gana a piedra')
      user_wins += 1
    else: 
      print('perdiste')
      computer_wins += 1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('ganaste, tijera gana a papel')
      user_wins += 1
    else: 
      print('perdiste, manco')
      computer_wins += 1

  if computer_wins == 2:
    print('El ganador es COMPUTADORA')
    break

  if user_wins == 2:
    print('GANASTE!!')
    break


  rounds += 1
  print('_' * 10)
  print(f'\nComputadora: {computer_wins} \nUsuario: {user_wins} ')
  print('_' * 10)