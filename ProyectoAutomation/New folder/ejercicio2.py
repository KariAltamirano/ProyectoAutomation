for i in range(5):
    precio = 0
    nombre = input("Ingrese el nombre del comprador: ")
    apellido = input("Ingrese el apellido del comprador: ")

    marca = input("Ingrese la marca: ")
    if marca == 'Ford':
        precio = precio + 100000
    elif marca == 'Chevrolet':
        precio = precio + 120000
    elif marca == 'Fiat':
        precio = precio + 800000

    puertas = input("Ingrese la cantidad de puertas: ")
    if puertas == '2':
        precio = precio + 50000
    elif puertas == '4':
        precio = precio + 65000
    elif puertas == '5':
        precio = precio + 78000

    color = input('Ingrese color: ')
    if color == 'blanco':
        precio = precio + 10000
    elif color == 'azul':
        precio = precio + 20000
    elif color == 'negro':
        precio = precio + 30000
    print("La persona: "+nombre+" "+apellido+" compro un auto marca "+marca+" de "+puertas+" puertas y color "+color+" con un precio de $"+ str(precio))
          
