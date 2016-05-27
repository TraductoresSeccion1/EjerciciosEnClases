#realice una funcion para saber si un numero es par o impar:
def parimpar(num):
    if num % 2:
        return "el numero es impar"
    else:
        return "el numero es par"

num = input("ingrese numero: ")

print parimpar(num)
