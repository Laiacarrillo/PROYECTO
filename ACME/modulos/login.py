from hashlib import sha256
from persistencia.persistencia import guardar_contra,cargar_contra,hash_contra,contra_predefinida
import hashlib
import getpass

contra_predefinida = "SISGESA"
archivo_contra= "contra.txt"

#Inicio de sesión
def login():
    usuario = input("Ingrese su nombre de usuario: ")
    contra = getpass.getpass("Ingrese su contraseña: ")
    if cargar_contra() is None: # Primera vez que se ejecuta el sistema
        if contra == contra_predefinida:
            guardar_contra(contra)
            print("Bienvenido al sistema")
            return True
        else:
            print("Contraseña incorrecta")
            return False
    elif hash_contra(contra) == cargar_contra():
        print("Bienvenido al sistema")
        return True
    else:
        print("Contraseña incorrecta")
        return False