# bucle es una estructura de control que permite repetir un bloque de código varias veces

# bucle for (para cada elemento en una secuencia)

fruits = ["manzana", "banana", "cereza", "naranja"]
for fruit in fruits:
    print(f"quiero comprar {fruit}")

for i in range(1,5):
		print(f"iteración {i}")
                

# bucle while (mientras una condición sea verdadera)

count = 0
while count < 20:
    print(f"el numero es {count}")
    count += 1