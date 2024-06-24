from TEMALDIGONIF import * 

banMenu = True
while banMenu:
    menu()
    opc = int(input("INgrese opc\n"))
    if opc == 1:
        registrar_personitas()
    elif opc == 2:
        buscar_personita()
    elif opc == 3:
        imp_certificados()
    else:
        print("Intente de nuevo!\n")