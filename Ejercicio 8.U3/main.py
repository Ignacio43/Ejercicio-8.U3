from manejador import ManejaPersonal



from ObjectEncoder import ObjectEncoder

if __name__ == "__main__":
    manejador = ManejaPersonal()
    
    jsonF = ObjectEncoder()  
    
    diccionario=jsonF.leerJSONArchivo('personal.json') 
    jsonF.decodificarDiccionario(diccionario, manejador)
    
    print("1.Insertar personal en posición ")
    print("2.Agregar personal ")
    print("3.Dada una posición mostrar tipo de dato ")
    print("4. Ingresa nombre carrera y dar lista ordenada de todos los agentes que son docentes investigadores")
    print("5. Dada un area, contar los agentes docente investigador y los investigadores")
    print("6. Generar listado ordenado por apellido de todos los agentes")
    print("7. Dada una categoría de investigacion listar apellido nombre e importe de todos los docentes investigadores, realizar total de importe extra")
    print("8. Almacena datos en personal.json")
    
    op = int(input("Ingrese opcion: "))
    while op != 0:
        if op == 1:
            elemento = manejador.CreaElemento()
            if elemento != -1:
                
                posicion = int(input("Ingrese posicion a colocar elemento: "))
                manejador.insertarElemento(posicion, elemento)
            else:
                print("No se creo el elemento ")
        elif op == 2:
            elemento = manejador.CreaElemento()
            if elemento != -1:    
                manejador.agregarElemento(elemento)
            else:
                print("No se creo el elemento ")
           
        elif op == 3:
            pos = int(input("Ingrese posicion a ver: "))
            manejador.MostrarElemento(pos)          
        elif op == 4:
            carrera = input("Ingrese nombre de carrera a filtrar: ")      
            manejador.listaOrdenadaNombre(carrera)
        elif op == 5:
            area = input("Ingrese area de investigacion: ")
            manejador.cuentaPorArea(area)
        elif op == 6:
           manejador.ordenaPorApellido()
           manejador.Muestra()
        elif op == 7:             
            cat = input("Ingrese categoria: ")
            manejador.listaPorCat(cat)
        elif op == 8:
            d = manejador.toJSON()
            jsonF.guardarJSONArchivo(d, "personal.json")
        else:
            print("Ingreso opcion incorrecta ")
            
        print("1.Insertar personal en posición ")
        print("2.Agregar personal ")
        print("3.Dada una posición mostrar tipo de dato ")
        print("4. Ingresa nombre carrera y dar lista ordenada de todos los agentes que son docentes investigadores")
        print("5. Dada un area, contar los agentes docente investigador y los investigadores")
        print("6. Generar listado ordenado por apellido de todos los agentes")
        print("7. Dada una categoría de investigacion listar apellido nombre e importe de todos los docentes investigadores, realizar total de importe extra")
        print("8. Almacena datos en personal.json")
        
        op = int(input("Ingrese opcion: "))