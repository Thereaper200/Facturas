from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.t1_brandon

coleccion = db.Prueba

while True:

    print('''
    Elige una opcion:
    1)Factura
    2)Salir
    ''')

    oper = input("Movimiento: ")

    if oper in ["1"]:

        factura = input("Nombre de la factura: ")

        while True:
            print('''
            1)iPad 12.9
            2)iPad 11
            3)iPad 10
            4)iPad no especificado
            5)Apple Pencil Gen2
            6)Apple Pencil Gen1
            7)Cambiar Factura
            ''')
            opcion = input("Eleccion: ")

            while True:

                if opcion in ["1"]:
                    print("iPad 12")
                    SN = input("Numero de serie: ")
                    coleccion.insert_one({'factura':factura, 'Product':'iPad Pro 12.9','SerialNumber':SN})
                    print(''' Cambiar Dispositivo
                    1) Si
                    2) No
                    ''')
                    s1 = input("Cambiar dispositivo?: ")
                    if s1 in ["1"]:
                        break
                    elif s1 in ["2"]:
                        print("OK")

                elif opcion in ["2"]:
                    print("iPad 11")
                    SN = input("Numero de serie: ")
                    coleccion.insert_one({'factura':factura, 'Product':'iPad Pro 11','SerialNumber':SN})
                    print('''
                    1) Si
                    2) no
                    ''')
                    s1 = input("Cambiar dispositivo?: ")
                    if s1 in ["1"]:
                        break
                    elif s1 in ["2"]:
                        print("OK")

                elif opcion in ["3"]:
                    print("iPad 10")
                    SN = input("Numero de serie: ")
                    coleccion.insert_one({'factura':factura, 'Product':'iPad Pro 10','SerialNumber':SN})
                    print('''
                    1) Si
                    2) no
                    ''')
                    s1 = input("Cambiar dispositivo?: ")
                    if s1 in ["1"]:
                        break
                    elif s1 in ["2"]:
                        print("OK")

                elif opcion in ["4"]:
                    print("iPad sin especificar")
                    SN = input("Numero de serie: ")
                    coleccion.insert_one({'factura':factura, 'Product':'iPad Pro','SerialNumber':SN})
                    print('''
                    1) Si
                    2) no
                    ''')
                    s1 = input("Cambiar dispositivo?: ")
                    if s1 in ["1"]:
                        break
                    elif s1 in ["2"]:
                        print("OK")

                    elif opcion in ["5"]:
                        print("Apple Pencil 2")
                        SN = input("Numero de serie: ")
                        coleccion.insert_one({'factura':factura, 'Product':'Apple Pencil Gen2','SerialNumber':SN})
                        print('''
                        1) Si
                        2) no
                        ''')
                        s1 = input("Cambiar dispositivo?: ")
                        if s1 in ["1"]:
                            break
                        elif s1 in ["2"]:
                            print("OK")

                elif opcion in ["6"]:
                    print("Apple Pencil 1")
                    SN = input("Numero de serie: ")
                    coleccion.insert_one({'factura':factura, 'Product':'Apple Pencil Gen1','SerialNumber':SN})
                    print('''
                    1) Si
                    2) no
                    ''')
                    s1 = input("Cambiar dispositivo?: ")
                    if s1 in ["1"]:
                        break
                    elif s1 in ["2"]:
                        print("OK")

                elif opcion in ["7"]:
                    break

                else:
                    print("Comando desconocido")
            if opcion in ["7"]:
                break
    elif oper in ["2"]:
        break
