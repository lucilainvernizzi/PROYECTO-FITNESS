import calendar

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
        return 0  

def dia_de_la_semana(dia, mes, año):
    if mes < 3:
        mes += 12
        año -= 1
    k = año % 100
    j = año // 100
    
    return (dia + (13 * (mes + 1)) // 5 + k + (k // 4) + (j // 4) + (5 * j)) % 7

def mostrar_calendario(mes, año):
    cant_dias = dias_en_mes(mes, año)
    dia_inicio = dia_de_la_semana(1, mes, año)
    dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

    for dia in dias:
        print(dia, end='       ')
    print("\n" + "-" * 60)

  
    columnas = [[] for _ in range(7)] 

    for dia in range(1, cant_dias + 1):
        columna_index = (dia + dia_inicio - 1) % 7
        columnas[columna_index].append(f"[{dia:>2}]")


    max_semanas = max(len(col) for col in columnas)  

    for i in range(max_semanas):
        for j in range(7):
            if i < len(columnas[j]):
                print(columnas[j][i], end='    ')
            else:
                print("[  ]", end='    ')
        print() 

año = int(input("Introduce el año (por ejemplo, 2023): "))
mes = int(input("Introduce el mes (1-12): "))

mostrar_calendario(mes, año)