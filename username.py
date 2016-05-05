def ValidarUsuario(username):
    if len(username) < 6:
        return 'El nombre de usuario debe contener al menos 6 caracteres'
    elif len(username) > 12:
        return 'El nombre de usuario no puede contener mas de 12 caracteres'
    elif not username.isalnum():
        return  'El nombre de usuario puede contener solo letras y numeros'
    else:
        return True
