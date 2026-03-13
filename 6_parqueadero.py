hours = int(input("¿cuantas horas estuvo tu carro en el parqueadero?  "))
one_hour = 5000
extra_hour = 3000


if hours == 1:
    total = one_hour

else : 
    total = one_hour + ((hours - 1) * extra_hour)
    print(f"el total a pagar es {total}")