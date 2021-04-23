class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
my_name = "Saban"
my_password = "clarusway"
x = input("please enter your name : ").capitalize()
if x == my_name:
    print("Hello,"+ color.BOLD + my_name + color.END +"!"+"The password is : "+ my_password)
else:
    print("Hello,"+ color.BOLD + x + color.END + "!"+"See you later." )