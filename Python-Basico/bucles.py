#Los bucles son estructuras de control que permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición. En Python, existen dos tipos principales de bucles: `for` y `while`.

#for (para cada elemento en una secuencia)

fruits = ["Manzana", "banana", "naranja", "kiwi"]

for fruit in fruits:
  print(fruit)
  
  
#Recorrer un rango de numeros

for i in range(0,5):
  print(f"Numero: {i}")
  
myList = ["Python", "Java", "C++", "JavaScript", "PHP"]

for language in myList:
  if language == "JavaScript":
    print("JavaScript encontrado, saliendo del bucle.")
    break  # Sale del bucle si encuentra "JavaScript"
  print(f"Lenguaje de programacion: {language}")
  
#Usando continue para saltar un elemento especifico

for language in myList:
  if language == "Java":
    print("Saltando Java.")
    continue  # Salta el resto del bucle para este elemento
  print(f"Lenguaje de programacion: {language}")

#Bucle while (mientras se cumpla una condicion)

count = 0

while count < 5:
  print(f"Contador: {count}")
  count += 1
  

choise = input("Para iniciar escriba iniciar: ") #INICIAR choise = "INICIAR"


while choise.lower() == "iniciar":
  numberOne = int(input("Ingrese un numero: "))
  numberTwo = int(input("Ingrese otro numero: "))
  print(f"La suma de {numberOne} y {numberTwo} es: {numberOne + numberTwo}")
  choise = input("Para continuar escriba 'continuar' o cualquier otra tecla para salir: ") #No
  if choise.lower() == "continuar":
    choise = "iniciar"  # Reinicia el bucle si el usuario escribe "continuar"
#Al terminar el bucle, se imprime un mensaje de despedida.
print("Gracias por usar la calculadora. ¡Hasta luego!")
