cafe = 4000
te = 3500
jugo = 5000



while True:
    
    try:
        
        question = int(input("Escoge una bebida: 1.cafe , 2.te, 3.jugo  "))

        quantity = int(input("Escribe la cantidad:  "))
        
        if question == 1 :
            
            result = cafe * quantity

        elif question == 2 :
            
            result = te * quantity

        elif question == 3 :
            
            result = jugo * quantity
        
        else :
            print("Por favor escoger una opcion del 1 al 3")
            continue
            
    except ValueError :
        print("Error al ingresar los datos, intentelo nuevamente")
        continue
    
    break


print(f"El total es {result}")