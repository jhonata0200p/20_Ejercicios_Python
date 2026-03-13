while True:
    try:
        age = int(input("Ingresa tu edad:  "))
        
        if age >= 0 and age <12:
            print("Debes pagar 8000")

        elif age >= 12 and age <= 59:
            print("Debes pagar 12000")
            
        elif age < 0 :
            print("no puede ser un valor negativo, intentelo de nuevo")
            continue

        else :
            print("Debes pagar 9000")
        break
    
    except ValueError:
        print("Error al ingresar los datos")
        continue