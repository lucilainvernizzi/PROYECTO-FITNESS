import os

texto_dieta ="""Para bajar de peso, es importante seguir una dieta hipocalórica, equilibrada y rica en nutrientes para asegurarte de perder grasa corporal mientras mantienes la masa muscular. Aquí tienes un plan de alimentación general que puedes adaptar según tus necesidades."""
texto_definicion = """Una dieta de definición se centra en reducir el porcentaje de grasa corporal mientras se mantiene la masa muscular. Es similar a una dieta de pérdida de peso, pero con un enfoque especial en preservar el músculo. Aquí tienes un plan de alimentación para ayudarte a lograrlo."""
texto_volumen= """Para aumentar el volumen muscular, es fundamental seguir una dieta hipercalórica, rica en proteínas, carbohidratos y grasas saludables, junto con un entrenamiento adecuado. Aquí tienes un plan general de dieta que puedes adaptar según tus necesidades y preferencias."""

#Paso 1: ingreso de datos

def cargar_datos():
    altura= int(input("Por favor, ingrese su altura en cm: "))

    peso = int(input("Ingrese su peso en KG: "))

    edad = int(input("Ingrese su edad: "))

    sexo = input("¿Cuál es su sexo? (H/M): ")
    if sexo.upper() == "H":
        sexo= "H"
    elif sexo.upper() == "M":
        sexo= "M"
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
    print("¿Te gustaria hacer algun tipo de dieta? ")
    dieta = str(input("si o no "))
    if dieta == "si":
        print("¿que quieres conseguir con tu dieta? ")
        objetivo = input("volumen, bajar de peso, definicion.")
        if objetivo == "volumen":
            print (texto_volumen)
        elif objetivo == "bajar de peso":
            print(texto_dieta)  
        elif objetivo== "definicion":
            print(texto_definicion)
        return objetivo


if __name__ == "__main__":
    main()




#Paso 2
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



#Paso 3

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
           
   return dias
