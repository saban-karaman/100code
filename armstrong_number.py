
number = input("Please enter a number :")
if number.isdigit() and int(number) > 0:
    total = 0
    for i in number:
        total += int(i)**len(number)
    if total == int(number):
        print(f"{int(number)} is an Armstrong number")
    else:
        print("It is not an Armstrong number")
else:
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!") 
 