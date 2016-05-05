import re

def ValidaPass(contra):
    if len(contra) > 8 and not (' ' in contra):
        if not re.search('[a-z]', contra):
            return 'la contrasena elegida no es segura 1'
        elif  not re.search('[A-Z]', contra):
            return 'la contrasena elegida no es segura 2'
        elif contra.isalnum():
            return 'la contrasena elegida no es segura 3'
        else:
            return True
    else:
        return 'la contrasena elegida no es segura 4'

#contra = raw_input('ingrese clave: ')
#print ValidaPass(contra)
