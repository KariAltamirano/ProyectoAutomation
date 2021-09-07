#LISTAS
autos = ['Ford','Chevrolet','Fiat']
print (autos)
print (autos[2])
print (autos[-1])

#agrego al final de la lista
autos.append('Dodge')
print(autos)

#agrego en la posicion 1
autos.insert(1,'Ferrari')
print(autos)

#elimino un elemento
del autos[2]
print(autos)

#largo de la lista
print(len(autos))

#modifico un item de la lista
autos[2] = 'Porsche'
print(autos)

if autos[2] == 'Porsche':
    print('Juancarlo')
else:
    print('chupapi')

#LAS TUPLAS- para losdatos q van y no vamos a modificarlos
colores = ('amarillo', 'azul', 'verde')
print(colores)

#buscar valores
print('amarillo' in colores)

if 'amarillo' in colores:
    print('haaalaaa')
else:
    print('chaooooo')
    
#DICCIONARIOS
usuario = {'id':1, 'name': 'Chuno', 'age':5, 'casado': True}
print(usuario['name'])

usuario['name'] = 'Rita'
print(usuario)

usuario['apellido'] = 'Taver'
print(usuario)

del usuario['apellido']
print(usuario)

print(usuario.keys())
print(usuario.values())

if 'id' in usuario:
    print('Tiene id')

usuario.clear()
print(usuario)


    













