saved_amount = int(input('Please enter your saved amount: '))
ps4_price = 300
if saved_amount > ps4_price:
    print("Yippee! You can buy your PS4")
elif saved_amount >= (ps4_price / 2):
    print("You saved more than half, keep saving!")
elif saved_amount <= (ps4_price / 2):
    print("You must save more, keep saving!")

math_mark = int(input('Please enter the mark: '))
if math_mark > 84:
    print("A (Excellent)")
elif math_mark > 69:
    print("B (Good)")
elif math_mark > 59:
    print("C (Medium)")
elif math_mark > 44:
    print("D (Not Bad)")
else:
    print("F (Failed)")