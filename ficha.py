def ficha():
 
    nombre_completo = input("Ingrese su nombre completo: ").strip().title()
  
    email = input("Ingrese su email: ")
    email = email.lower() 

    caracteres = len(nombre_completo) 

    espacio = nombre_completo.find(" ")
    iniciales = nombre_completo[0] + nombre_completo[espacio + 1]

    usuario = nombre_completo.lower()[espacio+1:] + "." + nombre_completo.lower()[:espacio]

    email_valido = "@" in email
    arroba = email.find("@")
    dominio = email[arroba+1:] 

    nombre_archivo = nombre_completo.replace(" ","_")

    cantidad_a = nombre_completo.lower().count("a")

    nombre_invertido = nombre_completo[::-1].upper()

    nota1 = int(input("Ingrese nota 1: "))
    nota2 = int(input("Ingrese nota 2: "))
    nota3 = int(input("Ingrese nota 3: "))

    suma = nota1 + nota2 + nota3 
    promedio = suma / 3
    promedio_entero = suma // 3


    print("========================") 
    print("    FICHA DEL ALUMNO")
    print("========================") 
    print(f"Nombre: {nombre_completo}") 
    print(f"Email: {email}")
    print(f"Caracteres en nombre: {caracteres}")
    print(f"Iniciales: {iniciales}")
    print(f"Usuario: {usuario}")
    print(f"Email valido: {email_valido}")
    print(f"Dominio: {dominio}")
    print(f"Nombre para archivo: {nombre_archivo}")
    print(f"Cantidad de a: {cantidad_a}")
    print(f"Codigo secreto: {nombre_invertido}")
    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")
    print(f"Suma: {suma}")
    print(f"Promedio: {promedio}")
    print(f"Promedio entero: {promedio_entero}")
    print("========================")



