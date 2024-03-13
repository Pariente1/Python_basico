name = "Nicolas"
last_name = "Montoya Monroy"
age = 30

#print(name)
#print(last_name )

full_name= name + " " + last_name

#print(full_name)
quote = "I'm Nicolas"
#print(quote)

quote2 = 'She Said "Hello" '
#print(quote2)

# Format 

template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name 
print("V1",template + "\n")

template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
print("V2",template + "\n")

template = f"hola, mi nombre es {name} y mi apellido es {last_name}"
print ("V3", template  + "\n")

template = f"hola, mi nombre es {name} y mi apellido es {last_name} y mi edad es {age} años de edad"
print ("V3", template)