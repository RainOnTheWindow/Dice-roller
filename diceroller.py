import random


def roll(num):
    return random.randint(1, int(num))


list_rolls = list()


def begin():
    num = raw_input('How many sides would you like your dice to have?')
    answer = raw_input('How many dice would you like to roll?')
    for i in range(int(answer)):
        list_rolls.append(roll(num))

    print("Here are your results: " + str(list_rolls))
    print("The total value is " + str(sum(list_rolls)))
    reroll()


def reroll():
    reroll = raw_input('Would you like to roll again? y or n?')
    if reroll == "y":
        del list_rolls[:]
        begin()
    else:
        print('Thank-you for using the dice roller!')
        exit


print("Welcome to the dice roller.")
begin()
