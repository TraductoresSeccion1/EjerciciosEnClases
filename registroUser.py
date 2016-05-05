from username import ValidarUsuario
from clave import ValidaClave

username =  raw_input('ingrese nombre de usuario: ')
clave = raw_input('ingrese clave')
if ValidarUsuario(username) == True and ValidaClave(clave) == True:
    print 'Datos correctos'
else:
    print 'Datos incorrectos'
