import getpass



mensaje = getpass.getpass("Ingrese la contraseña: ")
cuentas = 0

while mensaje != "ingrith":
    cuentas = cuentas + 1

    if cuentas <= 2:

        print ("constraseña incorrecta intente de nuevo")
        mensaje = getpass.getpass("Ingrese la contraseña: ")
    
    else: 
        print("maximo numero de intentos")
        break   

if mensaje == "ingrith":   
    print("contraseña correcta")









