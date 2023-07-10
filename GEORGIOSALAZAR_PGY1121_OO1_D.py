from colorama import Fore,Style
import os

asi = []
asicom = []

asic=set()
esp={}

platinum = 0
gold = 0
valorsilver = 0


valorplatinum = 120000
valorgold = 80000
valorsilver = 50000

menu1="""Creativos.cl
1) Comprar entradas.
2) Mostrar ubicaciones disponibles.
3) Ver listado de asistentes.
4) Mostrar ganancias.
5) Salir.
"""
error="""Error: Ingreso un dato no permitido"""

#1
def dis():
    os.system("cls")
    while True:
        try:
            r=input("Digite el rut\n")
            if (len(r))>=7 and (len(r))<=8:
                break
            else:
                print(Fore.RED+"Error: El rut debe tener 7 a 8 caracteres"+Style.RESET_ALL)
        except:
            input(Fore.RED+error+Style.RESET_ALL)

    os.system("cls")
    while True:
        try:
            n=input("Digite el nombre\n")
            if (len(n))>=4:
                break
            else:
                print(Fore.RED+"Error: El nombre debe contener minimo 4 caracteres"+Style.RESET_ALL)
        except:
            input(Fore.RED+error+Style.RESET_ALL)
    
    os.system("cls")
    while True:
        try:
            ap=input("Digite el apellido\n")
            if (len(ap))>=4:
                break
            else:
                print(Fore.RED+"Error: El apellido debe contener minimo 4 caracteres"+Style.RESET_ALL)
        except:
            input(Fore.RED+error+Style.RESET_ALL)
    
    os.system("cls")
    while True:
        try:
            asi=int(input("Digite cuantas entradas desea comprar.  MAX = 3\n"))
            if asi>=1 and asi<=3:
                break
            elif asi<=4:
                print(Fore.RED+"Error: No puedes comprar mas de 3 entradas"+Style.RESET_ALL)
            else:
                print(Fore.RED+"Error: Solo existen 100 asientos"+Style.RESET_ALL)
        except:
            input(Fore.RED+error+Style.RESET_ALL)

    os.system("cls")
    print(Fore.GREEN+"#########################\n#       ESCENARIO       #\n#########################\n"+Style.RESET_ALL)
    print(Fore.GREEN+"Disponible"+Style.RESET_ALL)
    print(Fore.RED+"Ocupado\n"+Style.RESET_ALL)
    for i in range (1,101):
        cc=str(i).zfill(2)
        if cc in asic:
            print(Fore.RED+cc+Style.RESET_ALL,end=" ")
        else:
            print(Fore.GREEN+cc+Style.RESET_ALL,end=" ")
        if i%10==0:
            print()
            if i%20==0:
                print()
                if i%30==0:
                    print()
                    if i%40==0:
                        print()
                        if i%50==0:
                            print()
                            if i%60==0:
                                print()
                                if i%70==0:
                                    print()
                                    if i%80==0:
                                        print()
                                        if i%90==0:
                                            print()

    for i in range (asi):
        cc=int(input("Digite el asiento\n"))
        if cc>=1 and cc<=100:
            cc=str(cc).zfill(2)
            if cc in asic:
                print(Fore.RED+"Error: El asiento no se encuentra disponible"+Style.RESET_ALL)
            else:
                print(Fore.GREEN+"El asiento fue reservado con exito"+Style.RESET_ALL)
                asic.add(cc)
                esp[cc]={'rut':r,'nombre':n,'apellido':ap,'asiento':cc}
        else:
            input(Fore.RED+"Error solo existen 100 asientos"+Style.RESET_ALL)

#2
def com():
    os.system("cls")
    print(Fore.GREEN+"#########################\n#       ESCENARIO       #\n#########################\n"+Style.RESET_ALL)
    print(Fore.GREEN+"Disponible"+Style.RESET_ALL)
    print(Fore.RED+"Ocupado\n"+Style.RESET_ALL)
    for i in range (1,101):
        cc=str(i).zfill(2)
        if cc in asic:
            print(Fore.RED+cc+Style.RESET_ALL,end=" ")
        else:
            print(Fore.GREEN+cc+Style.RESET_ALL,end=" ")
        if i%10==0:
            print()
            if i%20==0:
                print()
                if i%30==0:
                    print()
                    if i%40==0:
                        print()
                        if i%50==0:
                            print()
                            if i%60==0:
                                print()
                                if i%70==0:
                                    print()
                                    if i%80==0:
                                        print()
                                        if i%90==0:
                                            print()

#3
def can():
    os.system("cls")
    print(Fore.GREEN+"##########################\n#       ASISTENTES       #\n##########################\n"+Style.RESET_ALL)
    for v in esp.values():
        print(v)

#4
def pa():
    os.system("cls")
    
            
while True:
    os.system("cls")
    try:
        op=int(input(menu1))
        if op==1:
            os.system("cls")
            dis()
            input(Fore.GREEN+"\n\nPresione cualquier tecla para continuar\n"+Style.RESET_ALL)
        elif op==2:
            os.system("cls")
            com()
            input(Fore.GREEN+"\n\nPresione cualquier tecla para continuar\n"+Style.RESET_ALL)
        elif op==3:
            os.system("cls")
            can()
            input(Fore.GREEN+"\n\nPresione cualquier tecla para continuar\n"+Style.RESET_ALL)
        elif op==4:
            os.system("cls")
            pa()
            input(Fore.GREEN+"\n\nPresione cualquier tecla para continuar\n"+Style.RESET_ALL)
        elif op==5:
            os.system("cls")
            print(Fore.GREEN+"Georgio Juan Salazar Lira\n10/07/2023"+Style.RESET_ALL)
            input(Fore.GREEN+"\n\nPresione cualquier tecla para continuar\n"+Style.RESET_ALL)
    except:
        input(Fore.RED+error+Style.RESET_ALL)
