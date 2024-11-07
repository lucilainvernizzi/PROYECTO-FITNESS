def es_bisiesto(año):
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

def dias_en_mes(mes, año):
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mes in [4, 6, 9, 11]:
        return 30
    elif mes == 2:
        return 29 if es_bisiesto(año) else 28
    else:
        return 0  # Mes no válido

def dia_de_la_semana(dia, mes, año):
    if mes < 3:
        mes += 12
        año -= 1
    k = año % 100
    j = año // 100
    # Fórmula de Zeller
    return (dia + (13 * (mes + 1)) // 5 + k + (k // 4) + (j // 4) + (5 * j)) % 7

def mostrar_calendario(mes, año):
    dias = dias_en_mes(mes, año)
    dia_inicio = dia_de_la_semana(1, mes, año)

    # Imprimir encabezado
    print("Lunes    Martes   Miércoles Jueves   Viernes  Sábado   Domingo")
    print("-" * 60)

    # Imprimir espacios hasta el primer día
    espacios_iniciales = "    " * dia_inicio
    print(espacios_iniciales, end='')

    # Imprimir los días del mes
    for dia in range(1, dias + 1):
        print(f"[{dia:>2}]", end=' ')
        if (dia + dia_inicio) % 7 == 0:
            print()  # Nueva línea al final de la semana

    # Imprimir espacios vacíos para completar la tabla
    for dia in range(dias + 1, 16):
        print("[  ]", end=' ')
        if (dia + dia_inicio) % 7 == 0:
            print()  

    print() 


año = int(input("Introduce el año (por ejemplo, 2023): "))
mes = int(input("Introduce el mes (1-12): "))


mostrar_calendario(mes, año)