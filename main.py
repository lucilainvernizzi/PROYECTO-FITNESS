import core as f

def interfaz():
    f.menu()

texto_dieta ="""Para bajar de peso, es importante seguir una dieta hipocalórica, equilibrada y rica en nutrientes para asegurarte de perder grasa corporal mientras mantienes la masa muscular. Aquí tienes un plan de alimentación general que puedes adaptar según tus necesidades."""
texto_definicion = """Una dieta de definición se centra en reducir el porcentaje de grasa corporal mientras se mantiene la masa muscular. Es similar a una dieta de pérdida de peso, pero con un enfoque especial en preservar el músculo. Aquí tienes un plan de alimentación para ayudarte a lograrlo."""



def altura_usuario():
    alturas = int(input("Por favor, ingrese su altura en cm: "))
    return alturas

def peso_usuario():
    pesousu = int(input("Ingrese su peso en KG: "))
    return pesousu

def edad_usuario():
    años = int(input("Ingrese su edad: "))
    return años

def sexo_usuario():
    sexo = input("¿Cuál es su sexo? (H/M): ")
    if sexo.upper() == "H":
        return "H"
    elif sexo.upper() == "M":
        return "M"
    else:
        print("Sexo no válido. Por favor, ingrese H o M.")
        return sexo_usuario()


def metabolismo_basal(sexo, altura, peso, edad):
    if sexo == "H":
        return (10 * peso) + (6.25 * altura) - (5 * edad) + 5
    elif sexo == "M":
        return (10 * peso) + (6.25 * altura) - (5 * edad) - 161

def main():
    print("exelente , sigamos con el programa ...")   
    alturas = altura_usuario()
    pesousu = peso_usuario()
    años = edad_usuario()
    sexos = sexo_usuario()
    calculo = metabolismo_basal(sexos, alturas, pesousu, años)
    print("Sus calorias ingeridas para un dia serian :", calculo, "kcal")
    
   

def dieta() :
    print("¿te gustaria hacer algun tipo de dieta? ")
    dieta = input("si o no ")
    if dieta == "si":
        print("¿que quieres conseguir con tu dieta? ")
        volumen = input("volumen,bajar de peso,definicion.")
        if volumen == "volumen" :
         print ("""Para aumentar el volumen muscular, es fundamental seguir una dieta hipercalórica, rica en proteínas, carbohidratos y grasas saludables, junto con un entrenamiento adecuado. Aquí tienes un plan general de dieta que puedes adaptar según tus necesidades y preferencias.""")
         return volumen
        elif volumen == "bajar de peso" :
          print (texto_dieta)
           
        elif volumen == "definicion" :
         print (texto_definicion)

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







if __name__ == "__main__":
    interfaz()
    main()
    dieta()
    ingresar_objetivo()
    sugerir_rutinas()
    
    
