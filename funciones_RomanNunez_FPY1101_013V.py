libros=[]
l_prestados=[]

def registrar_libro():
    titulo=input("Ingrese el titulo del libro: ").upper().strip()
    autor=input("Ingrese el autor del libro: ").upper().strip()
    año=int(input("Ingrese el año de publicación: "))
    sku=input("Ingrese el SKU: ").upper().strip()

    if titulo == "" or autor=="" or año <=0 or año =="" or sku=="":
        print("Faltan datos por ingresar. Saldrá al menú principal.")
        print("")
        return

    libro={"Titulo": (titulo),
        "Autor": (autor),
        "Año": (año),
        "SKU": (sku),
        }
    
    libros.append(libro)

    print("Libro registrado correctamente.\n""")

def prestar_libro():
    usuario=input("Ingrese su nombre de usuario: ").upper().strip()
    sku=input("Ingrese el SKU del libro que desea pedir: ").upper().strip()
    
    if sku is libros["SKU":(sku)]:
        print("Si existe el libro.")
        if sku in l_prestados:
            print("Lo sentimos, el libro ya fue prestado.")
        else:
            fecha=("Ingrese la fecha de solicitud del prestamo separado por espacios(25 06 2024)").replace('','-')
            print("Puedes pasar a retirar tu libro.")
                
            libro_prestado={"Usuario": (usuario),
                            "Titulo": (autor),
                            "Fecha del prestamo": (fecha),
                            "SKU": (sku),
                            }
            l_prestados.append(libro_prestado)

def listar_libro():
    if not libros:
        print("No se han registrado libros.")
        return
    
    print("La lista de los libros es: ")
    print("TITULO\t\t\tAUTOR\t\tAÑO\t\tSKU")
    for i, libro in enumerate(libros,start=1):
        print(f"{libro['Titulo']}\t\t\t{libro['Autor']}\t\t{libro['Año']}\t\t{libro['SKU']}")

def reportes():
    libros_a_imprimir=l_prestados
    nombre_archivo="libros_prestados.txt"

    try:
        with open(nombre_archivo,'w') as archivo:
            archivo.write("LIBROS PRESTADOS: \n")
            for lib in libros_a_imprimir:
                linea=f"Usuario:{lib['Usuario']} Titulo: {lib['TITULO']} Fecha de prestamo: {lib['FECHA DEL PRESTAMO']}"
                archivo.write(linea)
                print("La lista de libros prestados se imprimió correctamente.")
                print("")
    except IOError as error:
        print(f"Error{error}: El archivo no se puede leer.")

def menu():
    while True:
        try:
            print("Bienvenid@ a Biblioteca DUOC UC.")
            print("****MENÚ****")
            op=int(input("Elija la opción deseada:\n1. Registrar libro\n2. Prestar libro\n3. Listar todos los libros\n4. Imprimir reporte de prestamos\n5. Salir del programa\nOpcion: "))
            if op==1:
                registrar_libro()
            elif op==2:
                prestar_libro()
            elif op==3:
                listar_libro()
            elif op==4:
                reportes()
            elif op==5:
                print("Programa finalizado...\nDesarrollado por Román Núñez\nRUN: 17.850.899-7")
                break
            else:
                print("Opción no valida. Intentelo nuevamente.")
        except ValueError:
            print("Error: Solo debe utilizar números.")