def analyze_input(rollInput):
    rollInput = rollInput.lower()
    # Look for 'd' character.
    if rollInput.find('d') > -1:
        positionOfDie = rollInput.find('d')
    else:
        return("Error")
    # Look for '+' or '-' character and define it.
    if rollInput.find('+') > -1:
        positionOfMod = rollInput.find('+')
        modType = '+'
    elif rollInput.find('-') > -1:
        positionOfMod = rollInput.find('-')
        modType = '-'
    else:
        positionOfMod = 0
        modType = 0
    # Check for number of dice. If missing, set to 1.
    if positionOfDie == 0:
        diceAmount = 1
    else:
        diceAmount = rollInput[ : positionOfDie]
    # Check for dice type and modifier.
    if modType == '+':
        diceType = rollInput[positionOfDie + 1 : positionOfMod] # Which dice are rolled?
        diceModifier = rollInput[positionOfMod + 1 : ]          # What is the modifier?
    elif modType == '-':
        diceType = rollInput[positionOfDie + 1 : positionOfMod] # Which dice are rolled?
        diceModifier = rollInput[positionOfMod + 1 : ]          # What is the modifier?
        diceModifier = int(diceModifier) - int(diceModifier) - int(diceModifier)
    elif modType == 0:
        diceType = rollInput[positionOfDie + 1 : ]              # Which dice are rolled?
        diceModifier = 0                                        # What is the modifier?
    # Return function result in a list.
    try:
        result = [int(diceAmount), int(diceType), int(diceModifier)]
    except:
        return("Error")
    return result

import random
print("SIMPLE DICE ROLLER BY MATIJA\n----------------\nTYPE 'Q' TO QUIT\n----------------\nINPUT DIE ROLL (EXAMPLE: 2d6+4):\n")

counter = 0
while True:
    # Ask user for input. Stop if 'q' entered.
    rollInput = input()
    if rollInput == 'q' or rollInput == 'Q':
        break
    # Invoke roll input analysis.
    if analyze_input(rollInput) == "Error":
        print("Incorrect syntax. Try again.\n")
        continue
    else:
        rollValues = analyze_input(rollInput)
    # Output the roll result.
    diceRolls = []
    for diceAmount in range(rollValues[0]):                     # Generate a list of individual rolls.
        diceRolls.append(random.randint(1, rollValues[1]))
    counter += 1
    print("Dice:", diceRolls)                                   # Print the final outcome.
    if rollValues[2] > 0:
        print("Roll #", counter, " Result: ", sum(diceRolls), " + ", rollValues[2], " = ", sum(diceRolls) + rollValues[2], sep='')
    elif rollValues[2] < 0:
        if sum(diceRolls) + rollValues[2] >= 0:
            print("Roll #", counter, " Result: ", sum(diceRolls), " - ", abs(rollValues[2]), " = ", sum(diceRolls) + rollValues[2], sep='')
        else:
            print("Roll #", counter, " Result: ", sum(diceRolls), " - ", abs(rollValues[2]), " = ", sum(diceRolls) + rollValues[2], " (0) ", sep='')
    else:
        print("Roll #", counter, " Result: ", sum(diceRolls), sep='')
    print()
