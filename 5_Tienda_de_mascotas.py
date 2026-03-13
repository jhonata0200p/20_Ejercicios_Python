
try: 
    mascota = input("Escribe el tipo de mascota: perro, gato, conejo  ")
    if mascota == "perro":
        print("Debes darle crocretas de la maxima calidat!!!")
    
    elif mascota == "gato":
        print("Debes darlo atun de la maxima calidat!!!")
    
    elif mascota == "conejo":
        print("Debes darle zanahoria, lechuga o alguna verdura y que entrene pesado y al fallo")
    
    else:
        print("escribe una de las 3 opciones")

except ValueError:
    print("datos invalidos")