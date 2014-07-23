import random


def roll(num):
    return random.randint(1, int(num))

list_rolls = list()


print("Welcome to the dice roller.")
num = raw_input('How many sides would you like your dice to have?')
answer = raw_input('How many dice would you like to roll?')
for i in range(int(answer)):
    list_rolls.append(roll(num))


print("Here are your results: " + str(list_rolls))
print("The total value is " + str(sum(list_rolls)))

    
