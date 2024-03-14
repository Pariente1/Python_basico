text = 'Ella sabe python'
print(text[0])
print(text[1])
#print(text[99])

#Para saber el tamaño le ponemos
size = len(text)

#para imprimir el último tenemos que ponerle -1 ya que inicia en 0.
print('size => ', size)

#Estas dos son equivalentes:
print(text[size -1 ])
print(text[-1])

# Slicing

print(text[0:5])
print(text[10:16])

# estos dos son equivalentes, si no le enviamos nada python entendera que inicia con 0
print(text[0:10])
print(text[:10])

'''
Para ir desde un punto hasta el final. El final se describe con -1, python el -1 lo entiende  desde la derecha hacia la izquierda, mientras que los numeros positivos se van desde izquierda a  derecha. 
'''
print(text[5:-1])
print(text[5:])

#Si quiero ir desde inicio hasta el fin.
print(text[:])

"""
También tenemos los saltos. 
El último parametro significa cuantos carácteres va a 'saltar' en cada iteracion. 

"""

print(text[10:16:2])

#Aquí sería irse desde el inicio hasta el final y 'saltando' cada 2 elementos.

print(text[::2])