#Es un bloque aislado de codigo reutilizable


#Estructura palabra reservada def + nombre de mi funcion + parentesis () + dos puntos ":" dentro lo que sea que quiera
#ejecutar

#Defino mi funcion (Declarar)
def saludar():
  print("Hola desde mi funcion")
  
#usar mi funcion (Invocar)
saludar()

#Esto es una variable Global, existe en todo el programa
valOne = 10

def sum():
  #Esto es una variable local, solo existe dentro de la funcion
  valTwo = 3
  print(f"La suma de {valOne} y {valTwo} es: {valOne + valTwo}")
  
sum()

print(valOne)


#Las funciones pueden recibir valores cambiantes, dichos valores se llaman parametros

def rest(num1=1, num2=1):
  print(f"La resta de {num1} y {num2} es: {num1 - num2}")

rest(1,2)
rest(10,5)
rest(100,20)
rest()

#Retorno de valores (es la capacidad de una funcion de devolver un valor al lugar donde fue llamada)
def mult(num1, num2):
  mult = num1 * num2
  return mult


#Se puede solicitar valores al usuario y pasarlos como argumentos a la funcion
numOne = int(input("Ingrese un numero: "))
numTwo = int(input("Ingrese otro numero: "))

sumTwo = mult(numOne, numTwo)

print(f" el resultado que retorna mi funcion mult es: {sumTwo}")

#Funciones lambda, seran funciones pequeñas, anonimas y definidas en una solo linea de codigo

#Declaracion de una funcion lambda
division = lambda num1, num2: num1 / num2

#Uso de la funcion lambda

print(f"La division de {numOne} y {numTwo} es: {division(numOne, numTwo)}")

#Callback, seran funciones que le pasaremos como argumento a otras


#Declaro mi funcion, que recibe una callback
def process(list, callback):
  return [callback(item) for item in list]


#el uso de mi funcion
results = process([1,2,3,4], lambda number: number * 2)

print(f"Los resultados de mi funcion process son: {results}")