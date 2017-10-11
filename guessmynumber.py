import random

def print_header():
    print("welcome to guess the number")
    print("pick a secret number from 1-100")
    print("i will guess it as few attemps as possible")


def print_footer(number,tries):
    print("the computer guessed correct, the number is", number)
    print(" it only takes computer", tries, "tries")



def main():
    print_header()

    number = random.randint(1, 100)
    answer = 'h' or 'l' or 'c'
    number = int(input("enter a number"))
    smallest = 1
    highest = 100
    guess = random.randint(1, 100)
    tries = 1
    while (guess != number):

        print(" the computer takes a guess", guess)

        a = raw_input("enter 'h' if your number is higher,'l' if your number is lower")
        if a == 'h':
            smallest = guess + 1
        elif a == 'l':
            highest = guess
        tries += 1
        guess = (smallest + highest) // 2

    print_footer(number,tries)

main()


