def registroDiario():
    CP = int(input("Ingresar el número de código de pieza: "))
    PiezasPro = 0
    PrT = 0 
    while CP != 0:
        if CP >= 1 and CP <= 99:
            PiezasPro = PiezasPro + 1
            CC = int(input("\nIngresar el número de código de componente: "))
            while CC != 0:
                if CC > 1 and CC <= 9999 and CC%100 == CP:
                    print("\nEl número de código ingresado es: ",CC)
                    while True:
                        PrC =float(input("\nIngresar el precio del componente en $: "))
                        if PrC >= 10.00 and PrC <= 999.99:
                            print("\nEl precio es válido, puede continuar")
                            PrT = PrT + PrC
                            break
                        else :
                            print("El precio ingresado es inválido")
                else :
                    print("El número de código de componente no es válido")
                CC = int(input("\nIngresar el nuevo número de código de componente: "))
            print("\nLa suma total de los componentes ingresados para esta pieza es de $",PrT)        
        else :
            print("El número de código de pieza no es válido")
        Prt = 0
        CP = int(input("\nIngresar el nuevo número de código de pieza: "))

    print("\n\nLa cantidad de piezas procesadas es de: ",PiezasPro) 
    return 0