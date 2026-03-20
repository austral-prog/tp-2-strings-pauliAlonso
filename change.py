def change():
    print("Ingresar gasto:")
    gasto = float(input())
    print(gasto)

    print("Dinero recibido")
    dinero = float(input())
    print(int(dinero))

    print()
    print("Vuelto")
    print()

    vuelto = dinero - gasto

    pesos = int(vuelto)
    centavos = int((vuelto - pesos) * 100)

    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)

    

   
   
