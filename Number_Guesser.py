import random
print("Welcome To Number Guesser")
print("===========\n")

angka = int(input("Please enter you favourite number from 1 to 10: "))
penebak = random.randrange(1,10)
if angka > 10:
    print("maaf angka yang kamu masukan lebih dari 10")
else:
    if angka == penebak:
        print("cool you win in this game! angka komputer: ", penebak)
    elif angka >= penebak:
        print ("You lose hahahaha")
        print("Your number is bigger than computer number, computer number is", penebak)
    else:
        print("You lose hahahaha")
        print("Your number is smaller than computer number, computer number is", penebak)
print("\nThank you for playing this game hehe")