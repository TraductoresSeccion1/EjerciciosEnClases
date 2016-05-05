'''
    ejemplo de registro de datos personales:
'''

opc='S'
registro=[]

while opc == 'S' or opc == 's':
    cedula=raw_input('ingrese la cedula: ')
    if len(cedula) <> 8:
        cedula=raw_input('debe ingresar una cedula valida (de 8 caracteres): ')

    nombre=raw_input('ingrese nombres: ')
    apellido=raw_input('ingrese apellido: ')
    sexo=raw_input('ingrese el sexo: ')

    registro.append( cedula+' '+nombre+' '+apellido+' '+sexo )
    import pdb
    #pdb.set_trace()
    #print 'la persona registrada es: '+str(cedula)+' '+nombre+' '+apellido+' '+sexo


    opc=raw_input('Desea continuar utilizando el programa (S/N) :')

print registro

