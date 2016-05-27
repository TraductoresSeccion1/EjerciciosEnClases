#ejercicio3: trabajo con listas
articulos = ['1 cafetera', '2 cocina', '3 microhondas']
precios = [200, 500, 400]
compra = []
res="s"
while res == "s":
    print "Elija los articulos de su preferencia"
    print articulos
    carrito = input('ingrese numero del articulo: ')
    if carrito in range(1, len(articulos)):
        compra.append(carrito)
    else:
        print "debe elegir un articulo de la lista"
    res = raw_input("desea seguir comprando: ")
total = 0
for i in compra:
    if i == 1:
        total = (total +precios[0] * 0.12) + precios[0]
    elif i == 2:
        total = (total +precios[1] * 0.12) + precios[1]
    elif i == 3:
        total = (total +precios[2] * 0.12) + precios[2]
print "Usted compro los siguientes articulos: \n"
for i in compra:
    print articulos[i]
print "El total de su compra es: ", str(total)
