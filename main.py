
#1ER PANTALLA: MENU PRINCIPAL
#2d PANTALLA: iNICIO SESION
#3ERA PANTALLA: mENU SECUNDARIO
#4TA PANTALLA: INGRESO DATOS PERSONALES/ CALCULO CALORIAS 
# 5TA PANTALLA: CALENDARIO  
# 6TA PANTALLA: INVENTARIO

import os
import modulo_funciones.core as f


def main(): 
    os.system("cls")
    f.intro()
    f.menu_principal()
    

if __name__=="__main__":
    main()
