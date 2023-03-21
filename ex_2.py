lista = []
numero = 0

while True:

    accion = input("ingrese que accion quiere hacer, agregar, editar, mostrar, eliminar o exit: ")
    accion = accion.strip()
    

    match accion:
        case "agregar":
            nombre = input("ingrese el nombre: ")
            lista.append(nombre)
            
            

        case "mostrar" | "display" | "show":
            for index, item in enumerate(lista):
                row = f"{index + 1}. {item}"
                print(row)
                
                

        case "editar":
            campo = int(input("ingrese el numero de la lista que desea editar: "))
            campo = campo - 1
            nombre_nuevo = input ("ingrese la edicion: ")
            lista[campo] = nombre_nuevo
            
        case "eliminar":
            eliminar = int(input("ingrese el numero a eliminar: "))
            lista.pop(eliminar)

        case "exit":
            break

        case _:
            print("comando desconocido")

print ("good bye adios")
    
