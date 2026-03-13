cone = 3000
glass = 4000 
banana_split = 9000

count_cone = 0
count_glass = 0
count_banana_split = 0
client = 0



continu = "s"

while continu == "s" :
    print("choose a product (1-3)")
    print("1. cone")
    print("2. glass")
    print("3. banana split")
    
    product = int(input(""))
    print("Enter de quantity:")
    quantity = int(input())
    
    if product == 1 :
        total = quantity * cone
        count_cone += 1
    
    elif product == 2:
        total = quantity * glass
        count_glass += 1
        
    elif product == 3:
        total = quantity * banana_split
        count_banana_split += 1
    
    else:
        print("product does not exist")
    
    client += 1
    
    print("")
    
    
        