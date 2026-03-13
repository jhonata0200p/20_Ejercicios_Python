hour = int(input("Enter the entry time "))

if hour in range(6,12):
    print("morning")

elif hour in range(12, 18):
    print("tarde")

elif hour in range(18, 23):
    print("night")
    
else:
    print("outside of business hours")