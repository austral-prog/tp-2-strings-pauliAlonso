def casting():
   
    precio = int(input("Ingrese el precio: "))

    descuento = float(input("Ingrese el descuento: ")) 
    
    cantidad = int(input("Cuantos productos compro: "))

    precio_con_descuento = precio - descuento 

    total = precio_con_descuento * cantidad 

    print(f"Precio: {precio}") 
    print(f"Descuento: {descuento}") 
    print(f"Precio con descuento: {precio_con_descuento}") 
    print(f"Total: {total}")  




