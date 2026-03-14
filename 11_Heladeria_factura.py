cone = 3000
glass = 4000 
banana_split = 9000

count_cone = 0
count_glass = 0
count_banana_split = 0
clients = 0
total_sold = 0



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
        count_cone += quantity
    
    elif product == 2:
        total = quantity * glass
        count_glass += quantity
        
    elif product == 3:
        total = quantity * banana_split
        count_banana_split += quantity
    
    else:
        print("product does not exist")
    
    clients += 1
    total_sold += total
    
    print(f"the total of your buy is {total}")
    
    continu = input("Do you want continue (s/n)")
    
    if count_cone > count_glass and count_cone > count_banana_split:
        print("the most ordered product was cone")
    elif count_glass > count_cone and count_glass > count_banana_split:
        print("the most ordered product was glass")
    
    elif count_banana_split > count_glass and count_banana_split > count_cone:
        print("he most ordered product was banana split")
    
    else :
        print("All of them had the same sales")
    
print("resume")
print(f"total sold {total_sold}")
print(f"total client {clients}")    
    
    
    
        