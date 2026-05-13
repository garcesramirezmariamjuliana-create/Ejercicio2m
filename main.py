print("Hola bienvenido al cajero automatico")

#este progragra simula un cajero automatico 

sal = 1000  #saldo
opc = 0  #opcion

while opc != 4:
    print("MENÚ DEL CAJERO")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")

    opc = int(input("Selecciona una opción: "))

    if opc == 1:
        print("Tu saldo actual es:", sal)

    elif opc == 2:
        deposito = float(input("Ingresa la cantidad de dinero que deseas depositar: "))
        
        if deposito > 0:
            sal += deposito
            print("TU depósito fue realizado correctamente.")
        else:
            print("dinero inválido.")

    elif opc== 3:
        retiro = float(input("Ingresa la cantidad de dinero que deseas retirar: "))

        if retiro > sal:
            print("Fondos insuficientes.")
        elif retiro <= 0:
            print("dinero inválido.")
        else:
            sal -= retiro
            print("Tu retiro fue realizado correctamente.")