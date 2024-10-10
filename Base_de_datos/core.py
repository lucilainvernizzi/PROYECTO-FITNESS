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
                ejecutar()
            elif op==4:
                repetir=False 
            else:
                print("Error")
        except:
            print("Error")
            input()

#Opcion 1
def mostrar_equipo():
    print("Bienvenido! Esta App fue creada por el equipo compuesto por Lucila Invernizzi, Juan Ignacio Fernández Noceda, Mateo Castellanos y Matías Scoccia.")

#Opcion 2
def mostrar_inst():
    print("""Bienvenido a la App VSFit, donde encontraras recetas fitness y nutritivas! Este programa te permitira hallar el plan de alimentacion y entrenamiento adecuado. Con la carga de datos personales, sera evaluada la mejor ruta para alcanzar las metas determinadas por el usuario, hallando dietas y rutinas de ejercitacion personalizadas.")
    Un nuevo estilo de vida saludable esta ahora en tus manos. Para utilizar el programa, solo debes seguir las instrucciones que se te presentan a continuacion:""")

    print("""1. Registro e Ingreso de datos personales. Deberas crear una cuenta con tu nombre de usuario, correo electronico y contrasena. Luego se solictara que ingreses datos personales como tu altura, peso, edad, genero y nivel de actividad fisica""")
    
    print("2. Determinar tus objetivos. ")
    print("Tendras la oportunidad de realizar un pequeno cuestionario que te permita clarificar tus objetivos nutricionales, como bajar de peso o ganar masa mucualar.")
    
    print("3. Recibir tu plan de alimentacion y entrenamiento personalizado.")
    print("El programa ")

    print("""4. Comenzar tu plan!. La constancia y disciplina son elementos clave para que tus objetivos se vuelvan realidad. Por este motivo, recibiras una serie de notificaciones semanales que te permitan seguir dia a dia tu plan personalizado. Tambien podras visualizar los pasos que debes seguir en nuestra ventana de calendario. Si no estas conmforme con las sugerencias realizadas por la App, siempre existe la posibilidad de modificar el plan a tu gusto.""")
   
    print("5. Seguimiento del plan!")
    print("Una vez iniciado el plan, es muy importante que se reciba un feedback por parte del usuario para analizar la eficiencia de los metodos sugeridos por nuestro sistema. De esta manera podremos ")
    print("Dentro de la App podras encontrar un inventario digital de tu propio hogar que nos permitira crear recetas en base a los alimentos con los que cuentas. Tambien contamos con una funcion -Lista de supermercado- donde te sugeriremos productos que podrias agregar a tu almacen para las recetas que conforman tu plan.")

#Opcion 3
def ejecutar():
    return


texto_dieta ="""Para bajar de peso, es importante seguir una dieta hipocalórica, equilibrada y rica en nutrientes para asegurarte de perder grasa corporal mientras mantienes la masa muscular. Aquí tienes un plan de alimentación general que puedes adaptar según tus necesidades."""
texto_definicion = """Una dieta de definición se centra en reducir el porcentaje de grasa corporal mientras se mantiene la masa muscular. Es similar a una dieta de pérdida de peso, pero con un enfoque especial en preservar el músculo. Aquí tienes un plan de alimentación para ayudarte a lograrlo."""

#ingreso de datos

def cargar_datos():
    altura= int(input("Por favor, ingrese su altura en cm: "))

    peso = int(input("Ingrese su peso en KG: "))

    edad = int(input("Ingrese su edad: "))

    sexo = input("¿Cuál es su sexo? (H/M): ")
    if sexo.upper() == "H":
        return "H"
    elif sexo.upper() == "M":
        return "M"
    else:
        print("Sexo no válido. Por favor, ingrese H o M.")

    return altura, peso, edad, sexo




def calcular_metabolismo_basal(sexo, altura, peso, edad):
    if sexo == "H":
        return (10 * peso) + (6.25 * altura) - (5 * edad) + 5
    elif sexo == "M":
        return (10 * peso) + (6.25 * altura) - (5 * edad) - 161



def main():
    print("Excelente , sigamos con el programa ...")
    alturas, pesousu, años, sexos = cargar_datos()
    calculo = calcular_metabolismo_basal(sexos, alturas, pesousu, años)
    print("Sus calorias ingeridas para un dia serian :", calculo, "kcal")
    dieta_seleccionada = dieta()
    if dieta_seleccionada == "volumen":
        return #texto_volumen
    elif dieta_seleccionada == "bajar de peso":
        return texto_dieta
    elif dieta_seleccionada == "definicion":
        return texto_definicion

def dieta() :
    print("¿te gustaria hacer algun tipo de dieta? ")
    dieta = input("si o no ")
    if dieta == "si":
        print("¿que quieres conseguir con tu dieta? ")
        volumen = input("volumen,bajar de peso,definicion.")
        if volumen == "volumen" :
         print ("""Para aumentar el volumen muscular, es fundamental seguir una dieta hipercalórica, rica en proteínas, carbohidratos y grasas saludables, junto con un entrenamiento adecuado. Aquí tienes un plan general de dieta que puedes adaptar según tus necesidades y preferencias.""")
         return volumen
        elif volumen == "bajar de peso :":
          print(texto_dieta)
          return texto_dieta   
        elif volumen == "definicion :" :
         print(texto_definicion)
        return texto_definicion


if __name__ == "__main__":
    interfaz()
    main()





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


#ingreso objetivos usuario
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