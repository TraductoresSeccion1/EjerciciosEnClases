from re import search as busqueda

def ValidaClave(clave):
    if len(clave) < 8:
        return 'la contrasena elegida no es segura 1'
    elif ' ' in clave:
        return 'la contrasena elegida no es segura 5'
    elif not busqueda('[a-z]', clave):
        return 'la contrasena elegida no es segura 2'
    elif not busqueda('[A-Z]', clave):
        return 'la contrasena elegida no es segura 3'
    elif  clave.isalnum():
        return 'la contrasena elegida no es segura 4'
    else:
        return True
