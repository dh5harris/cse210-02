import random

class Card:

    def __init__(self):
        self.points =0
        self.value = 0

    def get_card(self):
        #while points >0:
            self.initial_card = random.randint(1,13)
            print (f"Dealer's new card is: {self.initial_card}")
            player_guess = input(("Do you believe the card will be higher or lower (H/L): "))
            self.next_card = random.randint(1,13) 
            print(self.next_card)
            #score_adjustment = scoring(player_guess,card_value_initial,card_value_next)
           # points += score_adjustment
           
           # print(points)
            # countinue_playing = input("Do you wish to contine? Y/N: ")
            # if countinue_playing.upper() == "Y":
            #     continue
            # else:
            #     break

    def scoring(self,player_guess, self.initial_card, self.next_card):
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
        
        """"
        IC<NC and PG==L right, or IC>NC pg==H then right
            100
            
        """







