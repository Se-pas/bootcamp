#entero = int
#string (cadena de texto) = str
#Listas
[] #lista vacia
lista1 = ["Sebas", 23, "futbol"] #lista con elementos

#Bucles/Loop/Ciclos 
#Imprime cada elemento, recorriendo cada uno
for cualquier_cosa in range(10):
    print(cualquier_cosa + 1)

#Aca voy a imprimir el ultimo elemento, que en este caso yo se que se encuentra
#en la posicion 2 de la lista1
print(lista1[2]) 
lista1.append("Tecnologia")

#Imprimir el ultimo elemento de la lista sirve para los casos en los que se hace append
# o pop, es decir, si se agrega un dato en una lista muy larga o se borra y entonces no
# nos serviria, por ejemplo, llamar al ultimo elemento con su numero de posicion
print(lista1[len(lista1)-1])

print("-------------------")

########## FUNCIONES ############
#def nombre_de_la_funcion(argumento):
    #return 

def suma (num1,num2):
    resultado = num1+num2
    return resultado

#Equivalente a la de arriba
def suma2(num1, num2):
    return num1+num2

print(suma(5,10))
resul = suma(5,8)
print(resul) 

#Crear una funcion resta, que recibe como parametro dos numeros y retorne la resta
#de esos numeros 
#luego llamar a la funcion e imprimir el resultado

#Opcion 1
def resta(num1,num2):
        resultado = num1-num2
        return resultado
print(resta(5,4))

#Opcion 2 con variable
def resta1(num1, num2):
    return num1-num2

resul = resta1(15,6) #meto resta en una variable "resul"
print("hhh",resul) #llamo a la variable para imprimir el resultado

#Crear una funcion saludo2 que reciba como parametro nombre y  edad 
#e imprimir "Hola soy ____ y tengo ____ anhos"
#llamar varias veces a la funcion con distintos valores
#Nota: retornar algo es opcional

#Opcion 1
def saludo2(nombre,edad):
    print("Hola soy",nombre, "y tengo", edad, "anhos")

saludo2("Sebas", 23)
saludo2("Pepe", 23)
saludo2("Carlos", 45)

#Opcion 2 #CORREGIR
#def saludo3(nombre1,edad1)
 #   return "hola soy", nombre, "y tengo", edad, "aos"

#print(saludo3("Sebas", "21"))

#EJERCICIO 1
#Crear una funcion suma_lista que reciba como argumento una 
#lista de numeros y retorne la suma de sus elementos
#Pista: usar for y una variable acumulador

listita = [1,2,3,4,5]
listota = [100, 5, 5]
def suma_lista(listitaa): 
    suma = 0 #
    for i in listitaa: #mismo proceso que el de 
        suma = suma + i 
    return suma
print(suma_lista(listita))

print(suma_lista (listota))

#EJERCICIO 2 Lista al cuadrado
#Crear una funcion que reciba una lista de numero como parametro
#y retorne una lista con los numeros al cuadrado
#lista_cuadrado (listita) ---> []

listita = [1,2,3,4,5] 
def lista_cuadrado(list4): #tip: usar siempre un argumento con nombre unico 
    lista = [] #creo una lista vacia para almacenar los datos en ella, porque debo presentar los cuadrados en una lista
    for i in list4: #para la variable de for en el argumento "list 4" #Esta ejecutando el ciclo list4 del argumento
        cuadrado = i*i #se hace una variable para introducirla en la lista, el cuadrado de un numero es la multiplicacion del numero por si mismo
        lista.append(cuadrado) #append para agregar la variable cuadrado a la lista 
    return lista #retorna la lista con los datos introducidos 
print(lista_cuadrado(listita)) #imprimo a partir de la llamada de mi funcion a la vez llamando a mi lista de numeros que debo multiplicar al cuadrado


#Creo una funcion suma_cuadrado que reciba una lista de numeros y retorne el valor
#de la suma de cada numero al cuadrado
#[1,2,3,4] -----> 1+4+9+16 = 30

lista_numeros = [1,2,3,4]
def suma_cuadrado(lista_n):
    suma=0
    for p in lista_n:
        suma = suma + (p*p)
    return suma

print(suma_cuadrado(lista_numeros)) #imprimo el resultado de la funcion suma_cuadrado

def suma_cuadrado2(lista_n2):
    return suma_lista(lista_cuadrado(lista_numeros))

print(suma_cuadrado2(lista_numeros))
