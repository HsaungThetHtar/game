import random

num =random.randrange(1000, 10000)
guesses = 0

while True:
    n = input('Guess the 4 digit number: ')

    if n == num:
        guesses += 1
        print("Great! You guessed the number in", guesses, "tries! You're a Mastermind!")
        break
    else:
        guesses += 1
        count = 0
        n = str(n)
        num = str(num)
        c = ['X'] * 4

        for i in range(4):
            if n[i] == num[i]:
                count += 1
                c[i] = n[i]

        print("Not quite the number. But you did get", count, "digit(s) correct!")
        print("Digits you guessed correctly", " ".join(c))
