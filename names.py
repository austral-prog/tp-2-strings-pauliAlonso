def names():
    nombre = input("Ingrese su nombre:")
    apellido = input("Ingrese su apellido:")

    nombre_completo = nombre + " " + apellido 

    print(nombre_completo.lower())
    print(nombre_completo.title())
    print(nombre_completo.upper())
    print(f"\t{nombre_completo.lower()}") 

 
