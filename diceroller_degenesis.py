import random

print("-------------------------------")
print("DEGENESIS DICE ROLLER BY MATIJA")
print("-------------------------------")
print("       ENTER 'Q' TO QUIT")
print(" -----------------------------")
print(" ENTER AMOUNT OF DICE TO ROLL:")

counter = 0
while True:
    print("")
    rollInput = input("")
    if rollInput == 'q' or rollInput == 'Q':
        break
    try:
        rollInput = int(rollInput)
    except:
        for digit in range(len(str(rollInput))):
            print("-", end='')
        print("\nNo. Try again.")
        continue
    if int(rollInput) >= 100:
        for digit in range(len(str(rollInput))):
            print("-", end='')
        print("\nNo. Try again.")
        continue
    elif int(rollInput) < 0:
        for digit in range(len(str(rollInput))):
            print("-", end='')
        print("\nNo. Try again.")
        continue
    diceRolls = []
    successes = []
    triggers = 0
    counter += 1
    for die in range(rollInput):
        roll = random.randint(1, 6)
        diceRolls.append(roll)
        if roll > 3:
            successes.append(roll)
        if roll == 6:
            triggers += 1

    diceRolls = sorted(diceRolls, reverse=True)
    successes = sorted(successes, reverse=True)

    for digit in range(len(str(rollInput))):
            print("-", end='')
    print("\nRoll #", counter, ": ", diceRolls, sep='')
    print("-----------------")

    if not successes:
        print("Success | Trigger")
        print("--------|--------")
        print("      0 | 0      ")
    elif len(successes) < 10:
        print("Success | Trigger")
        print("--------|--------")
        print(f"      {len(successes)} | {triggers}      ")
    else:
        print("Success | Trigger")
        print("--------|--------")
        print(f"     {len(successes)} | {triggers}      ")
    print("-----------------")

    if diceRolls.count(1) > len(successes):
        print("CRITICAL FAILURE!")
