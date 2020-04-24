# Payer throwing 2 dice
# 2 players
# Change turns
# Start game
# Win message
# 3 tries max
# Stop at X tries or max number of tries
# Keep the dice score

import random

# on_going_game = True
# player_turn = 'X'
choice_x = None
dice_one_x = None
dice_two_x = None
both_dice_score_x = None
choice_y = None
dice_one_y = None
dice_two_y = None
both_dice_score_y = None
second_turn_choice_x = None
second_turn_choice_y = None
third_turn_choice_x = None
third_turn_choice_y = None


# The first throw for player 1 (which is X)
def first_throw_x():
    global choice_x, dice_one_x, dice_two_x
    print("Player one turn ")
    choice_x = input("Type 'throw' to throw the dice: ")
    choice_x = choice_x.lower()
    if choice_x == 'throw':
        dice_one_x = random.randint(1, 6)
        dice_two_x = random.randint(1, 6)
        both_dice_score_x = dice_one_x + dice_two_x
        print('Player one rolled a', dice_one_x, "and a", dice_two_x)
        print('Player one score is', both_dice_score_x)
    elif choice_x != 'throw' :
        first_throw_x()


# The first throw for player 2 (which is Y)
def first_throw_y():
    global choice_y, dice_one_y, dice_two_y, both_dice_score_y
    print("Player two turn ")
    choice_y = input("Type 'throw' to throw the dice: ")
    choice_y = choice_y.lower()
    if choice_y == 'throw':
        dice_one_y = random.randint(1, 6)
        dice_two_y = random.randint(1, 6)
        both_dice_score_y = dice_one_y + dice_two_y
        print('Player two rolled a', dice_one_y, "and a", dice_two_y)
        print('Player two score is', both_dice_score_y)
    elif choice_y != 'throw' :
        first_throw_y()


# The second throw for player one (which is X)
def second_throw_x():
    global second_turn_choice_x, second_turn_choice_x, dice_one_x, choice_x, dice_two_x, both_dice_score_x
    second_turn_choice_x = input("Player one, do you want to throw again? (yes/no)")
    second_turn_choice_x = second_turn_choice_x.lower()
    if second_turn_choice_x == 'yes':
        dice_one_x = random.randint(1, 6)
        dice_two_x = random.randint(1, 6)
        both_dice_score_x = dice_one_x + dice_two_x
        print('Player one rolled a', dice_one_x, "and a", dice_two_x)
        print('Player one score is', both_dice_score_x)
    elif second_turn_choice_x == 'no':
        both_dice_score_x = dice_one_x + dice_two_x
        print("Player one passed with a final score of ",both_dice_score_x)
    else:
        second_throw_x()


# The second throw for player two (which is Y)
def second_throw_y():
    global second_turn_choice_y, second_turn_choice_y, dice_one_y, choice_y, dice_two_y, both_dice_score_y
    second_turn_choice_y = input("Player two, do you want to throw again? (yes/no)")
    second_turn_choice_y = second_turn_choice_y.lower()
    if second_turn_choice_y == 'yes':
        dice_one_y = random.randint(1, 6)
        dice_two_y = random.randint(1, 6)
        both_dice_score_y = dice_one_y + dice_two_y
        print('Player two rolled a', dice_one_y, "and a", dice_two_y)
        print('Player two score is', both_dice_score_y)
    elif second_turn_choice_y == 'no':
        both_dice_score_y = dice_one_y + dice_two_y
        print("Player two passed with a final score of ", both_dice_score_y)
    else:
        second_throw_y()


# The third throw for player one (which is X)
def third_throw_x():
    global third_turn_choice_x, third_turn_choice_x, dice_one_x, choice_x, both_dice_score_x, dice_two_x
    third_turn_choice_x = input("Player one, is your last chance to throw again. (yes/no)")
    third_turn_choice_x = third_turn_choice_x.lower()
    if third_turn_choice_x == 'yes':
        dice_one_x = random.randint(1, 6)
        dice_two_x = random.randint(1, 6)
        both_dice_score_x = dice_one_x + dice_two_x
        print('Player one rolled a', dice_one_x, "and a", dice_two_x)
        print('Player one final score is', both_dice_score_x)
    elif second_turn_choice_x == 'no':
        both_dice_score_x = dice_one_x + dice_two_x
        print("Player one passed with a final score of ", both_dice_score_x)
    else:
        third_throw_x()


# The third throw for player two (which is Y)
def third_throw_y():
    global third_turn_choice_y, third_turn_choice_y, dice_one_y, choice_y, both_dice_score_y, dice_two_y
    third_turn_choice_y = input("Player two, is your last chance to throw again. (yes/no)")
    third_turn_choice_y = third_turn_choice_y.lower()
    if third_turn_choice_y == 'yes':
        dice_one_y = random.randint(1, 6)
        dice_two_y = random.randint(1, 6)
        both_dice_score_y = dice_one_y + dice_two_y
        print('Player two rolled a', dice_one_y, "and a", dice_two_y)
        print('Player two final score is', both_dice_score_y)
    elif second_turn_choice_y == 'no':
        both_dice_score_y = dice_one_y + dice_two_y
        print("Player two passed with a final score of ", both_dice_score_y)
    else:
        third_throw_y()

# Final score once both passed / one passed and the other used third chance / both used third chance
def final_score():
    if both_dice_score_x >both_dice_score_y:
        print("Player one won! with a score of ", both_dice_score_x)
    elif both_dice_score_x < both_dice_score_y:
        print("Player two won! with a score of ", both_dice_score_y)
    elif both_dice_score_x == both_dice_score_y:
        print("It's a tie with a score of ", both_dice_score_x)


first_throw_x()
first_throw_y()
second_throw_x()
second_throw_y()
if second_turn_choice_x == 'yes' and second_turn_choice_y == 'yes':
    third_throw_x()
    third_throw_y()
    final_score()
elif second_turn_choice_x == 'yes' and second_turn_choice_y == 'no':
    third_throw_x()
    final_score()
elif second_turn_choice_x == 'no' and second_turn_choice_y == 'yes':
    third_throw_y()
    final_score()
elif second_turn_choice_x == 'no' and second_turn_choice_y == 'no':
    final_score()
