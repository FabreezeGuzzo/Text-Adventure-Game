# Problem Statement:  Game of survival
# Data In: Age/RunorFight/If user wants to split attributes
# Data Out:  Outcome of encounter/strength and ghost atrributes
# Credits: Fabrizio Guzzo
print("Lone Knights Quest of Survival In the hidden Forest")
print("By Guzzo Games")
#Input#1 Int
character_age = int(input("Enter Heros age"))
if character_age > 10 :
    strength_attribute = 5
    print("Heros Strength:", strength_attribute)
elif character_age == 10 :
    strength_attribute = 2
    print("Heros Strength:", strength_attribute)
else:
    strength_attribute = 1
    print("Heros Strength:", strength_attribute)
#output #1 character strength
print("Your Hero begins his journey...")
print("While traversing alone throughout the woods the hero encounters an enemy foe...")
#input #2 Str
print("The foe identifies himself as Sir Greg member of the enemy house Livington")
print("Sir Greg has a strength value of 4:")
choice_one = str(input("You have the option to fight or run:"))
if choice_one == str.lower('fight'):
    if strength_attribute > 4 :
           print("Sir Greg was defeated and won the encounter")
    elif strength_attribute < 4 :
           print("Sir Greg showed mercy in your defeat and let you runaway")
    else:
            print("You and Sir Greg suprised each other in combat and went separate ways")
else:
        print("You choose wisely and will fight another day")
        print("You have ended your journey momentarily as your hero took a long nap. Follow along for the sequel coming out in the summer of 2023")
        exit()
#Input #3 Float
print("You have unlocked the ability of Ghost:")
print("would you like to split your strength in half in order to split your strength and ghost abilities evenly?")
ghost_attribute = float(input("If yes type out .5/If not type 1:"))
if ghost_attribute == .5:
    strength_attribute == 3
    ghost_attribute == 3
    print("strength =", strength_attribute)
    print("ghost =", ghost_attribute)
else:
    strength_atribute = 6
    ghost_attribute == 0
    print("strength =", strength_atribute)
    print("ghost =", ghost_attribute)
print("The quest continues in the sequal A Knights Trail to Redemption 2 coming in the summer of 2023")
