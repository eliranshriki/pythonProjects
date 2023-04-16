import random
import blackjack_art
import os
end_game=False
comp_drow=True

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card
def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(user_cards,computer_cards):
    if calculate_score(user_cards)>21:
        return f"Your score is {calculate_score(user_cards)} and it's over 21 you loose"
    elif calculate_score(computer_cards)>21:
        return f"the computer score is {calculate_score(computer_cards)} and it's over 21 and he loose"
    else:
        if calculate_score(computer_cards) == 0:
            return "the computer have a Blackjack and he win"
        elif calculate_score(user_cards)==0 and calculate_score(computer_cards)!=0:
            return "you have Blackjack you win"
        else:
            if calculate_score(user_cards)==calculate_score(computer_cards):
                return (f"you have the same score {calculate_score(user_cards)} and it's a DROW")
            elif calculate_score(user_cards)>calculate_score(computer_cards):
                return (f"your score is {calculate_score(user_cards)} the computer score is {calculate_score(computer_cards)} and you WIN")
            elif calculate_score(user_cards)<calculate_score(computer_cards):
                return (f"your score is {calculate_score(user_cards)} the computer score is {calculate_score(computer_cards)} and you loose")


print(blackjack_art.logo)
continue_play=True
while continue_play:
  user_cards = []
  computer_cards = []
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  print(f"your card are {user_cards} and the score of your card are {calculate_score(user_cards)}")
  print(f"the computer card are {computer_cards} and the score of there card are {calculate_score(computer_cards)}")

  if calculate_score(computer_cards) == 0 or calculate_score(user_cards)==0 or calculate_score(user_cards)>21:
    end_game=True

  while end_game == False:
    drow=input("do you want to draw another card.? type 'y' for yes or 'n' for no ").lower()
    if drow == 'y':
        user_cards.append(deal_card())
        print(f"your card {user_cards} and the score is {calculate_score(user_cards)}")
        if calculate_score(user_cards)>21:
            end_game=True
    else:
        while comp_drow:
            if calculate_score(computer_cards)<17:
                computer_cards.append(deal_card())
                print (computer_cards)
                if calculate_score(computer_cards)>21:
                    comp_drow=False
                    end_game=True
            else:
                comp_drow=False
                end_game=True
  
  print(compare(user_cards,computer_cards))
  more_game=input("do you wand to play again? type 'y' for yes 'n' for no")
  if more_game=='y':
    os.system('clear')
    print(blackjack_art.logo)
    end_game=False
    comp_drow=True
  else:
    continue_play=False

