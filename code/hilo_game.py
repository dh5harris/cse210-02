import random

points=300

countinue_playing = "Y"

#def continue_playing (points):
while points >0 and countinue_playing.upper() == "Y":  #need to add if you still want to play
    print()
    card_value_initial = random.randint(1,13)
    print (f"Dealer's new card is: {card_value_initial}")
    player_guess = input(("Do you believe the card will be higher or lower (H/L): "))
    card_value_next = random.randint(1,13)
    if player_guess.upper() == "H"  and card_value_next > card_value_initial:
        points = points + 100
        print (f"Dealers card is: {card_value_next}. You were correct You earned 100 points!")
    elif player_guess.upper() == "H"  and card_value_next <= card_value_initial:
        points = points - 75
        print(f"Dealers card is: {card_value_next}. Sorry, you were incorrect.  You lost 75 points.")
    elif player_guess.upper() == "L"  and card_value_next < card_value_initial:
        points = points + 100
        print(f"Dealers card is: {card_value_next}. You were correct!  You earned 100 points")
    elif player_guess.upper() == "L"  and card_value_next >= card_value_initial:
        points = points - 75
        print (f"Dealers card is: {card_value_next}. Sorry you were incorrect. You lost 75 points")
    print (points)
    countinue_playing = input("Do you wish to contine? Y/N: ")






