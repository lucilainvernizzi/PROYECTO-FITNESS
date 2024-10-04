import core as f

def interfaz():
    f.menu()

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
        return #texto_volumen#
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

