from art import logo
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game = input("Do you want a black jack card game ? enter 'y' or 'n' \n").lower()
your_cards = []
computer = []
your_cards.extend([random.choice(cards), random.choice(cards)])
computer.extend([random.choice(cards)])
print(logo)
print(f"\tYour cards : {your_cards}, current scores: {sum(your_cards)}")
print(f"\tComputer's first card: {computer}")
a = sum(your_cards)
b = sum(computer)
while (sum(your_cards) < 21) and (sum(computer) < 21):
    get_card = input("Type 'y' to get another card, type 'n' to pass : ").lower()
    if get_card == 'y':
        your_cards.extend([random.choice(cards)])
        print(f"\tYour cards : {your_cards}, current scores: {sum(your_cards)}")
        while sum(computer) < 17:
            computer.extend([random.choice(cards)])
        print(f"\tComputer's final hand: {computer}, current scores: {sum(computer)}")
    elif get_card == 'n':
        while sum(computer) < 17:
            computer.extend([random.choice(cards)])
            print(f"\tComputer's final hand: {computer}, current scores: {sum(computer)}")
            if sum(computer) == 21:
              print(f"You lose. Computer final hands {computer}")
        if sum(your_cards) == sum(computer):
            print("Draw")
            break
        elif sum(your_cards) > sum(computer):
            print("Congrat. You win")
        
if sum(your_cards) == 21:
    print("Blackjack You Win")       
elif sum(your_cards) > 21:
    print("You went over. You lose :D")
elif sum(your_cards) == sum(computer):
    print("Draw")    
elif sum(your_cards) < 21 and sum(computer) > 21:
    print("Congrat. You win")
else:
    print("You went over. You lose :D")