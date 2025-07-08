import calculadora as cal

from helpers import herramientas

print("iniciando el modulo principal")

sum = cal.sum(10, 5)

rest = cal.rest(10, 5)

print(f"La suma es: {sum}")

print(f"La resta es: {rest}")


hello = herramientas.hello("Jean")

goodbye = herramientas.goodbye("Jean")

circle_area = herramientas.obtain_circle_area(10)
