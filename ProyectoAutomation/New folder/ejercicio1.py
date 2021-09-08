#sacar promedios
def promedio(matematica,literatura,fisica):
   return(matematica+literatura+fisica)/3

#imprimir datos
def datos_del_alumno(nombre,apellido,prom):
    print("el alumno "+nombre+" "+apellido+" tiene como promedio: "+str(prom))

#aprobacion de alumnos
def estado_de_aprobacion(prom):
    if prom >6:
        print("el alumno aprobó")
        if prom >= 9:
            print("alumno destacado")
    elif prom >= 4:
        print("a recuperatorio")
    else:
        print("insuficiente")

#ingreso de datos
nombre = input("ingrese su nombre: ")
apellido = input("ingrese su apellido: ")
matematica = int(input("ingrese nota de matemáticas: "))
literatura = int(input("ingrese nota de literatuta: "))
fisica = int(input("ingrese nota de física: "))

prom = promedio(matematica,literatura,fisica)
datos_del_alumno(nombre,apellido,prom)
estado_de_aprobacion(prom)





    
