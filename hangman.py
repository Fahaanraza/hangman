import random
wordlist = ["mouse", "banana", "fahaan", "king", "chaithanya",
            "bhabya", "sharan", "minaj", "munaf", "ershad"]
choosen = random.choice(wordlist)
print(choosen)
chos_length = len(choosen)
empty = []
for i in range(chos_length):
    empty.append("_")


def guess():
    for i in range(0, chos_length):
        if choosen[i] == guessed:
            empty[i] = guessed
    print(empty)


end_game = False
lives = 3
while "_" in empty and not end_game:
    guessed = input("Guess a letter: ")
    guessed.lower

    if guessed not in choosen:
        lives = lives-1
        print("Thats not a correct letter\n Remaining lives= "+str(lives))
    if lives == 0:
        print("you lose-__-")
        end_game = True
    guess()
    if "_" not in empty:
        print("ya won")
