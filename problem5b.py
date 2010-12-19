def check_even_devided(number, list):
    """
    Retuns the number if remainder of all numbers in list is zero.
    """
    i = 0
    for n in list:
        if not number % n:
            i += 1
        if i == len(list):
            return number

        
    
basenumber = 20
multi = 1
list = [5,7,9,11,13,16,17]

while True:
    number = multi * basenumber
    number = check_even_devided(number, list)
    if number :
        number = check_even_devided(number, range(1,20))
        if number:
            print number
            break
    multi += 1

