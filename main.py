import modulo_funciones.core as f

def main():
    f.menu()

texto_dieta ="""Para bajar de peso, es importante seguir una dieta hipocalórica, equilibrada y rica en nutrientes para asegurarte de perder grasa corporal mientras mantienes la masa muscular. Aquí tienes un plan de alimentación general que puedes adaptar según tus necesidades."""
texto_definicion = """"Una dieta de definición se centra en reducir el porcentaje de grasa corporal mientras se mantiene la masa muscular. Es similar a una dieta de pérdida de peso, pero con un enfoque especial en preservar el músculo. Aquí tienes un plan de alimentación para ayudarte a lograrlo."""


def altura_usuario():
    alturas = int(input("Por favor, ingrese su altura en cm: "))
    return alturas

def peso_usuario():
    pesousu = int(input("Ingrese su peso en KG: "))
    return pesousu

def edad_usuario():
    años = int(input("Ingrese su edad: "))
    return años

def genero_usuario():
    generos = input("¿Cuál es su género? (H/M): ")
    if generos.upper() == "H":
        return "H"
    elif generos.upper() == "M":
        return "M"
    else:
        print("Género no válido. Por favor, ingrese H o M. ")
        return genero_usuario()

h = 88.36
m = 447.6

def peso_ideal(genero, altura, peso, edad):
    if genero == "H":
        return 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * edad)
    elif genero == "M":
        return 447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * edad)

def main():
    print("Hola, bienvenido al programa de ")
    alturas = altura_usuario()
    pesousu = peso_usuario()
    años = edad_usuario()
    generos = genero_usuario()
    calculo = peso_ideal(generos, alturas, pesousu, años)
    print("Sus calorias ingeridas para un dia serian : ", calculo, "kcal")
    dieta_seleccionada = dieta()
    if dieta_seleccionada == "volumen":
        pass
    elif dieta_seleccionada == "bajar de peso":
        return texto_dieta
    elif dieta_seleccionada == "definicion":
        pass

def dieta() :
    print("¿te gustaria hacer algun tipo de dieta ?")
    dieta = input("si o no")
    if dieta == "si":
        print("¿que quieres conseguir con tu dieta? ")
        volumen = input("volumen,bajar de peso,definicion.")
        if volumen == "volumen" :
         print ("""Para aumentar el volumen muscular, es fundamental seguir una dieta hipercalórica, rica en proteínas, carbohidratos y grasas saludables, junto con un entrenamiento adecuado. Aquí tienes un plan general de dieta que puedes adaptar según tus necesidades y preferencias.""")
         return volumen
        elif volumen == "bajar de peso : ":
          print(texto_dieta)
          return texto_dieta   
        elif volumen == "definicion : " :
         print(texto_definicion)
        return texto_definicion

main()
dieta()

if __name__ == "__main__":
    main()