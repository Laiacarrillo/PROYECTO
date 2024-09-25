from modulos.modulos import limpiarPantalla, registroGrupos, registroModulos,\
 registroEstudiantes, registroDocentes, registroAsistencia,\
generacionInformes, cambia_contra, consultaInformacion, asignarGruposyModulos
from persistencia.persistencia import cargarGrupos, cargarModulos, cargarEstudiantes, cargarAsistencia, cargarDocentes
from menu.interfazmenu import menu
from modulos.login import login

if login():
    sw = True
    while sw:
        print('''
███╗   ███╗███████╗███╗   ██╗██╗   ██╗
████╗ ████║██╔════╝████╗  ██║██║   ██║
██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝
              ''')
        opc = menu()
        match opc:
            case 'a':
                limpiarPantalla()
                grupos = {}
                archGrupos = 'ACME/json/Grupos.json'
                grupos = cargarGrupos(archGrupos)
                grupos = registroGrupos(grupos)
                limpiarPantalla()
                
            case 'b':
                limpiarPantalla()
                modulos = {}
                archModulos = 'ACME/json/Modulos.json'
                modulos = cargarModulos(archModulos)
                modulos = registroModulos(modulos)
                limpiarPantalla()
                
            case 'c':
                limpiarPantalla()
                estudiantes = {}
                archEstudiantes = 'ACME/json/Estudiantes.json'
                estudiantes = cargarEstudiantes(archEstudiantes)
                estudiantes = registroEstudiantes(estudiantes)
                limpiarPantalla()
                
            case 'd':
                limpiarPantalla()
                docentes = {}
                archDocentes = 'ACME/json/Docentes.json'
                docentes = cargarDocentes(archDocentes)
                docentes = registroDocentes(docentes)
                limpiarPantalla()
            case 'e':
                limpiarPantalla()
                asistencia = {}
                archAsistencia = 'ACME/json/Asistencia.json'
                asistencia = cargarAsistencia(archAsistencia)
                asistencia = registroAsistencia(asistencia)
                limpiarPantalla()
            case 'f':
                estudiantes = {}
                archEstudiantes = 'ACME/json/Estudiantes.json'
                estudiantes = cargarEstudiantes(archEstudiantes)
                modulos = {}
                archModulos = 'ACME/json/Modulos.json'
                modulos = cargarModulos(archModulos)
                grupos = {}
                archGrupos = 'ACME/json/Grupos.json'
                grupos = cargarGrupos(archGrupos)
                docentes = {}
                archDocentes = 'ACME/json/Docentes.json'
                docentes = cargarDocentes(archDocentes)
                limpiarPantalla()
                consultaInformacion(estudiantes, modulos, grupos, docentes)
                limpiarPantalla()
            case 'g':
                modulos = {}
                archModulos = 'ACME/json/Modulos.json'
                modulos = cargarModulos(archModulos)
                estudiantes = {}
                archEstudiantes = 'ACME/json/Estudiantes.json'
                estudiantes = cargarEstudiantes(archEstudiantes)
                asistencia = {}
                archAsistencia = 'ACME/json/Asistencia.json'
                asistencia = cargarAsistencia(archAsistencia)
                limpiarPantalla()
                generacionInformes(asistencia, estudiantes, modulos)
                limpiarPantalla()
            case 'h':
                limpiarPantalla()
                cambia_contra()
                limpiarPantalla()
            case 'i':
                limpiarPantalla()
                print('''
 ██████╗ ██████╗  █████╗  ██████╗██╗ █████╗ ███████╗    ██████╗  ██████╗ ██████╗ 
██╔════╝ ██╔══██╗██╔══██╗██╔════╝██║██╔══██╗██╔════╝    ██╔══██╗██╔═══██╗██╔══██╗
██║  ███╗██████╔╝███████║██║     ██║███████║███████╗    ██████╔╝██║   ██║██████╔╝
██║   ██║██╔══██╗██╔══██║██║     ██║██╔══██║╚════██║    ██╔═══╝ ██║   ██║██╔══██╗
╚██████╔╝██║  ██║██║  ██║╚██████╗██║██║  ██║███████║    ██║     ╚██████╔╝██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝╚═╝  ╚═╝╚══════╝    ╚═╝      ╚═════╝ ╚═╝  ╚═╝
                                                                                 
██╗   ██╗███████╗ █████╗ ██████╗     ███████╗██╗                                 
██║   ██║██╔════╝██╔══██╗██╔══██╗    ██╔════╝██║                                 
██║   ██║███████╗███████║██████╔╝    █████╗  ██║                                 
██║   ██║╚════██║██╔══██║██╔══██╗    ██╔══╝  ██║                                 
╚██████╔╝███████║██║  ██║██║  ██║    ███████╗███████╗                            
 ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚══════╝╚══════╝                            
                                                                                 
██████╗ ██████╗  ██████╗  ██████╗ ██████╗  █████╗ ███╗   ███╗ █████╗ ██╗         
██╔══██╗██╔══██╗██╔═══██╗██╔════╝ ██╔══██╗██╔══██╗████╗ ████║██╔══██╗██║         
██████╔╝██████╔╝██║   ██║██║  ███╗██████╔╝███████║██╔████╔██║███████║██║         
██╔═══╝ ██╔══██╗██║   ██║██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║██╔══██║╚═╝         
██║     ██║  ██║╚██████╔╝╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║██║  ██║██╗         
╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝ 
                      ''')
                sw = False
