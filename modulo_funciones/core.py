import os
import json
from colorama import init, Fore, Back, Style
import modulo_funciones.GLOBAL as g


#FUNCIONES MENU PRINCIPAL
def intro():

    init(autoreset=True)

    texto = f"""
    {Fore.BLUE}    ___    ____  ____     _________________   __________________
    {Fore.BLUE}   /   |  / __ \/ __ \   / ____/  _/_  __/ | / / ____/ ___/ ___/
    {Fore.BLUE}  / /| | / /_/ / /_/ /  / /_   / /  / / /  |/ / __/  \__ \\__ \ 
    {Fore.BLUE} / ___ |/ ____/ ____/  / __/ _/ /  / / / /|  / /___ ___/ /__/ / 
    {Fore.BLUE}/_/  |_/_/   /_/      /_/   /___/ /_/ /_/ |_/_____//____/____/  
                                                            
    """

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

        opcion_valida = False  
        while not opcion_valida:  
            try:
                op = int(input("Ingrese un valor del menu: "))
                opcion_valida = True 
            
            except ValueError:
                print("Por favor, ingrese un número válido.")
            
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
            menu = False
        else:
            print("Opción no válida. Inténtelo de nuevo.")
            opcion = input("Seleccione una opción del menu: ")

def verificar_o_crear_archivo_json():
    ruta_proyecto = os.path.join(os.path.dirname(__file__), '..') 
    ruta_carpeta = os.path.join(ruta_proyecto, 'base_de_datos') 

    # Ruta completa al archivo usuarios.json
    ruta_archivo_json = os.path.join(ruta_carpeta, 'usuarios.json')

    if not os.path.exists(ruta_archivo_json):
        
        with open(ruta_archivo_json, 'w') as f:
            json.dump({}, f, indent=4)
        print(f"Archivo 'usuarios.json' creado en {ruta_archivo_json}")
    return ruta_archivo_json

def verificar_datos(nombre_usu):
    ruta_archivo_json = verificar_o_crear_archivo_json()
    
    with open(ruta_archivo_json, 'r') as f:
        usuarios = json.load(f)

    if nombre_usu in usuarios:
        usuario_existente =  True 
        return usuario_existente, usuarios.get(nombre_usu)
    else:
        usuario_existente = False
        return usuario_existente, {}
    
def crear_usuario():
    os.system('cls')
    print("Registro de nuevo usuario")
    print("")
    g.nombre = input("Ingrese su nombre de usuario: ")
    g.contraseña = input("Ingrese su contraseña: ")

    g.usuario_existente, g.datos_de_usuario = verificar_datos(g.nombre)
    
    while g.usuario_existente:  # Cambié g.usuario a g.usuario_existente
        try:
            opcion = int(input("El nombre de usuario ya existe. Intente con otro nombre de usuario (1) o inicie sesión (2)."))
            if opcion == 1:
                g.nombre = input("Ingrese su nombre de usuario: ")
                g.contraseña = input("Ingrese su contraseña: ")
                g.usuario_existente, g.datos_de_usuario = verificar_datos(g.nombre)
            elif opcion == 2:
                iniciar_sesion()
            else:
                print("Error. Opción no válida.")
        except:
            print("Error")

    # Agregar al archivo json un diccionario de datos como valor de la clave con el nombre del usuario
    nuevo_usuario = {'contraseña': g.contraseña}  
   
    with open(verificar_o_crear_archivo_json(), 'r+') as f:
        usuarios = json.load(f)
        usuarios[g.nombre] = nuevo_usuario  # Agregar el nuevo usuario al diccionario
        f.seek(0)  # Mover el cursor al inicio del archivo
        json.dump(usuarios, f, indent=4)  # Guardar el diccionario actualizado
    
    input()
    os.system('cls') 
    print("¡Usuario registrado con éxito!")
    input()
    menu_secundario()

def iniciar_sesion():
    os.system('cls')
    print("Inicio de sesión")
    print("")
    g.nombre = input("Ingrese su nombre de usuario: ")
    g.contraseña = input("Ingrese su contraseña: ")

    ruta_archivo_json = verificar_o_crear_archivo_json()

    try:
        with open(ruta_archivo_json, 'r') as f:
            usuarios = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError): 
        print("No hay usuarios registrados o el archivo está corrupto.")
        return False

    if g.nombre in usuarios and usuarios[g.nombre]['contraseña'] == g.contraseña:
        os.system('cls') 
        print(f"Bienvenido/a {g.nombre} nuevamente")
        g.usuario_existente, g.datos_de_usuario = verificar_datos(g.nombre)
        input()
        menu_secundario()
        return True
    
    os.system('cls')
    print("Nombre de usuario o contraseña incorrectos.")
    print("")
    registrarse = input("¿Desea registrarse? (s/n): ")
    if registrarse.lower() == 's':
        crear_usuario()
    return False

#FUNCION MENU SECUNDARIO

def menu_secundario():
    repetir = True
    while repetir:
        os.system('cls')

        print("1. Información personal")
        print("2. Calendario")
        print("3. Inventario")
        print("4. Cerrar sesion")

        try:
            op= int(input("Ingrese un valor del menu."))

            if op==1:
                datos_usuario()
                definir_objetivo()
                input()
            elif op==2:
                mostrar_calendario()
                try:
                    n = int(input("Elija 1 para elegir una rutina hecha, o 2 para hacer tu propia rutina"))
                    if n ==1:
                        elegir_Rutina()
                    elif n ==2:
                        hacer_Rutina()
                    else:
                        print("Error, elija el numero 1 o 2.")
                except:
                    print("Error, Opción no válida")
                input()
            elif op==3:
                mostrar_inventario()
                inventario()
                input()
            elif op==4:
                print("Cerrando sesion.")
                repetir= False
            else:
                print("Error")
        except:
            print("Error")
            input()
    


#FUNCIONES INGRESO DATOS
def datos_usuario():
    os.system('cls')
    if g.usuario_existente:
        print("El usuario ya existe")
        print("")
        print("Bienvenido", g.nombre ,"! A continuacion puede visualizar sus datos cargados.")
        print("")
        print(g.datos_de_usuario)
        print("")

        actualizar= input("Desea actualizar sus datos? (si/no)")
        if actualizar=="si":
            cargar_datos()
            print("Listo! Ya se han actualizado sus datos") 
        else:
            print("Puede continuar utilizando el programa con normalidad ... ")  
    else:
        cargar_datos()
    return

def cargar_datos():
    altura_usuario, peso_usuario, edad_usuario, sexo_usuario, cantidad_ejercicio = cargar_info_personal()
    calculo_calorias = calcular_calorias(altura_usuario, peso_usuario, edad_usuario, sexo_usuario, cantidad_ejercicio)
    #objetivo_usuario= definir_objetivo()

    ruta_archivo_json = verificar_o_crear_archivo_json()
    g.calorias = calculo_calorias
      
    with open(ruta_archivo_json, 'r') as f:
        usuarios = json.load(f)
             
    agregar_datos = {
        "altura" : altura_usuario, 
        "peso" : peso_usuario,
        "edad" : edad_usuario, 
        "sexo" : sexo_usuario, 
        "calorias" : calculo_calorias,
        "cantidad_ejercicio" : cantidad_ejercicio,
        "heladera" : ''
        }
    usuarios[g.nombre].update(agregar_datos)

    with open(ruta_archivo_json, 'w') as f:
        json.dump(usuarios, f, indent=4)


def cargar_info_personal():
    os.system('cls')
    print("Necesitamos que cargues los siguientes datos para calcular tus calorias de mantenimiento.")
    
    g.altura= int(input("Por favor, ingrese su altura en cm: "))
    g.peso = int(input("Ingrese su peso en KG: "))
    g.edad = int(input("Ingrese su edad: "))

    bandera = True
    while bandera:
        g.sexo = input("¿Cuál es su sexo? (H/M): ")
        if g.sexo.upper() == "H":
            g.sexo= "H"
            bandera = False
        elif g.sexo.upper() == "M":
            g.sexo= "M"
            bandera = False
        else:
            print("Sexo no válido. Por favor, ingrese H o M.")
    input()
    
    os.system('cls')        
    g.cantidad_ejercicio = int(input("Ingrese la cantidad de ejercicio que haga durante la semana; si no hace ejercicio ponga 1, si hace 1-3 veces a la semana ingrese 2, si hace 3-5 veces a la semana ingrese 3, si hace 6-7 veces a la semana ingrese 4, si hace 2 veces al dia o mas ingrese 5: "))
    g.usuario_existente=True
    return g.altura, g.peso, g.edad, g.sexo, g.cantidad_ejercicio


def calcular_calorias (altura, peso, edad, sexo, cantidad_ejercicio):
    if sexo == "H":
        calorias = (10 * peso) + (6.25 * altura) - (5 * edad) + 5
        
        bandera=True
        while bandera==True:
            if cantidad_ejercicio == 1:
                calorias = calorias * 1.2
                bandera=False
            elif cantidad_ejercicio == 2:
                calorias = calorias * 1.375
                bandera=False
            elif cantidad_ejercicio == 3:
                calorias = calorias * 1.55
                bandera=False
            elif cantidad_ejercicio == 4:
                calorias = calorias * 1.725
                bandera=False
            elif cantidad_ejercicio == 5:
                calorias = calorias * 1.9
                bandera=False
            else:
                print("")
                cantidad_ejercicio = int(input("Por favor ingrese solo un numero del 1 al 5: "))
                print("")
    else:
        calorias = (10 * peso) + (6.25 * altura) - (5 * edad) - 161

        bandera=True
        while bandera==True:
            if cantidad_ejercicio == 1:
                calorias = calorias * 1.2
                bandera=False
            elif cantidad_ejercicio == 2:
                calorias = calorias * 1.375
                bandera=False
            elif cantidad_ejercicio == 3:
                calorias = calorias * 1.55
                bandera=False
            elif cantidad_ejercicio == 4:
                calorias = calorias * 1.725
                bandera=False
            elif cantidad_ejercicio == 5:
                calorias = calorias * 1.9
                bandera=False
            else:
                print("")
                cantidad_ejercicio = int(input("Por favor ingrese solo un numero del 1 al 5: "))
                print("")

    return calorias


def definir_objetivo() :
    os.system('cls')
    print("¿Cual es tu objetivo? ")
    print("")
    print("1. Ganar musculo")
    print("2. Quemar grasa")
    print("3. Mantenimiento")
    print("")
    print(texto_aumento_musculo)
    print("")
    print(texto_quemar_grasa)
    print("")
    print(texto_mantenimiento)
    print("")
    
    bandera=True
    while bandera:
        try:
            objetivo = int(input("Seleccione del menu: "))
            if objetivo == 1:
                print (texto_aumento_musculo)
                if g.sexo == "H":
                    g.calorias += 500
                elif g.sexo == "M":
                    g.calorias += 250
                print("Estas son tu calorias para tu volumen: ", g.calorias)
                bandera=False


            elif objetivo == 2:
                print(texto_quemar_grasa)  
                if g.sexo == "H":
                    g.calorias -= 800
                elif g.sexo == "M":
                    g.calorias -= 400
                print("Estas son tus calorias para tu definicion: ", g.calorias)
                bandera=False
            
            elif objetivo == 3:
                print(texto_mantenimiento)
                print("Para mantener tu peso debes seguir comiendo las mismas calorias de mantenimiento: ", g.calorias)
                bandera=False

            else: 
                print("El valor ingresado es inválido, por favor intentelo de nuevo")
                objetivo = int(input("Seleccione del menu"))

        except: 
            print("Error")
            input()    
    return objetivo



# FUNCIONES CALENDARIO

def mostrar_calendario():
    os.system ('cls')

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
    os.system ('cls')

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

                                                  

#RUTINAS
def solicitar_dias_entrenamiento():
    bandera = True
    while bandera:
        try:
            dias = int(input("¿Cuántos días quiere entrenar por semana entre 3 y 6?: "))
            if dias < 3 or dias > 6:
                print("ERROR, debe ser entre 3 y 6.")
            else:
                bandera = False
                return dias
                
        except ValueError:
            print("ERROR, debe ingresar un número válido.")

def cargar_rutinas():
    try:
        with open("Base_de_datos/rutinas.json", "r") as contenido:
            rutinas = json.load(contenido)
        return rutinas
    
    except FileNotFoundError:
        print("Error: El archivo no se encontró.")
        return None

def elegir_Rutina():

    rutinas = cargar_rutinas()
    a = solicitar_dias_entrenamiento()
    
    if a == 6:
        g.rutinaSeleccionada = rutinas[0]

    elif a == 4:
        g.rutinaSeleccionada = rutinas[2] 
        
    elif a == 5:
        g.rutinaSeleccionada = rutinas[3] 
        
    elif a == 3:
        g.rutinaSeleccionada = rutinas[1] 

    for clave, valor in g.rutinaSeleccionada.items():
            print(f"**{clave}**:")  # Imprime el nombre de la categoría
            for ejercicio, detalles in valor.items():  # Itera sobre los ejercicios en cada categoría
                if detalles["ejercicio"]:  # Verifica que el ejercicio no esté vacío
                    print(f"  {ejercicio}: {detalles['ejercicio']} - Series: {detalles['series']}, Repeticiones: {detalles['repeticiones']}")
            print()

def cargar_ejercicios():
    try:
        with open("Base_de_datos/ejercicios.json", "r") as contenido:
            ejercicios = json.load(contenido)
        return ejercicios
    
    except FileNotFoundError:
        print("Error: El archivo no se encontró.")
        return None

def hacer_Rutina():


    ejercicios = cargar_ejercicios()


    print("Ejercicios disponibles por grupo muscular:")
    for grupo in ejercicios.keys():
        print(grupo)
        print("--")

    g.miRutina = {
        "Ejercicio1" : {},
        "Ejercicio2" : {}, 
        "Ejercicio3" : {},
        "Ejercicio4" : {}, 
        "Ejercicio5" : {},  
        "Ejercicio6" : {},
        "Ejercicio7" : {}, 


    }

    bandera = True
    i = 1
    while bandera:
        grupo = input("Selecciona un grupo muscular (o escriba -1 para terminar): ")

        if grupo== "-1":
            bandera = False

        elif grupo in ejercicios:
            ejercicios_grupo = ejercicios[grupo]
            print(f"Ejercicios disponibles para {grupo}: ")

            for ejercicio in ejercicios_grupo:
                print(ejercicio)
            print()  # Nueva línea después de listar los ejercicios
            ejercicio = input("Escriba un ejercicio de igual manera a como esta mostrado para agrgarlo a su rutina: ")

            if ejercicio in ejercicios_grupo:
                try:
                    series = int(input("Ingrese el número de series: "))
                    repeticiones = int(input("Ingrese el número de repeticiones: "))
                except:
                    print("Porfavor elija un numero")

                ejercicio_info = {
                    "ejercicio": ejercicio,
                    "series": series,
                    "repeticiones": repeticiones
                }

                g.miRutina[f"Ejercicio{i}"] = ejercicio_info

                print(f"Ejercicio '{ejercicio}' agregado a la rutina.")

            else:
                print("Ejercicio no encontrado. Intenta de nuevo.")
        else:
            print("Grupo muscular no encontrado. Intenta de nuevo.")
        i += 1

    print(g.miRutina)

    g.datos_de_usuario["miRutina"] = g.miRutina

# FUNCIONES INVENTARIO/RECETAS
def inventario():
    
    print("""Esta función nos permite almacenar las comidas que tengas a disponibilidad, para esto
           vas a tener que buscarlas dentro de nuestro diccionario de comidas y luego escribir si alguna
          de las comidas mostradas a continuacion esta a tu alcance""")
    print("Comidas disponibles:")

    with open('Base_de_datos/comidas.json','r') as f:
        comidas = json.load(f)
    
    for comida in comidas:
        print(comida)

    
    input()





texto_quemar_grasa = """|2_ Una dieta de definición se centra en reducir el porcentaje de grasa corporal mientras se mantiene la masa muscular. Es una dieta de pérdida de peso, pero con un enfoque especial en preservar el músculo."""
texto_aumento_musculo= """|1_ Para aumentar el volumen muscular, es fundamental seguir una dieta hipercalórica que puede variar su riqueza en proteínas, carbohidratos y grasas saludables, junto con un entrenamiento adecuado."""
texto_mantenimiento= """|3_ Ya sabiendo nuestras calorias de mantenimiento, podemos con esto mantener nuestro peso."""



def busqueda_secuencial(lista, dato):
    i = 0
    while i < len(lista) and lista[i] != dato:
        i+=1
    if i < len(lista):
        return i
    else:
        return -1
    

