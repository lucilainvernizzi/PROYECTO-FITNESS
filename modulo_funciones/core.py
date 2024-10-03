import os

def menu():
    repetir = True
    while repetir:
        
        print("1. Equipo")
        print("2. Instrucciones del programa")
        print("3. Ejecutar")
        print("4. Salir")

        try:
            op= int(input("Ingrese un valor del menu."))

            if op==1:
                mostrar_equipo()
            elif op==2:
                mostrar_inst()
            elif op==3:
                 repetir=False   
            
            elif op==4:
                ejecutar()
            else:
                print("Error")
        except:
            print("Error")
            input()


def mostrar_equipo():
    print("Bienvenido! Esta App fue creada por el equipo compuesto por Lucila Invernizzi, Juan Ignacio Fernández Noceda, Mateo Castellanos y Matías Scoccia.")

def mostrar_inst():
    print("""Bienvenido a la App de recetas Fitness y nutritivas! Este programa te permitira encontrar el plan de alimentacion y entrenamiento adecuado para cada usuario. Con la carga de datos personales del usuario, sera evaluada la mejor ruta para alcanzar las metas determinadas por el usuario, hallando dietas y rutinas de ejercitacion personalizadas.")
    Un nuevo estilo de vida saludable esta ahora en tus manos Para utilizar el programa, solo debes seguir las instrucciones que se te presenan a continuacion:""")

    print("""1. Registro e Ingreso de datos personales.Deberas crear una cuenta con tu nombre de usuario, correo electronico y contrasena. Luego se solictara que ingreses datos personales como tu altura, peso, edad, genero y nivel de actividad fisica""")
    
    print("2. Determinar tus objetivos. ")
    print("Tendras la oportunidad de realizar un pequeno cuestionario que te permita clarificar tus objetivos nutricionales, como bajar de peso o ganar masa mucualar.")
    
    print("3. Recibir tu plan de alimentacion y entrenamiento personalizado.")
    print("El programa ")

    print("""4. Comenzar tu plan!. La constancia y disciplina son elementos clave para que tus objetivos se vuelvan realidad. Por este motivo, recibiras una serie de notificaciones semanales que te permitan seguir dia a dia tu plan personalizado. Tambien podras visualizar los pasos que debes seguir en nuestra ventana de calendario. Si no estas conmforme con las sugerencias realizadas por la App, siempre existe la posibilidad de modificar el plan a tu gusto.""")
   
    print("5. Seguimiento del plan!")
    print("Una vez iniciado el plan, es muy importante que se reciba un feedback por parte del usuario para analizar la eficiencia de los metodos sugeridos por nuestro sistema. De esta manera podremos ")
    print("Dentro de la App podras encontrar un inventario digital de tu propio hogar que nos permitira crear recetas en base a los alimentos con los que cuentas. Tambien contamos con una funcion -Lista de supermercado- donde te sugeriremos productos que podrias agregar a tu almacen para las recetas que conforman tu plan.")

def ejecutar():
    return

#Funcion para recetas: Importa del archivo json el diccionario de recetas.
#Esta incompleto el algoritmo para ver si las comidas del usuario coinciden con las recetas y decirle que recetas puede hacecr

def busqueda_secuencial(lista, dato):
    i = 0
    while i < len(lista) and lista[i] != dato:
        i+=1
    if i < len(lista):
        return i
    else:
        return -1
    

#funciones sugerencia dieta y rutinas para formar plam y cumplimiento de objetivos

def sugerir_recetas():
    import json
    with open('recetas.json') as f:
        recetas = json.load(f)

    comidas = []
    n = str(input("Ingrese un ingrediente o -1 para terminar: "))


    while n != "-1":
        n = str(input("Ingrese un ingrediente o -1 para terminar: "))

    i = 0
    s = True
    while i < len(comidas) and s == True:

        encontrado = busqueda_secuencial(recetas, comidas[i])
        if encontrado != -1:


            i = i + 1
        else:
            s = False
    
     
    print(recetas['1'])
    print(recetas['2'])
    print(recetas['3'])

def sugerir_rutinas():
    obj= ingresar_objetivo()
    cant_dias= ingresar_dias_entrenamiento ()
    
    print("Su rutina de entrenamiento ideal es:")
    try:
        if obj==1:
            print("Para tonificar no hay nada mejor que el entrenamiento de fuerza con intervalos de cardio.") 
            print ()
            print ("Dia Lunes: ")
            rutina_lunes= ["8 Kettlebell desde sentadilla frontal", "10 burpees", "8 kettlebell balanceo Ruso", "10 burpees", "8 kettlebell press de hombro", "10 burpees"]
            for i in range (len(rutina_lunes)+1):
                print(rutina_lunes[i], sep= "-")
        elif obj==2:
            print("Si tu objetivo es bajar de peso,") 
            print ()
            print ("Dia Lunes: ")

        elif obj==3:
            print("Aumentar masa muscular, el entrenamiento de fuerza musculatoria es el mas indicado para ti.")
            
        elif obj==4:
            print("Dado que tu objetivo no esta definido")
        else:
            print("Error")
    except:
        print("Error")


#ingreso objetivos usuario
def ingresar_objetivo():
            
    print("1. Tonificar sus musculos.")
    print("2. Bajar de peso.")
    print("3. Aumentar masa muscular.")
    print("4. No tengo un objetivo definido.")

    objetivo= int(input("Ingrese su numero de objetivo: "))
    return objetivo

def ingresar_dias_entrenamiento():
   dias = int(input("Ingrese cuantos dias desea entrenar por semana: "))
   while dias<1 or dias>7:
       print("Error. La cantidad de dias no es valida")
       dias = int(input("Ingrese cuantos dias desea entrenar por semana: "))           
           
   return dias