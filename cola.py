MaxTamC = 10
A = [0] * MaxTamC  # Initialize the queue with space for 10 elements
frente = 0
final = 0
contador = 0

respuesta = input("¿Desea agregar elementos a la cola? (s/n): ").lower()

while respuesta == 's' and contador < MaxTamC:
    if (final + 1) % MaxTamC == frente:
        print("Desbordamiento de la cola")
        exit(1)

    elemento = int(input("Ingrese un elemento para la cola: "))
    A[final] = elemento  # Store the element in the queue
    final = (final + 1) % MaxTamC  # Move final forward

    contador += 1
    print(f"Elemento {contador} agregado a la cola: {elemento}")

    if contador < MaxTamC:
        respuesta = input("¿Desea agregar más elementos a la cola? (s/n): ").lower()

# Validar si la cola está vacía
if frente == final:
    print("La cola está vacía")
    exit(1)

# Obtener el primer elemento de la cola
primerElemento = A[frente]
print(f"El primer elemento de la cola es: {primerElemento}")
frente = (frente + 1) % MaxTamC  # Eliminate the front element by moving frente forward

# Imprimir elementos de la cola en el orden de ingreso
print("Elementos de la cola en el orden de ingreso:")
i = frente
while i != final:
    print(A[i], end=" ")
    i = (i + 1) % MaxTamC
print()  # For a newline after the elements are printed

