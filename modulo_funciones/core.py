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


        op = errorEntero()    

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
            os.system("cls")
            print("error, elija un numero del 1 al 4")
            input()

def mostrar_equipo():
    os.system('cls')
    print("\033[0;36m")
    print("\033[4;15HEquipo de desarrollo")
    print("\033[0;37m")
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

    print("\033[0;36m")
    print("\033[4;15HInstrucciones")
    print("\033[0;37m")
    
    print("""Este programa te permitira encontrar el mejor plan de alimentacion y entrenamiento.""")
    print("")
    print("Carga datos personales del usuario para calcular tu metabolismo basal y encontrar la mejor ruta para alcanzar sus metas.")
    print("Un nuevo estilo de vida saludable esta ahora en tus manos! Para utilizar el programa, solo debes seguir las siguientes instrucciones: ")
    print("")
    print("1. Registro e Ingreso de datos personales. ")
    print("")
    print("2. Determinar tus objetivos nutricionales, como bajar de peso o ganar masa muscular.")
    print("")
    print("3. Recibe tu plan de alimentacion y entrenamiento personalizado.")
    print("")
    print("""4. Comenza tu plan!. La constancia y disciplina son elementos clave. """)
    print("")
    
def ejecutar():
    os.system('cls')
    ingresar_cuenta()


def errorEntero():

    try:
        opcion = int(input("Seleccione una opción del menu: "))
        return opcion
    except:
        print("Error, ingrese un numero del 1 al 3.")
#FUNCIONES LOGIN

def ingresar_cuenta():
    menu= True
    while menu:
        os.system('cls')

        print("\033[0;36m")
        print("\033[4;15HInicio de sesion")
        print("\033[0;37m")
        print("")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")


        opcion = errorEntero()
        
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
        return usuario_existente, usuarios[nombre_usu]
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
    
    while g.usuario_existente:  
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
        f.seek(0)  
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
    else:
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

        print("\033[0;36m")
        print("\033[4;15HMenu")
        print("\033[5;15HFit App")
        print("\033[0;37m")

        print("1. Información personal")
        print("2. Rutinas")
        print("3. Inventario")
        print("4. Cerrar sesion")

        op= errorEntero()

        if op==1:
                datos_usuario()
                definir_objetivo()
                input()
        elif op==2:
            mostrar_titulo_rutinas()
            try:
                os.system('cls')
                n = int(input("Seleccione 1 para elegir una rutina preestablecida o 2 para personalizar tu propia rutina."))
                if n ==1:
                    elegir_Rutina()
                elif n ==2:
                    hacer_Rutina()
                else:
                    print("Error, elija el numero 1 o 2.")
            except:
                print("Error, Opción no válida")
            mostrar_calendario()
            input()
        elif op==3:
            mostrar_inventario()
            inventario()
            input()

        elif op==4:
            print("Cerrando sesion.")
            repetir= False
        else:
            print("Error!, elija un numero del 1 al 4")
            input()
        

#FUNCIONES INGRESO DATOS
def datos_usuario():
    os.system('cls')
    if len(g.datos_de_usuario) > 1:
        print("El usuario ya existe.")
        print("")
        print("Bienvenido", g.nombre ,"! A continuacion puede visualizar sus datos cargados.")
        print("")

        for clave, valor in g.datos_de_usuario.items():
            print(f"{clave}: {valor}")

        try:
            actualizar= input("Desea actualizar sus datos? (si/no)")
            if actualizar=="si":
                os.system('cls')
                cargar_datos()
                print("Listo! Ya se han actualizado sus datos") 
            else:
                print("Puede continuar utilizando el programa con normalidad ... ")  
        except:
            print("Error, ingresar si o no")
    else:
        cargar_datos()
    

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
    g.datos_de_usuario = usuarios[g.nombre]
  
    with open(ruta_archivo_json, 'w') as f:
        json.dump(usuarios, f, indent=4)

def cargar_info_personal():
    os.system('cls')

    print("\033[0;36m")
    print("\033[4;15HDatos del usuario")
    print("\033[0;37m")

    print("Necesitamos que cargues los siguientes datos para calcular tus calorias de mantenimiento.")
    print("")

    bandera = True
    while bandera:
        g.altura= int(input("Por favor, ingrese su altura en cm: "))
        if g.altura <= 0:
            print("La edad no es válida. Por favor, intentelo de nuevo.")
        else:
            bandera = False
    
    bandera = True
    while bandera:
        g.peso = int(input("Ingrese su peso en KG: "))
        if g.peso <= 0:
            print("El peso no es válido. Por favor, intentelo de nuevo.")
        else:
            bandera = False

    bandera = True
    while bandera:
        g.edad = int(input("Ingrese su edad: "))
        if g.edad<=0 or g.edad>100:
            print("La edad no es válida. Por favor, intentelo de nuevo.")
        else:
            bandera = False

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
    g.cantidad_ejercicio = int(input('''Ingrese la cantidad de ejercicio que realiza usualmente durante la semana; 
                                     1. Si no realiza ejercicio
                                     2. Si ejercita 1-3 veces a la semana ingrese 2
                                     3. Si hace 3-5 veces a la semana
                                     4. Si hace 6-7 veces a la semana
                                     5. Si hace 2 veces al dia o mas. '''))
    g.usuario_existente=True
    return g.altura, g.peso, g.edad, g.sexo, g.cantidad_ejercicio

def calcular_calorias (altura, peso, edad, sexo, cantidad_ejercicio):
    if sexo == "H":
        calorias = (10 * peso) + (6.25 * altura) - (5 * edad) + 5
        
    else:
        calorias = (10 * peso) + (6.25 * altura) - (5 * edad) - 161

    if cantidad_ejercicio == 1:
            calorias = calorias * 1.2
               
    elif cantidad_ejercicio == 2:
            calorias = calorias * 1.375
                
    elif cantidad_ejercicio == 3:
            calorias = calorias * 1.55
               
    elif cantidad_ejercicio == 4:
            calorias = calorias * 1.725
                
    elif cantidad_ejercicio == 5:
            calorias = calorias * 1.9
                

    return calorias

def definir_objetivo() :
    os.system('cls')
    texto_aumento_musculo= """|1_ Para aumentar el volumen muscular, es fundamental seguir una dieta hipercalórica que puede variar su riqueza en proteínas, carbohidratos y grasas saludables, junto con un entrenamiento adecuado."""
    texto_quemar_grasa = """|2_ Una dieta de definición se centra en reducir el porcentaje de grasa corporal mientras se mantiene la masa muscular. Es una dieta de pérdida de peso, pero con un enfoque especial en preservar el músculo."""
    texto_mantenimiento= """|3_ Ya sabiendo nuestras calorias de mantenimiento, podemos con esto mantener nuestro peso."""

    print("\033[0;36m")
    print("\033[4;15HDatos del usuario")
    print("\033[0;37m")

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
            os.system('cls')
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

# FUNCIONES Rutinas
def mostrar_titulo_rutinas():
    pass

def mostrar_titulo_calendario():
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

#RUTINAS
def solicitar_dias_entrenamiento():
    os.system("cls")

    bandera = True
    while bandera:
        try:
            dias = int(input("¿Cuántos días quiere entrenar por semana entre 3 y 6?: "))
            if dias < 3 or dias > 6:
                print("Error, debe ser entre 3 y 6.")
            else:
                bandera = False
                return dias      
        except ValueError:
            print("Error, debe ingresar un número válido.")

def cargar_rutinas():
    try:
        with open("Base_de_datos/rutinas.json", "r") as contenido:
            rutinas = json.load(contenido)
        return rutinas
    
    except FileNotFoundError:
        print("Error: El archivo no se encontró.")
        return None

def elegir_Rutina():

    print("\033[0;36m")
    print("\033[4;15HRutinas")
    print("\033[0;37m")

    rutinas = cargar_rutinas()
    g.dias_entrenamiento_plan = solicitar_dias_entrenamiento()
    
    if g.dias_entrenamiento_plan == 6:
        g.rutinaSeleccionada = rutinas[0]

    elif g.dias_entrenamiento_plan == 4:
        g.rutinaSeleccionada = rutinas[2] 
        
    elif g.dias_entrenamiento_plan == 5:
        g.rutinaSeleccionada = rutinas[3] 
        
    elif g.dias_entrenamiento_plan == 3:
        g.rutinaSeleccionada = rutinas[1] 

    os.system("cls")
    print("\033[0;36m")
    print("\033[4;15HSu rutina!")
    print("\033[0;37m")

    for clave, valor in g.rutinaSeleccionada.items():
            print(f"**{clave}**:")  # Imprime el nombre de la categoría
            for ejercicio, detalles in valor.items():  # Itera sobre los ejercicios en cada categoría
                if detalles["ejercicio"]:  # Verifica que el ejercicio no esté vacío
                    print(f"  {ejercicio:<20} {detalles['ejercicio']:<30} - Series: {detalles['series']:<5} - Repeticiones: {detalles['repeticiones']:<5}")
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
    os.system('cls')
    print("Genial! Aqui podras armar tu propia rutina de entrenamiento!")
    input()
    
    os.system('cls')
    print("\033[0;36m")
    print("\033[4;15HPersonalizar rutina")
    print("\033[0;37m")

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
            ejercicio = input("Escriba un ejercicio de igual manera a como esta mostrado para agregarlo a su rutina: ")

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

#CALENDARIO
def es_bisiesto(año):
    return año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)

def dias_en_mes(mes, año):
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mes in [4, 6, 9, 11]:
        return 30
    elif mes == 2:
        return 29 if es_bisiesto(año) else 28
    return 0

# Algoritmo de Zeller para calcular el día de la semana
def calcular_dia_semana(año, mes, dia):
    if mes < 3:
        mes += 12
        año -= 1
    k = año % 100
    j = año // 100
    dia_semana = (dia + 13 * (mes + 1) // 5 + k + k // 4 + j // 4 - 2 * j) % 7
    return (dia_semana + 6) % 7  

def generar_calendario(mes, año):
    dias = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
    print(f"\nCalendario: {mes}/{año}")
    print(f"{' '.join([d[:3] for d in dias])}")
    
    primer_dia = calcular_dia_semana(año, mes, 1)
    num_dias = dias_en_mes(mes, año)

    calendario = ["    "] * primer_dia

    for dia in range(1, num_dias + 1):
        calendario.append(f"{dia: >3} ")

    for i in range(0, len(calendario), 7):
        print("".join(calendario[i:i+7]))

def fechas_por_dia_semana(mes, año):
    dias = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
    fechas = {dia: [] for dia in dias}
    num_dias = dias_en_mes(mes, año)
    
    for dia in range(1, num_dias + 1):
        dia_semana = calcular_dia_semana(año, mes, dia)
        fechas[dias[dia_semana]].append(dia)
    
    # Imprimir las fechas clasificadas

    if g.dias_entrenamiento_plan == 6:
        print(f"Entrenamientos de {g.dias_entrenamiento_plan} días")
        print("Lunes --- Pull")
        print("Martes --- Push")
        print("Miercoles --- Legs")
        print("Jueves --- Pull")
        print("Viernes --- Push")
        print("Sabado --- Legs")
        print("Domingo- Descanso")

        ''''
        print(f"{"Lunes"}: {', '.join(map(str, lista))}")
        print("Martes")
        print(f"{'Martes'}: {', '.join(map(str, lista))}")
        print("Miércoles")
        print(f"{'Miércoles'}: {', '.join(map(str, lista))}")
        print("Jueves")
        print(f"{'Jueves'}: {', '.join(map(str, lista))}")
        print("Viernes")
        print(f"{'Viernes'}: {', '.join(map(str, lista))}")
        print("Sábado")
        print(f"{'Sábado'}: {', '.join(map(str, lista))}")
        print("Domingo")
        print(f"{'Domingo'}: {', '.join(map(str, lista))}")
        
        for dia, lista in fechas.items():
            print(f"{dia}: {', '.join(map(str, lista))}")
            '''

    elif g.dias_entrenamiento_plan == 4:
        print(f"Entrenamientos de {g.dias_entrenamiento_plan} días")
        print("Lunes --- Tren Inferior")
        print("Martes --- Tren Superior")
        print("Miercoles --- Descanso")
        print("Jueves --- Tren Inferior")
        print("Viernes --- Tren Superior")
        print("Sabado --- Descanso")
        print("Domingo --- Descanso") 

    elif g.dias_entrenamiento_plan == 5:
        print(f"Entrenamientos de {g.dias_entrenamiento_plan} días")
        print("Lunes --- Pull")
        print("Martes --- Push")
        print("Miercoles --- Legs")
        print("Jueves --- Descanso")
        print("Viernes --- Pecho y Espalda")
        print("Sabado --- Legs")
        print("Domingo- Descanso")

    elif g.dias_entrenamiento_plan == 3:
        print(f"Entrenamientos de {g.dias_entrenamiento_plan} días")
        print("Lunes --- Full Body")
        print("Martes --- Descanso")
        print("Miercoles --- Full Body")
        print("Jueves --- Descanso")
        print("Viernes --- Full Body")
        print("Sabado --- Descanso")
        print("Domingo --- Descanso")
    
def mostrar_calendario():
    visualizar= int(input("Si desea visualizar su plan de entrenamiento en el calendario seleccione 1."))
    if visualizar == 1:
        os.system('cls')
        mostrar_titulo_calendario()
        try:
            mes = int(input("Ingrese el mes (1-12): "))
            año = int(input("Ingrese el año: "))

            if 1 <= mes <= 12:
                generar_calendario(mes, año)
                print("\nSu plan de entrenamiento este mes:")
                fechas_por_dia_semana(mes, año)
            else:
                print("Por favor, ingrese un mes válido (1-12).")
        except ValueError:
            print("Por favor, ingrese valores numéricos válidos.")
      
# FUNCIONES INVENTARIO/RECETAS

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

def inventario():
    
    print("""Esta función nos permite almacenar las comidas que tengas a disponibilidad, para esto
           vas a tener que buscarlas dentro de nuestro diccionario de comidas y luego escribir si alguna
          de las comidas mostradas a continuacion esta a tu alcance""")
    print("Grupos de comidas disponibles:")

    with open('Base_de_datos/comidas.json','r') as f:
        comidas = json.load(f)
    
    #Imprimir grupos
    for clave in comidas.keys():
        print(clave)
        print("--")

    #Seleccionar grupo
    g.miHeladera = {}

    bandera = True
    while bandera:
        grupo = input("Selecciona un grupo de comidas (o escriba -1 para terminar): ")

        if grupo== "-1":
            bandera = False

        elif grupo in comidas:
            comidas_grupo = comidas[grupo]
            print(f"Comidas disponibles para {grupo}: ")

            for comida in comidas_grupo:
                print(comida)
            print() 
            comida = input("Escriba una comida de igual manera a como esta mostrada para agregarlo a su heladera: ")

            if comida in comidas_grupo:
                
                
                g.miHeladera[f"{comida}"] = comidas_grupo[comida]

                print(f"La comida '{comida}' agregada a la heladera.")

            else:
                print("Comida no encontrada. Intenta de nuevo.")
        else:
            print("Grupo de comida no encontrado. Intenta de nuevo.")
    print("Su heladera es: ")
    print(g.miHeladera)
    input()
    miDieta()

def miDieta():
    g.miDieta = {}

    print(f"Con las calorias que usted necesita consumir, kcal: '{g.calorias}', elija ingredientes o comidas de su heladera para llegar a sus calorias deseadas.")

    bandera = True
    while bandera:
        for comida in g.miHeladera:
            print(comida)
            print("--")

        comida = input("Selecciona una comida para agregar a tu dieta (o escriba -1 para terminar): ")

        if comida== "-1":
            bandera = False

        elif comida in g.miHeladera:
            print(f"Comidas de tu heladera: ")

            g.miDieta[f"{comida}"] = g.miHeladera[comida]

            print(f"La comida '{comida}' fue agregada a la heladera.")

        else:
            print("Comida no encontrada. Intenta de nuevo.")
    print("Su dieta para hoy es: ")
    
    print(g.miDieta)




'''




def busqueda_secuencial(lista, dato):
    i = 0
    while i < len(lista) and lista[i] != dato:
        i+=1
    if i < len(lista):
        return i
    else:
        return -1
        
        
'''

