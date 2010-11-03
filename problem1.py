suma = 0 
for number in range(1000):
    if not (number % 5 and number % 3):
        suma += number
        print number

print suma
    
