class Vehiculo():
    def __init__(self,color,marca,velocidad_maxima):
        self.color = color
        self.marca = marca
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0
        self.encendido = False


#camion y auto heredan de vehiculo las props, entonces no las pongo en cada vehiculo que describo

class Camion(Vehiculo):
    def __init__(self, carga_maxima, color,marca,velocidad_maxima):
        self.carga_maxima = carga_maxima
        self.carga_actual = 0
        Vehiculo.__init__(self,color,marca,velocidad_maxima)
    
    def cargar(self,cantidad):
        self.carga_actual = self.carga_actual+cantidad
    
    def mostrar_velocimetro(self):
        print('La velocidad actual es de  '+str(self.velocidad_actual)+ " de "+str(self.velocidad_maxima)+'y la carga es '+str(self.carga_actual))

#puedo seguir agregando cosas a camion como le puse al autito

class Automovil(Vehiculo):
    def __init__(self,puertas,color,marca,velocidad_maxima):
        self.puertas = puertas
        Vehiculo.__init__(self,color,marca,velocidad_maxima)
        
    def abrir_puertas(self,nro_puertas):
        print('se abrir puertas')


#ver de pasasr esto a Vehiculo

    def encender_auto(self):
        self.encendido = True
        print('auto encendido')

    def apagar_auto(self):
        self.encendido = False
        print('auto apagado')

    def mostrar_velocimetro(self):
        print('La velocidad actual es de  '+str(self.velocidad_actual)+ " de "+str(self.velocidad_maxima))

    def acelerar(self,velocidad):
        if(self.encendido == True):
            if self.velocidad_actual+velocidad > 200:
                self.velocidad_actual = 200
            else:
                self.velocidad_actual = self.velocidad_actual+velocidad
        else:
            print('Para acelerar hay que encender el auto')
        self.mostrar_velocimetro()

    def frenar(self,velocidad):
        if self.velocidad_actual-velocidad < 0:
            self.velocidad_actual = 0
        else:
            self.velocidad_actual = self.velocidad_actual-velocidad
        self.mostrar_velocimetro()


mi_auto = Automovil('verde', 'Peugeot', 200)
print(mi_auto.color)
print(mi_auto.marca)
mi_auto.encender_auto()
mi_auto.acelerar(1000)
mi_auto.frenar(50)
mi_auto.apagar_auto()

mi_camion = Camion('verde', 'Mbenz', 90, 1000)
mi_camion.carga_actual = 500
print(mi_camion.carga_actual)





