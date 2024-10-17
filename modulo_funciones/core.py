#FUNCIONES MENU PRINCIPAL
import os
import json


def intro():
    os.system("cls")
    print("\033[0;36m]")
    print("\033[4;15HBienvenidos a la App Fitness")
    print("\033[5;15HProgramacion I")

    print("\033[0;37m]")
    input ()

def menu_principal():
    repetir = True
    while repetir:
        print("1. Equipo")
        print("2. Instrucciones del programa")
        print("3. Ejecutar")
        print("4. Salir")

        try:
            os.system("cls")
            op= int(input("Ingrese un valor del menu."))
            
            if op==1:
                mostrar_equipo()
            elif op==2:
                mostrar_inst()
            elif op==3:
                ejecutar()
            elif op==4:
                repetir= False
            else:
                print("Error")
        except:
            print("Error")
            input()


def mostrar_equipo():
    print("Bienvenido! Esta App fue creada por el equipo de:")
    print("Lucila Invernizzi, LU: 1201347")
    print("Juan Ignacio Fernández Noceda, LU: ")
    print("Mateo Castellanos, LU:")
    print("Matías Scoccia, LU: ")
    print("")
    print("Somos estudiantes de la materia Programacion I, de la carrera Ingeniería Informática en UADE.")
    print("")

def mostrar_inst():
    print("""Bienvenido a la App de recetas Fitness y nutritivas! Este programa te permitira encontrar el mejor plan de alimentacion y entrenamiento. Con la carga de datos personales del usuario, sera evaluada la mejor ruta para alcanzar sus metas.")
    Un nuevo estilo de vida saludable esta ahora en tus manos! Para utilizar el programa, solo debes seguir las siguientes instrucciones""")

    print("""1. Registro e Ingreso de datos personales. Deberas crear una cuenta con tu nombre de usuario y contrasena. Luego se solictara que ingreses datos personales como tu altura, peso, edad, genero y nivel de actividad fisica""")
    
    print("2. Determinar tus objetivos. ")
    print("Determinar tus objetivos nutricionales, como bajar de peso o ganar masa mucualar.")
    
    print("3. Recibir tu plan de alimentacion y entrenamiento personalizado.")
    print("El programa ")

    print("""4. Comenzar tu plan!. La constancia y disciplina son elementos clave para que tus objetivos se vuelvan realidad. Podras visualizar los pasos que debes seguir en nuestra ventana de calendario. """)
   
    print("5. !")
    print("Dentro de la App podras encontrar un inventario digital de tu propio hogar que nos permitira crear recetas en base a los alimentos con los que cuentas. ")


def ejecutar():
    ingresar_cuenta()
    menu_secundario()
    definir_calorias()
    sugerir_recetas()
    sugerir_rutinas()

#FUNCIONES LOGIN

def ingresar_cuenta():
    menu = True
    while menu:
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")

    try:
        opcion = int(input("Seleccione una opción del menu: "))

        if opcion == 1:
            crear_usuario()
        elif opcion == 2:
            iniciar_sesion()
        elif opcion == 3:
            print("Cerrando sesion.")
            menu = False
        else:
            print("Opción no válida. Inténtelo de nuevo.")
            opcion = input("Seleccione una opción del menu: ")
    except:
        print("Error")
        print()
        

def verificar_datos(nombre_usu):
    with open('usuarios.json', 'r') as f:
        datos_usu = json.load(f) 

    for usuario in datos_usu.get('usuarios', []):
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
        opcion= int(input())
        if opcion==1:
            nombre = input("Ingrese su nombre de usuario: ")
            contraseña = input("Ingrese su contraseña: ")
            usuario, datos_de_usuario= verificar_datos(nombre)
        elif opcion==2:
            iniciar_sesion()
            return #para salir de la funcion una vez que se inicia sesion
        else:
            print("Error")

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
                sugerir_rutinas()
            elif op==3:
                 sugerir_recetas()   
            elif op==4:
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
def sugerir_rutinas():
    obj= ingresar_objetivo()
    cant_dias= ingresar_dias_entrenamiento ()
    musculo= input("Que quieres entrenar hoy?")

    rutina_piernas= []
    rutina_brazos= []
    rutina_gluteos= []

    
    print("Su rutina de entrenamiento ideal es:")
    try:
        if obj==1:
            print("Para tonificar no hay nada mejor que el entrenamiento de fuerza con intervalos de cardio.") 
            print ()
            if musculo=="piernas":
                print ("Dia Lunes: ")
                for i in range (len(rutina_piernas)+1):
                    print(rutina_piernas[i], sep= "-")
            elif musculo=="brazos":
                for i in range (len(rutina_brazos)+1):
                    print(rutina_brazos[i], sep= "-")
            elif musculo=="gluteos":
                for i in range (len(rutina_gluteos)+1):
                    print(rutina_gluteos[i], sep= "-")


            
        elif obj==2:
            print("Si tu objetivo es bajar de peso,") 
            print ()
            if musculo=="piernas":
                print ("Dia Lunes: ")
                for i in range (len(rutina_piernas)+1):
                    print(rutina_piernas[i], sep= "-")
            elif musculo=="brazos":
                for i in range (len(rutina_brazos)+1):
                    print(rutina_brazos[i], sep= "-")
            elif musculo=="gluteos":
                for i in range (len(rutina_gluteos)+1):
                    print(rutina_gluteos[i], sep= "-")

        elif obj==3:
            print("Aumentar masa muscular, el entrenamiento de fuerza musculatoria es el mas indicado para ti.")
            print ()
            if musculo=="piernas":
                print ("Dia Lunes: ")
                for i in range (len(rutina_piernas)+1):
                    print(rutina_piernas[i], sep= "-")
            elif musculo=="brazos":
                for i in range (len(rutina_brazos)+1):
                    print(rutina_brazos[i], sep= "-")
            elif musculo=="gluteos":
                for i in range (len(rutina_gluteos)+1):
                    print(rutina_gluteos[i], sep= "-")

        elif obj==4:
            print("Dado que tu objetivo no esta definido, te sugerimos algunas rutinas de ejrciios generales que pueden ser utiles para mantener tu cuerpo em forma sin buscar un objetivo especifico.")
            print()
            if musculo=="piernas":
                print ("Dia Lunes: ")
                for i in range (len(rutina_piernas)+1):
                    print(rutina_piernas[i], sep= "-")
            elif musculo=="brazos":
                for i in range (len(rutina_brazos)+1):
                    print(rutina_brazos[i], sep= "-")
            elif musculo=="gluteos":
                for i in range (len(rutina_gluteos)+1):
                    print(rutina_gluteos[i], sep= "-")
        else:
            print("Error")
    except:
        print("Error")

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

def rutinas():
    import json

    try:
        contenido = open("archivos/rutinas.json", "r")
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