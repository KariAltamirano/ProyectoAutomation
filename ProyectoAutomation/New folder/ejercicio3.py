def calcular_precio(marcas,puertas,color,ventas):
    marcas = {'ford':100000, 'chevrolet':120000, 'fiat':80000}
    colores = {'blanco':10000, 'azul':20000, 'negro':30000}
    puertas = {2:50000,4:65000,5:78000}
    precio = marcas[marca]+ colores [color]+ puertas[puerta]
    if ventas > 5 and ventas <11:
        precio= precio*0.9
    elif ventas >10 and ventas <51:
        precio = precio *0.85
    elif ventas >10 and ventas <51:
        precio = precio *0.85
    elif ventas >50:
        precio = precio *0.82
    return precio

mas_clientes = 'si'
ventas = []
marcas =['ford', 'chevrolet' , 'fiat']
puertas =[2,4,5]
colores = ['blanco', 'azul' , 'negro']

while mas_clientes == 'si':
    nombre = input('Ingrese nombre: ')
    apellido = input('Ingrese el apellido: ')
    marca= ''
    puerta = 0
    color = ''
    
    while marca not in marcas:
        marca = input('Ingrese la marca: ')
        marca=marca.lower()

    while puerta not in puertas:
        puerta = int(input('ingrese puertas: '))

    while color not in colores:
        color = input('ingrese el color: ')
        color = color.lower()


    #precio = calcular_precio(marca,puerta,color)

    ventas.append({'nombre':nombre, 'apellido':apellido, 'marca':marca, 'puertas':puerta, 'color':color})

    mas_clientes = input('Hay mas clientes?: ')

largo = len(ventas)
for i in ventas:
    precio = calcular_precio(marcas,puertas,color,largo)
#largo es la cant de ventas que voy a tener
          
    print("La persona: "+ i ['nombre']+" "+ i ['apellido']+
          " compro un auto marca "+ i ['marca'] +" de "+ str(i ['puertas'])+" puertas y color "+ i ['color'] +" con un precio de $"+ str(precio)) 

    
    
    
                   



