import random
from os import system, name
import time
contador_id =1 
personitas = []
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def menu():
    print("menu")
    print("1.Registrar Usuario ")
    print("2.Buscar Usuario")
    print("3.Certificados!")
    print("4.Salir")

def salir():
    print("Usted ha salido del sistema....")
    print("""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠁⠸⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃⠀⠀⢸⠸⠀⡠⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠃⠀⠀⢠⣞⣀⡿⠀⠀⣧⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡖⠁⠀⠀⠀⢸⠈⢈⡇⠀⢀⡏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠩⢠⡴⠀⠀⠀⠀⠀⠈⡶⠉⠀⠀⡸⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⠎⢠⣇⠏⠀⠀⠀⠀⠀⠀⠀⠁⠀⢀⠄⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⠏⠀⢸⣿⣴⠀⠀⠀⠀⠀⠀⣆⣀⢾⢟⠴⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣿⠀⠠⣄⠸⢹⣦⠀⠀⡄⠀⠀⢋⡟⠀⠀⠁⣇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡾⠁⢠⠀⣿⠃⠘⢹⣦⢠⣼⠀⠀⠉⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀
⠀⠀⢀⣴⠫⠤⣶⣿⢀⡏⠀⠀⠘⢸⡟⠋⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀⠀⠀⠀
⠐⠿⢿⣿⣤⣴⣿⣣⢾⡄⠀⠀⠀⠀⠳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀
⠀⠀⠀⣨⣟⡍⠉⠚⠹⣇⡄⠀⠀⠀⠀⠀⠀⠀⠀⠈⢦⠀⠀⢀⡀⣾⡇⠀⠀
⠀⠀⢠⠟⣹⣧⠃⠀⠀⢿⢻⡀⢄⠀⠀⠀⠀⠐⣦⡀⣸⣆⠀⣾⣧⣯⢻⠀⠀
⠀⠀⠘⣰⣿⣿⡄⡆⠀⠀⠀⠳⣼⢦⡘⣄⠀⠀⡟⡷⠃⠘⢶⣿⡎⠻⣆⠀⠀
⠀⠀⠀⡟⡿⢿⡿⠀⠀⠀⠀⠀⠙⠀⠻⢯⢷⣼⠁⠁⠀⠀⠀⠙⢿⡄⡈⢆⠀
⠀⠀⠀⠀⡇⣿⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠦⠀⠀⠀⠀⠀⠀⡇⢹⢿⡀
⠀⠀⠀⠀⠁⠛⠓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠼⠇⠁
    """)

def obt_ciudad():
    clear()
    while True:
        ciudad = input("Ingrese bien su ciudad por favor!\n ").lower()
        if ciudad == "madrid":
            ciudad_id = '-MD'
            break
        elif ciudad == 'barcelona':
            ciudad_id = '-BC'
            break
        elif ciudad == "sevilla":
            ciudad_id = '-SV'
            break
        else:
            print("malo")
    return ciudad_id


def obt_nif():
    clear()
    while True:
        try:
            nif = int(input("Ingrese su NIF (solo 8 digitos)\n"))
            if len(str(nif)) == 8:
                print("NIF registrado con exito!\n")
                break
            else:
                print("El nif ingresado no esta dentro de los parametros solicitados")
        except:
            print("Debe dar un numero entero")
    return nif

def obt_nombre():
    clear()
    nombre = input("Ingrese nombre\n").lower()
    while len(nombre) < 8 or nombre == "" or nombre == " ":
        nombre = input("Ingresa un nombre nuevamente!\n")
    return nombre

def obt_edad():
    clear()
    while True:
        edad = int(input("INgrese su edad\n"))
        if edad >= 15:
            print("bien hecho!")
            break
        else:
            print("mal hecho!")
    return edad


def buscar_personita():
    clear()
    nif_buscar = input("Ingrese nif de la personita por favor!\n").upper()
    print("persona encontrada!", nif_buscar)
    for personita in personitas:
        if personita[0] == nif_buscar:
            print("\tPersona encontrada!")
            print("-------------------------")
            print(f"NIF: {personita[0]}")
            print(f"NOMBRE: {personita[1]}")
            print(f"EDAD: {personita[2]}")
            print(f"NACIONALIDAD {personita[3]}")
            print("-------------------------")
            
        else:
            print("nif no encontrado!")
        input("enter para salir!")


def obt_nacionalidad():
    clear()
    nacionalidad = input("Ingrese su nacionalidad por favor!\n")
    while not nacionalidad:
        nacionalidad = input("Ingrese su nacionalidad por favor!")

def registrar_personitas():
    clear()
    print("Bienvenido al registro de españa")
    while True:
        nif_personita = obt_nif()
        ciudad = obt_ciudad()
        nombre = obt_nombre()
        edad = obt_edad()
        dia = random.randint(1, 30)
        mes = random.randint(1, 12)
        estado = random.randint(1, 2)
        salario = random.randint(150000, 1000000)
        año = 2024 - edad
        nif_persona = f"{nif_personita}" + f"{ciudad}"
        nacimiento = f"{dia}" + "/" f"{mes}" + "/" + f"{año}"
        personita = [nif_persona, nombre, edad, nacimiento, estado, salario]
        personitas.append(personita)
        print(personita)
        agregar = int(input("Desea agregar otra persona? \n1.SI\n2.NO\n"))
        if agregar == 1:
            continue
        elif agregar == 2:
            break
        else:
            print("wuajaj")




def imp_certificados():
    while True:
        print("\tMenu para imprimir certificados!")
        print("Certificado de nacimiento")
        print("Certificado de estado conyugal")
        print("Certificado de Salario mensual uwu ")
        try:
            opc2 = int(input("INgrese opcion para continuar!\n"))
            if opc2 == 1:
                print("Certificado de nacimiento!\n")
                buscar_nif = input("Ingrese el nif para buscar certificados\n")
                for personita in personitas:
                    if personita[0] == buscar_nif:
                        print("-------------------------")
                        print("\tCertificado de nacimiento!")
                        print(f"NIF: {personita[0]}")
                        print(f"NOMBRE: {personita[1]}")
                        print(f"EDAD: {personita[2]}")
                        print(f"Nacimient: {personita[3]}")
                        print("-------------------------")
                        input("ENter para continuar.... \n")
                        
            

            elif opc2 == 2:

                print("certificado de conyugal")
                buscar_nif = input("Ingrese el nif para buscar certificados\n")
                for personita in personitas:
                    if personita[0] == buscar_nif:
                        if personita[4] == 1:

                            print("-------------------------")
                            print("\tCertificado de conyugal!")
                            print(f"NIF: {personita[0]}")
                            print(f"NOMBRE: {personita[1]}")
                            print(f"EDAD: {personita[2]}")
                            print("ESTADO: CASADO")
                            print("-------------------------")
                            input("ENter para continuar.... \n")
                        elif personita[4] == 2:

                            print("-------------------------")
                            print("\tCertificado de conyugal!")
                            print(f"NIF: {personita[0]}")
                            print(f"NOMBRE: {personita[1]}")
                            print(f"EDAD: {personita[2]}")
                            print("ESTADO: SOLTERO")
                            print("-------------------------")
                            input("ENter para continuar.... \n")
            elif opc2 == 3:
                print("certificado de sueldo mensual!")
                buscar_nif = input("Ingrese el nif de la persona!\n")
                for personita in personitas:
                    if personita[0] == buscar_nif:
                            print("-------------------------")
                            print("\tCertificado de sueldo mensual!")
                            print(f"NIF: {personita[0]}")
                            print(f"NOMBRE: {personita[1]}")
                            print(f"EDAD: {personita[2]}")
                            print(f"SUELDO: ${personita[5]}")
                            print("-------------------------")
                            input("ENter para continuar.... \n")
                            
                
            else:
                print("malmalmal")
        except:
            print("Holas tas mal xd ")
    return buscar_nif
