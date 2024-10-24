#FUNCIONES MENU PRINCIPAL
import os
import json
from colorama import init, Fore, Back, Style


def intro():

    init(autoreset=True)

    texto = f"""
    {Fore.BLUE}    ___    ____  ____     _________________   __________________
    {Fore.BLUE}   /   |  / __ \/ __ \   / ____/  _/_  __/ | / / ____/ ___/ ___/
    {Fore.BLUE}  / /| | / /_/ / /_/ /  / /_   / /  / / /  |/ / __/  \__ \\__ \ 
    {Fore.BLUE} / ___ |/ ____/ ____/  / __/ _/ /  / / / /|  / /___ ___/ /__/ / 
    {Fore.BLUE}/_/  |_/_/   /_/      /_/   /___/ /_/ /_/ |_/_____//____/____/  
                                                            
    """

    # Imprime el texto
    print(texto)
    input()

def menu_principal():
    repetir = True
    while repetir:
        os.system("cls")

        
        print("\033[0;36m")
        print("\033[4;15HBienvenidos a la App Fitness")
        print("\033[5;15HProgramacion I")
        print("\033[0;37m")
        
        print("1. Equipo")
        print("2. Instrucciones del programa")
        print("3. Ejecutar")
        print("4. Salir")
        #print("{0:4}{1:4}{3:4}{4:4}".format(a, b, c, d))

        try:
            
            op= int(input("Ingrese un valor del menu: "))
            
            if op==1:
                mostrar_equipo()
                input()
            elif op==2:
                mostrar_inst()
                input()
            elif op==3:
                ejecutar()
                input()
            elif op==4:
                print("El programa ha finalizado.")
                repetir= False
            else:
                print("error")
        except:
            print("Error")
            input()


def mostrar_equipo():
    os.system('cls')
    print("")
    print("Bienvenido! Esta App fue creada por el equipo de:")
    print("")
    print("Lucila Invernizzi, LU: 1201347")
    print("Juan Ignacio Fernández Noceda, LU: ")
    print("Mateo Castellanos, LU:")
    print("Matías Scoccia, LU: ")
    print("")
    print("Somos estudiantes de la materia Programacion I, de la carrera Ingeniería Informática en UADE.")
    print("")

def mostrar_inst():
    os.system('cls')
    print("""Este programa te permitira encontrar el mejor plan de alimentacion y entrenamiento.""")
    print("")
    print("Con la carga de datos personales del usuario, sera evaluada la mejor ruta para alcanzar sus metas.")
    print("Un nuevo estilo de vida saludable esta ahora en tus manos! Para utilizar el programa, solo debes seguir las siguientes instrucciones: ")
    print("")
    print("""1. Registro e Ingreso de datos personales. Deberas crear una cuenta con tu nombre de usuario y contrasena. Luego se solictara que ingreses datos personales como tu altura, peso, edad, genero y nivel de actividad fisica""")
    print("")
    print("2. Determinar tus objetivos. ")
    print("Determinar tus objetivos nutricionales, como bajar de peso o ganar masa mucualar.")
    print("")
    print("3. Recibir tu plan de alimentacion y entrenamiento personalizado.")
    print("El programa ")
    print("")
    print("""4. Comenzar tu plan!. La constancia y disciplina son elementos clave para que tus objetivos se vuelvan realidad. Podras visualizar los pasos que debes seguir en nuestra ventana de calendario. """)
    print("")
    print("5. !")
    print("Dentro de la App podras encontrar un inventario digital de tu propio hogar que nos permitira crear recetas en base a los alimentos con los que cuentas. ")


def ejecutar():
    os.system('cls')
    ingresar_cuenta()
    #definir_calorias()
    #inventario()
    #calendario()

#FUNCIONES LOGIN

def ingresar_cuenta():
    menu= True
    while menu:
        os.system('cls')
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")

        opcion = int(input("Seleccione una opción del menu: "))

        if opcion == 1:
            crear_usuario()
            input()
        elif opcion == 2:
            iniciar_sesion()
            input()
        elif opcion == 3:
            menu_principal()
            input()
        else:
            print("Opción no válida. Inténtelo de nuevo.")
            opcion = input("Seleccione una opción del menu: ")

        
def verificar_datos(nombre_usu):
    try:
        contenido = open("Base_de_datos/usuarios.json", "r")
        lineas = contenido.read()
        contenido.close()

        datos_usu = json.loads(lineas)
    except:
        print("error")

    for usuario in datos_usu('usuarios', []):
        if usuario['nombre'] == nombre_usu:
            usuario_existente= True 
        else:
            usuario_existente= False
    return usuario_existente, datos_usu

def crear_usuario():
    print("Registro de nuevo usuario")
    nombre = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
        
    usuario, datos_de_usuario= verificar_datos(nombre)


    while usuario:
        print("El nombre de usuario ya existe. Intente con otro nombre de usuario(1) o inicie sesion(2).")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            nombre = input("Ingrese su nombre de usuario: ")
            contraseña = input("Ingrese su contraseña: ")
            usuario, datos_de_usuario= verificar_datos(nombre)
        elif opcion == 2:
            iniciar_sesion()
            return #para salir de la funcion una vez que se inicia sesion
        else:
            print("error")

    #si el usuario no existe, se procede a crear uno nuevo
    nuevo_usuario = {'nombre': nombre, 'contraseña': contraseña}
    datos_de_usuario['usuarios'].append(nuevo_usuario)

    #guardar nuevo usuario en JSON
    with open('usuarios.json', 'w') as f:
        json.dump(datos_de_usuario, f, indent=4)
    
    print("¡Usuario registrado con éxito!")
    


def iniciar_sesion():
    print("Inicio de sesión")
    nombre = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    try:
        with open('usuarios.json', 'r') as f:
            datos_de_usuario = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No hay usuarios registrados o el archivo está corrupto.")
        return False

    for usuario in datos_de_usuario.get('usuarios', []):
        if usuario['nombre'] == nombre and usuario['contraseña'] == contraseña:
            print("Bienvenido", nombre, "nuevamente")
            return True

    print("Nombre de usuario o contraseña incorrectos.")
    registrarse = input("¿Desea registrarse? (s/n): ")
    if registrarse.lower() == 's':
        crear_usuario()
    return False


'''
#FUNCION MENU SECUNDARIO

def menu_secundario():
    repetir = True
    while repetir:
        
        print("1. Información personal")
        print("2. Calendario")
        print("3. Inventario")
        print("4. Cerrar sesion")

        try:
            op= int(input("Ingrese un valor del menu."))

            if op==1:
                cargar_info_personal()
            elif op==2:
                #sugerir_rutinas()
                pass
            elif op==3:
                #inventario() 
                pass  
            elif op==4:
                print("Cerrando sesion.")
                repetir= False
            else:
                print("Error")
        except:
            print("Error")
            input()
    
    menu_principal()


#FUNCIONES INGRESO DATOS
def cargar_info_personal():
    nombre = input("Ingrese su nombre: ")
    print("Hola", nombre, "!")
    print("Necesitamos que cargues los siguientes datos para calcular tu metabolismo basal.")

    edad = input("Ingrese su edad: ")

    altura= int(input("Por favor, ingrese su altura en cm: "))

    peso = int(input("Ingrese su peso en KG: "))

    edad = int(input("Ingrese su edad: "))


    sexo= True
    while sexo:
        sexo = input("¿Cuál es su sexo? (H/M): ")
        if sexo.upper() == "H":
            sexo= "H"
        elif sexo.upper() == "M":
            sexo= "M"
        else:
            print("Sexo no válido. Por favor, ingrese H o M.")
            sexo = input("¿Cuál es su sexo? (H/M): ")

    return altura, peso, edad, sexo, nombre


def calcular_metabolismo_basal(sexo, altura, peso, edad):
    if sexo == "H":
        return (10 * peso) + (6.25 * altura) - (5 * edad) + 5
    elif sexo == "M":
        return (10 * peso) + (6.25 * altura) - (5 * edad) - 161



def definir_calorias():
    nombre_usu= "hola"

    usuario_existente=verificar_datos(nombre_usu)

    if usuario_existente:
        print("Bienvenido", "!")
        #si ya esta registrados mostrar datos en pantalla y dar la opcion de actualizarlos
    else:
    #si es usuario nuevo:
        altura_usuario, peso_usuario, edad_usuario, sexo_usuario = cargar_info_personal()
        calculo_calorias = calcular_metabolismo_basal(altura_usuario, peso_usuario, edad_usuario, sexo_usuario)
        objetivo_usuario= definir_objetivo()
    #cargar datos en el archivo json usuarios
        print("El numero de calorias que debe ingerir por dia son:", calculo_calorias, "kcal")
        print("Ahora que conocemos su metabolismo basal y su objetivo... Podemos comenzar a formular su plan!")

    return calculo_calorias, objetivo_usuario


def definir_objetivo() :
    print("¿Cual es tu objetivo? ")
    print("1. Volumen")
    print("2. Bajar de peso")
    print("3. Definicion")
    print("4. No tengo un objetivo definido")
    
    try:
        objetivo = int(input("Seleccione del menu"))
        if objetivo ==1:
            print (texto_volumen)
        elif objetivo == 2:
            print(texto_dieta)  
        elif objetivo== 3:
            print(texto_definicion)
        elif objetivo==4:
            print("No hay problema, solo sigue comiendo saludable y haciendo ejercicio.")
        else: 
            print("El valor ingresado es inválido, por favor intentelo de nuevo")
            objetivo = int(input("Seleccione del menu"))
    except: 
        print("Error")
        input()    
    return objetivo



# FUNCIONES CALENDARIO

def ingresar_objetivo():
            
    print("1. Ganar musculo.")
    print("2. Perder grasa")
    print("3. Ambas")
    print("4. No tengo un objetivo definido.")

    objetivo= int(input("Ingrese su numero de objetivo: "))
    return objetivo

def ingresar_dias_entrenamiento():
   dias = int(input("Ingrese cuantos dias desea entrenar por semana: "))
   while dias<1 or dias>7:
       print("Error. La cantidad de dias no es valida")
       dias = int(input("Ingrese cuantos dias desea entrenar por semana: "))           
           
   return dias

#Funcion rutinas

def mostrar_calendario():

    init(autoreset=True)

    texto = f"""
    {Fore.BLUE}   ___      _                _            _       
    {Fore.BLUE}  / __\__ _| | ___ _ __   __| | __ _ _ __(_) ___  
    {Fore.BLUE} / /  / _` | |/ _ \ '_ \ / _` |/ _` | '__| |/ _ \ 
    {Fore.BLUE}/ /__| (_| | |  __/ | | | (_| | (_| | |  | | (_) |
    {Fore.BLUE}\____/\__,_|_|\___|_| |_|\__,_|\__,_|_|  |_|\___/
                                                            
    """

    # Imprime el texto
    print(texto)
    input()

                                                  
def mostrar_inventario():

    init(autoreset=True)

    texto = f"""
    {Fore.BLUE}  _____                      _             _       
    {Fore.BLUE}  \_   \_ ____   _____ _ __ | |_ __ _ _ __(_) ___  
    {Fore.BLUE}   / /\/ '_ \ \ / / _ \ '_ \| __/ _` | '__| |/ _ \ 
    {Fore.BLUE}/\/ /_ | | | \ V /  __/ | | | || (_| | |  | | (_) |
    {Fore.BLUE}\____/ |_| |_|\_/ \___|_| |_|\__\__,_|_|  |_|\___/ 
                                                   
                                                            
    """

    # Imprime el texto
    print(texto)
    input()

                                                  



def rutinas():

    try:
        contenido = open("Base_de_datos/rutinas.json", "r")
        lineas = contenido.read()
        contenido.close()

        rutinas = json.loads(lineas)

    except:
        print("error")

    a = int(input("Cuantos dias quiere entrenar por semana entre 3 y 6?: "))
    while a > 6 or a < 3:
            a = int(input("ERROR, Cuantos dias quiere entrenar por semana entre 3 y 6?: "))

    if a == 6:
        print(rutinas[0])
    elif a == 4:
         print(rutinas[2])
    elif a == 5:
         print(rutinas[3])
    elif a == 3:
        print(rutinas[1])


def hacerTuRutina():
    import json

    try:
        contenido = open("Base_de_datos/ejercicios.json", "r")
        lineas = contenido.read()
        contenido.close()

        ejercicios = json.loads(lineas)

    except:
        print("error")


    print(ejercicios["Pecho"])

    n = int(input("Ingrese el ejercicio que quiere para este musculo: "))

    ejerciciosPecho = []
    ejerciciosEspalda = []
    ejerciciosBiceps= []
    ejerciciosTriceps = []
    ejerciciosQuadriceps = []
    ejerciciosIsquiotibiales = []
    ejerciciosGemelos = []


    miRutina = {"Pecho" : ejerciciosPecho, 
                "Espalda": ejerciciosEspalda,  
                "Biceps" : ejerciciosBiceps , 
                "Triceps" : ejerciciosTriceps, 
                "Quadriceps" : ejerciciosQuadriceps, 
                "Isquiotibiales" : ejerciciosIsquiotibiales, 
                 "Gemelos" : ejerciciosGemelos }

    for n_ejercicio in ejercicios:
        if n_ejercicio["n"] in ejercicios:
            miRutina["Pecho"].append(n)

    for n_ejercicio in ejercicios:
        if n_ejercicio["n"] in ejercicios:
            miRutina["Pecho"].append(n)
    

    for n_ejercicio in ejercicios:
        if n_ejercicio["n"] in ejercicios:
            miRutina["Pecho"].append(n)

    for n_ejercicio in ejercicios:
        if n_ejercicio["n"] in ejercicios:
            miRutina["Pecho"].append(n)

    for n_ejercicio in ejercicios:
        if n_ejercicio["n"] in ejercicios:
            miRutina["Pecho"].append(n)

    for n_ejercicio in ejercicios:
        if n_ejercicio["n"] in ejercicios:
            miRutina["Pecho"].append(n)

    for n_ejercicio in ejercicios:
        if n_ejercicio["n"] in ejercicios:
            miRutina["Pecho"].append(n)

# FUNCIONES INVENTARIO/RECETAS
def inventario():
    pass





texto_dieta ="""Para bajar de peso, es importante seguir una dieta hipocalórica, equilibrada y rica en nutrientes para asegurarte de perder grasa corporal mientras mantienes la masa muscular. Aquí tienes un plan de alimentación general que puedes adaptar según tus necesidades."""
texto_definicion = """Una dieta de definición se centra en reducir el porcentaje de grasa corporal mientras se mantiene la masa muscular. Es similar a una dieta de pérdida de peso, pero con un enfoque especial en preservar el músculo. Aquí tienes un plan de alimentación para ayudarte a lograrlo."""
texto_volumen= """Para aumentar el volumen muscular, es fundamental seguir una dieta hipercalórica, rica en proteínas, carbohidratos y grasas saludables, junto con un entrenamiento adecuado. Aquí tienes un plan general de dieta que puedes adaptar según tus necesidades y preferencias."""




def busqueda_secuencial(lista, dato):
    i = 0
    while i < len(lista) and lista[i] != dato:
        i+=1
    if i < len(lista):
        return i
    else:
        return -1
    
    '''
