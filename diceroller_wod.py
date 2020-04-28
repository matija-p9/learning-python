def explode_die():
    a = 10
    expl = []
    while a == 10:
        expl.append(a)
        a = random.randint(1,10)
    if a > 7:
        expl.append(a)
    return expl

import itertools
import random
print("SIMPLE DICE ROLLER BY MATIJA\n----------------\nTYPE 'Q' TO QUIT\n----------------\nINPUT DIE QUANTITY:\n")

counter = 0
while True:
    rollInput = input()
    if rollInput == 'q' or rollInput == 'Q':
        break
    try:
        rollInput = int(rollInput)
    except:
        print("Incorrect syntax. Try again.\n")
        continue
    diceRolls = []
    successes = []
    explosions = []
    finalSuccesses = []
    counter += 1
    for die in range(rollInput):
        roll = random.randint(1, 10)
        diceRolls.append(roll)
        if roll > 7:
            successes.append(roll)
        if 7 < roll < 10:
            finalSuccesses.append(roll)
        if roll == 10:
            explosions.append(explode_die())

    explosions = list(itertools.chain(*explosions))

    diceRolls = sorted(diceRolls, reverse=True)
    print("Roll #", counter, ": ", diceRolls, sep='')

    successes = sorted(successes, reverse=True)
    if not successes:
        successes = [0]

    finalSuccesses = finalSuccesses + explosions
    finalSuccesses = sorted(finalSuccesses, reverse=True)
    if not finalSuccesses:
        print("Successes: ", finalSuccesses, ": 0", "\n", sep='')
    else:
        print("Successes: ", finalSuccesses, ": ", len(finalSuccesses), "\n", sep='')
