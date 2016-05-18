print 'Tienda NIKE (Articulos)'
print '----------------------------'
print 'Zapatos depotivos= 15.000 bs.f '
print 'Camisa dam = 4.000bs.f '
print 'Camisa cab = 6.000bs.f '
print 'Jeans = 25.000 bs.f '
print 'Morral nike= 13.000bs.f '

print('\n')

producto1 = 15000  
producto2 = 4000
producto3 = 6000  
producto4 = 25000  
producto5 = 1300

 
def FacturaCliente(producto1, producto2, producto3, producto4, producto5):
   productovalor = producto1 + producto2 + producto3 + producto4 + producto5 
   iva = productovalor * 0.12
   total = productovalor + iva
   print 'Total: ' 
   print productovalor
   print 'IVA: ' 
   print iva
   print 'Total a Pagar: '
   print total

FacturaCliente(producto1, producto2, producto3, producto4, producto5)
