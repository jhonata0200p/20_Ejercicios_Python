vainilla = 0
chocolate = 0
fresa = 0

i=0

while i < 5:
        try:
            question = int(input("que sabor escoges: 1.Vainilla , 2.Chocolate, 3.Fresa  "))
            
            if question == 1:
                vainilla += 1
               
                
            elif question == 2:
                chocolate += 1
               
                
            elif question == 3:
                fresa += 1
                
            
            else:
                print("escoge solamente 1.Vainilla , 2.Chocolate, 3.Fresa")
                continue
            
            i += 1
        except ValueError:
            print("valor incorrecto intentalo nuevamente")
        
print(f"se escogio Vainilla {vainilla} veces / Chocolate {chocolate} veces / Fresa {fresa} veces")
        
        