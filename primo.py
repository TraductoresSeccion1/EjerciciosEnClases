#ejercicio2: numeros primos
def primos(num):
    if num % 2 == 0:
        return "es primo"
    else:
        return "no es primo"
num = input("ingrese numero")
print primos(num)
