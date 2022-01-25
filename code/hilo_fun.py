import random
def main():
    points = 300
    play_game(points)

def play_game(points):
    while points >0:
        card_value_initial = random.randint(1,13)
        print (f"Dealer's new card is: {card_value_initial}")
        player_guess = input(("Do you believe the card will be higher or lower (H/L): "))
        card_value_next = random.randint(1,13) 
        print(card_value_next)
        score_adjustment = scoring(player_guess,card_value_initial,card_value_next)
        points += score_adjustment
        print(points)
        countinue_playing = input("Do you wish to contine? Y/N: ")
        if countinue_playing.upper() == "Y":
            continue
        else:
            break

def scoring(player_guess,card_value_initial,card_value_next):
    if player_guess.upper() == "H"  and card_value_next > card_value_initial:
        score_adjustment = 100
        print (f"Dealers card is: {card_value_next}. You were correct You earned 100 points!")
    elif player_guess.upper() == "H"  and card_value_next <= card_value_initial:
        score_adjustment = -75
        print(f"Dealers card is: {card_value_next}. Sorry, you were incorrect.  You lost 75 points.")
    elif player_guess.upper() == "L"  and card_value_next < card_value_initial:
        score_adjustment = 100
        print(f"Dealers card is: {card_value_next}. You were correct!  You earned 100 points")
    elif player_guess.upper() == "L"  and card_value_next >= card_value_initial:
        score_adjustment = -75
        print (f"Dealers card is: {card_value_next}. Sorry you were incorrect. You lost 75 points")
    return score_adjustment
    
if __file__==main():
    main()