
# fiz buzz game
game = []
for i in range(1,101):
    game.append(i)
    if i % 3 == 0 and i % 5 == 0:
        game[i-1] = "FizzBuzz"
    elif i % 3 == 0:
        game[i -1] ="Fizz"
    elif i % 5 == 0:
        game[i - 1] = "Buzz"
    print(game[i-1])

