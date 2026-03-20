def change():
    print("Ingresar gasto:")
    gasto = float(input())

    print(gasto)

    print("Dinero recibido")
    dinero = float(input())

    print(int(dinero) if dinero.is_integer() else dinero)

    print()
    print("Vuelto")
    print()

    vuelto = dinero - gasto

    pesos = int(vuelto)
    centavos = int(round((vuelto - pesos) * 100))

    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)    

    

   
   
