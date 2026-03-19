def change():

    gasto = float(input("Ingresar gasto:\n"))
    dinero_recibido = int(input("Dinero recibido:\n"))

    vuelto = dinero_recibido - gasto 

    pesos = int(vuelto) 
    centavos = round(vuelto - pesos ) * 100 
  
    print("Ingresar gasto:")
    print(gasto)
    print("Dinero recibido")
    print(dinero_recibido)

    print(vuelto)

    print("Pesos:")
    print(pesos) 
    print("Centavos:") 
    print(centavos) 
    

    

   
   