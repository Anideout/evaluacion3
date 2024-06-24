from os import system, name
import time
import random
contador_nif=1
habitantes = []
def menu():
    print("\tMenu principal!")
    print("1. Registro de ciudadano")
    print("2.Buscar persona")
    print("3.Imprimir certificado")
    print("4.Salir\n")

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def salir():
    print("Usted ha salido del sistema....")
    print("Matias Borquez\nHecho en VSCodium... python3.11.9.64")

def obt_city():
    clear()
    
    while True:
        nacion = (input("Indique si pertenece a la ciudad de (madrid, barcelona, sevilla). Si pertenece a otra ciudad por favor escriba (otro) \n")).lower()
        if nacion == "madrid":
            print("Registrado con exito!")
            id_city = 'MAD' 
            break
        elif nacion == "barcelona":
            print("Registrado con exito!")
            id_city = 'BAR'
            break
        elif nacion == "sevilla":
            print("Registrado con exito!")
            id_city = 'SEV'
            break
        elif nacion == "otro":
            print("Registrado con exito!")
            id_city = 'XXX'
            break
        else:
            print("Por favor, indique su ciudad , si su ciudad natal no es 'Barcelona, Madrid o Sevilla' por favor escriba (otro)\n")
    return id_city
    

def obt_nif():
    clear()

    while True:
        try:
            nif = int(input("INgrese su NIF (solo 8 digitos)\n"))
            if len(str(nif)) == 8:
                print("NIF registrado con exito!\n")
                id_city = obt_city()
                nif_final = str(nif) + id_city
                break
            else:
                print("Por favor ingrese su nif bien \n")
        except:
            print("Intente de nuevo por favor\n ")
    return nif_final
            

def obt_nombre():
    clear()
    while True:
        nombre = input("Ingrese nombre y apellido por favor!\n")
        if nombre !="" and nombre!=" " and not "  " in nombre:
            if len(nombre)>=8:
                break
            else:
                print("Por favor indique bien su nombre y apellido! no puede contener menos de 8 caracteres ")
        
        else:
            print("Nombre no puede estar vacio\n")
    return nombre

def obt_nacionalidad():
    while True:
        nacionalidad = input("Por favor indique su nacionalidad!\n")
        if nacionalidad != "" and nacionalidad != " " and not "  " in nacionalidad:
            print("Su nacionalidad ha sido registrada con exito!\n")
            break
        else:
            print("Por favor vuelva a indicar su nacionalidad! no puede quedar el espacio en vacio...\n")

    return nacionalidad

def obt_edad():
    while True:
        try:
            edad = int(input("Ingrese su edad por favor!\n"))
            if edad>=15:
                print("Edad registrada con exito!")
                break
            else:
                print("Usted debe ser mayor de 15 años para poder continuar!\n")
        except:
            print("Para ingresar edad solo debe ingresar numeros")
    return edad

def registrar_persona():
    contador = 1 
    while True:
        nif = obt_nif()
        ciudad = obt_city()
        contador += 1 
        nombre = obt_nombre()
        nacionalidad = obt_nacionalidad()
        edad = obt_edad()
        dia = random.randint(1,30)
        mes = random.randint(1, 2)
        año = 2024 - edad
        nacimiento =  f"{dia}" + "/" f"{mes}" + "/" + f"{año}"
        estado = random.randint(1, 2)
        sueldo = random.randint(100000, 2000000)
        habitante=[nif, nombre, edad, nacionalidad,ciudad, nacimiento, estado, sueldo]
        habitantes.append(habitante)
        print(habitantes)
        agregar = input("Desea agregar otro estudiante? 1.SI2.NO\n")
        if agregar == 1:
            continue
        elif agregar == 2:
            break
        else:
            print("porfavor indique una de las 2 opciones\n")
            #no entiendo pq  no rompe el bucle u.uuuu 




def buscar_persona():
    nif_buscar = input("INgrese nif de la persona!\n")
    for habitante in habitantes:
        if habitante[0] == nif_buscar:
            print(f"NIF: {habitante[0]}")
            print(f"NOMBRE: {habitante[1]}")
            print(f"EDAD: {habitante[2]}")
            print(f"NACIONALIDAD {habitante[3]}\n")



def imprimir_certificados():
    while True:
        print("\tMenu para imprimir certificados!")
        print("1. Certificado de nacimiento! ")
        print("3. Certificado de  Estado conyugal")
        print("4. Certificado!  de salario mensual")
        opc2 = input("Ingrese opcion!\n")
        if opc2 == "1":
            nif_buscar = input("Ingrese NIF de la persona por favor!")
            for habitante in habitantes:
                if habitante[0] == nif_buscar:
                    print("---------------------------")
                    print("\tCertificado de Nacimiento!")
                    print(f"NIF {habitante[0]}")
                    print(f"NOMBRE {habitante[1]}")
                    print(f"EDAD: {habitante[2]}")
                    print(f"NACIONALIDAD {habitante[3]}")
                    print(f"NACIMIENTO {habitante[5]}")
        elif opc2 == "2":
            nif_buscar = input("Ingrese NIF de la persona por favor!")
            for habitante in habitantes:
                if habitante[0] == nif_buscar:
                    if nif_buscar < 2:
                        print("---------------------------")
                        print("\tCertificado de estado conyugal!")
                        print(f"NIF {habitante[0]}")
                        print(f"NOMBRE {habitante[1]}")
                        print(f"EDAD: {habitante[2]}")
                        print(f"NACIONALIDAD {habitante[3]}")
                        print(f"ESTADO: CASADO")
                    elif nif_buscar < 2:
                        print("---------------------------")
                        print("\tCertificado de estado conyugal!")
                        print(f"NIF {habitante[0]}")
                        print(f"NOMBRE {habitante[1]}")
                        print(f"EDAD: {habitante[2]}")
                        print(f"NACIONALIDAD {habitante[3]}")
                        print(f"ESTADO: SOLTERO")

        elif opc2 == "3":
            nif_buscar = input("Ingrese NIF de la persona por favor!")
            for habitante in habitantes:
                if habitante[0] == nif_buscar:
                    print("---------------------------")
                    print("\tCertificado de Salario mensual!")
                    print(f"NIF {habitante[0]}")
                    print(f"NOMBRE {habitante[1]}")
                    print(f"EDAD: {habitante[2]}")
                    print(f"NACIONALIDAD {habitante[3]}")
                    print(f"SALARIO MENSUAL {habitante[7]}")

