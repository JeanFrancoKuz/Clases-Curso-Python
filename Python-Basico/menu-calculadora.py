# Menu de una calculadora simple
print("\n\t=== Menu-Calculadora ===")
print("\t1. Sumar")
print("\t2. Restar")
print("\t3. Multiplicar")
print("\t4. Dividir")
print("\t5. Salir")
opcion = input("\n\tSeleccione una opción (1-5): ")

if opcion == "1":
  num1 = float(input("Ingresa el primer número: "))
  num2 = float(input("Ingresa el segundo número: "))
  print(f"\tResultado: {num1} + {num2} = {num1 + num2}")
elif opcion == "2":
  num1 = float(input("Ingresa el primer número: "))
  num2 = float(input("Ingresa el segundo número: "))
  print(f"\tResultado: {num1} - {num2} = {num1 - num2}")
elif opcion == "3":
  num1 = float(input("Ingresa el primer número: "))
  num2 = float(input("Ingresa el segundo número: "))
  print(f"\tResultado: {num1} * {num2} = {num1 * num2}")
elif opcion == "4":
  num1 = float(input("Ingresa el primer número: "))
  num2 = float(input("Ingresa el segundo número: "))
  if num2 != 0:
    print(f"\tResultado: {num1} / {num2} = {num1 / num2}")
  else:
    print("\tError: No se puede dividir entre cero.")
elif opcion == "5":
  print("\n\tGracias por usar el programa. ¡Hasta pronto!")
else:
  print("\tOpción inválida. Por favor intenta de nuevo.")
