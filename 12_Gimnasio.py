clients = []

attend_low = 0
attend_medium = 0
attend_high = 0

for i in range (1,6):
    name = input("Enter your name:   ")
    day = int(input("Enter days attended:  "))
    minutes  =int(input("Enter the average number of minutes trained per day:   "))
    
    client = {
    "name" : name,
    "days" : day,
    "average" : minutes
    }
    
    clients.append(client)

for client in clients :
    if client["days"] < 3:
        attend_low += 1
   
    elif client["days"] in range(3,5):
        attend_medium += 1
    
    elif client["days"] > 5:
        attend_high += 1


print(f"low {attend_low}")
print(f"medium {attend_medium}")
print(f"low {attend_high}")
    