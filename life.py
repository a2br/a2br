from random import random as eight_ball

alive = True


def eat():
    print("Chomp, chomp.")


def sleep():
    print("ZZzZzzzzzz...")


while alive:
    fate = round(eight_ball(), 2)
    hungry = round(fate)

    (eat if hungry else sleep)()

    alive = False if fate == 0.42 else True

print('W A S T E D .')
