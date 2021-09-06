#numero = input("ingrese numero: ")
#print(int(numero)+20)

#def ingresar_numero():
#  numero = input("ingrese numero: ")
# print(int(numero)+20)

def ingresar_numero():
    numero = int(input("ingrese numero: "))
    numero = numero *30
    return numero

#mi_numero = ingresar_numero()
#print(mi_numero) 

#hacer algo con numeros es la funcion, la variable de esa funcion es mi_variable. a la funcion le paso 2 parametros a y b 
def hacer_algo_con_numeros(a,b):
        return a + b
a = 50
b = 80

mi_variable = hacer_algo_con_numeros(a,b)
print(mi_variable)



