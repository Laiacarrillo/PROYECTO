
def menu():
    sw = True
    while sw:
        print('MENÚ')
        print('a. Registro de grupos.')
        print('b. Registro de módulos.')
        print('c. Registro de estudiantes.')
        print('d. Registro de docentes.')
        print('e. Registro de asistencia.')
        print('f. Consultas de información')
        print('g. Generación de informes')
        print('h. Cambio de contraseña.')
        print('i. Salida del sistema.')
        print("Ingrese una opcion: ",end="")
        opciones = ["a","b","c","d","e","f","g","h","i"]
        opc = input().lower()
        if opc in opciones:
            return opc
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")
            input('Presione una tecla para continuar')
