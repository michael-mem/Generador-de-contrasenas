import random
import string

print("=========================")
print("GENERADOR DE CONTRASEÑAS")
print("=========================\n")

def generar_contrasena():
    caracter = string.ascii_lowercase + string.digits  + string.ascii_uppercase #+ string.punctuation

    contrasena = []

    while (len(contrasena) < 16):
        caracteres=random.choice(caracter)    
        contrasena.append(caracteres)

    contrasena = "".join(contrasena)
    return contrasena

def run():
    contrasena = generar_contrasena()
    print('Tu nueva contraseña es: '+ contrasena)

if __name__ == "__main__":
    run()
