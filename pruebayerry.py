print 'Productos a comprar'
print '----------------------------'
print 'Sacapuntas = 10 bs.f '
print 'Borrador = 40 bs.f '
print 'Hoja = 5 bs.f '
print 'Porta Minas = 25 bs.f '
print 'Marcador = 200 bs.f '
print 'Cartulina = 50 bs.f '
print 'Papel Bond = 100 bs.f '
print '----------------------------'

articulo1 = 10  
articulo2 = 40  
articulo3 = 5  
articulo4 = 25
articulo5 = 200
articulo6 = 50
articulo7 = 100 
 
def totalizarCompra(item1, item2, item3, item4, item5, item6, item7):
   costoTotal = item1 + item2 + item3 + item4 + item5 + item6 + item7
   iva = costoTotal * 0.12
   total = costoTotal + iva
   print 'Total: ' 
   print costoTotal
   print 'IVA: ' 
   print iva
   print 'Total a Pagar: '
   print total

totalizarCompra(articulo1, articulo2, articulo3, articulo4, articulo5, articulo6, articulo7)
