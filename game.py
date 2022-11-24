import random
def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card
def calculate_score(cards):
    if 11 in cards and 10 in cards and len(cards)==2:
        return 0
    if sum(cards)>21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(user_score,computer_score):
    if user_score==computer_score:
        return "draw"
    elif user_score==0:
        return "You lose because of blackjack"
    elif computer_score==0:
        return "You win because computer has blackjack"
    elif user_score>21:
        return "You lose because score is greater than 21"
    elif computer_score>21:
        return "You win because computer score is greate than 21"
    elif user_score>computer_score:
        return "You win"
    else:
        return "Computer win"

    user_cards=[]
    computer_cards=[]
    is_game_over=False
    for i in range(2):
        new_card=deal_card()
        user_cards.append(new_card)
        new_card1=deal_card()
        computer_cards.append(new_card1)
    while is_game_over==False:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print("user have", user_cards, "score", user_score)
