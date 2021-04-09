from art import logo
print(logo)
def plus(number_1, number_2):
  return number_1 + number_2
def ex(number_1, number_2):
  return number_1 - number_2
def multi(number_1, number_2):
  return number_1 * number_2
def div(number_1, number_2):
  return number_1 / number_2
def calculate(number_1, operator, number_2):
  operators = {"+": plus(number_1, number_2), "-": ex(number_1, number_2), "*": multi(number_1, number_2), "/": div(number_1, number_2)}
  for i in operators:
    if operator == i:
      return operators[i]
should_end = True
while should_end == True:
  number_1 = float(input("What's the first number ?: "))
  print("+ \n- \n* \n/")
  operator = input("Pick on operation: ")
  number_2 = float(input("What's the next number ?: "))
  print(f"{number_1} {operator} {number_2} = {calculate(number_1, operator, number_2)}")
  its_ok = input(f"Type 'y' to continue calculating with {calculate(number_1, operator, number_2)}, type 'n' to start a new").lower()
  if its_ok == 'n':
    should_end = True
    # clear() clear function not yet learn
  elif its_ok == 'y':
    number_1 = calculate(number_1, operator, number_2)
    print("+ \n- \n* \n/")
    operator = input("Pick on operation: ")
    number_2 = float(input("What's the next number ?: "))
    print(f"{number_1} {operator} {number_2} = {calculate(number_1, operator, number_2)}")
    its_ok = input(f"Type 'y' to continue calculating with {calculate(number_1, operator, number_2)}, type 'n' to start a new").lower()
    should_end = True
  else:
    should_end = False