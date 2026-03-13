
while True:
    try:
        question = int(input("input the age:  "))
        
        if question >= 0 and question < 13  :
            print("no puede ingresar")
        
        elif question >= 13 and question <= 18:
            print("clase juvenil")
        
        elif question >= 18 and question <= 59:
            print("clase general")
        
        elif question < 0 :
            print("no puede ser un valor negativo, intentelo de nuevo")
            continue
        
        else:
            print("clase senior")
        
        break
    
    except ValueError:
        print("Error al ingresar los datos")
