question = int(input("Enter the number of attendees"))

try:
    if question < 5:
        print("Low attendance")
    
    elif question in range(5,8):
        print("Medium attendance")
        
    else:
        print("high attendance")
        
except ValueError:
    print("Error en el ingreso de datos")