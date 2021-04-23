person_age = input("Are you a cigarette addict older than 75 years old? Please enter 'yes' or 'no' :").lower()
if person_age == "yes":
    age = True
else:
    age = False
person_chronic = input("Do you have a severe chronic disease? Please enter 'yes' or 'no' :").lower()
if person_chronic == "yes":
    chronic = True
else:
    chronic = False
person_immune = input("Is your immune system too weak? Please enter 'yes' or 'no' :").lower()
if person_immune == "yes":
    immune = True
else:
    immune = False
if age or chronic or immune:
    print("You are in risky group")
else:
    print("You are not in risky group")