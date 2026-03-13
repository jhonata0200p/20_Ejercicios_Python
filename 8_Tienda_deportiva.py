counter = 0

for i in range(1,7):
    question = float(input("Enter the product price: "))
    if question > 100000:
        counter += 1
        
print(f"{counter} products cost more than 100,000 ")