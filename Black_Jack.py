import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
decision = 'y'

def blackjack (game):
    print("Welcome to Blackjack!")
    you = []
    dealer = []
    sum1 = 0
    sum2 = 0
    while game == 'y':
        for i in range (2):
            you.append(random.choice(cards))
            dealer.append(random.choice(cards))
            sum1 += int(you[i])
            sum2 += int(dealer[i])
        print(f"Your cards: {you}, current score = {sum1}")
        print(f"Computer's first card: {dealer[0]},")
        play = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        while play == 'y':
            you.append(random.choice(cards))
            dealer.append(random.choice(cards))
            sum1 += int(you[-1])
            sum2 += int(dealer[-1])
            print(f"Your cards: {you}, current score = {sum1}")
            print(f"Computer's first card: {dealer[0]}")
            if 11 in dealer and sum(dealer) > 21:
                dealer [dealer.index(11)] = 1
                sum2 -= 10
            if 11 in you and sum(you) > 21:
                you[you.index(11)] = 1
                sum1 -= 10
            if sum1 >= 21 or sum2 >= 21:
                break
            play = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if play == 'n':
                break

        while sum2 < 17:
            dealer.append(random.choice(cards))
            sum2 += int(dealer[-1])
        if 11 in dealer and sum(dealer) > 21:
            dealer[dealer.index(11)] = 1
            sum2 -= 10
        if 11 in you and sum(you) > 21:
            you[you.index(11)] = 1
            sum1 -= 10
        if sum1 > sum2:
            if sum1 > 21 and sum2 == 21:
                print(f"Your final hand: {you}, final score: {sum1}")
                print(f"Computer's final hand:{dealer}, final score: {sum2}")
                print("You went over. Opponent wins with a blackjack 😭")
                return
            elif sum1 > 21 and sum2 < 21:
                print(f"Your final hand: {you}, final score: {sum1}")
                print(f"Computer's final hand:{dealer}, final score: {sum2}")
                print("You went over. You lose 😭")
                return
            elif sum1 == 21:
                print(f"Your final hand: {you}, final score: {sum1}")
                print(f"Computer's final hand:{dealer}, final score: {sum2}")
                print("Win with a Blackjack 😱")
                return
            else:
                print(f"Your final hand: {you}, final score: {sum1}")
                print(f"Computer's final hand:{dealer}, final score: {sum2}")
                print("You win😎")
                return
        elif sum2 > sum1:
            if sum2 > 21 and sum1 < 21:
                print(f"Your final hand: {you}, final score: {sum1}")
                print(f"Computer's final hand:{dealer}, final score: {sum2}")
                print("Dealer went over. You win😎")
                return
            elif sum2 > 21 and sum1 == 21:
                print(f"Your final hand: {you}, final score: {sum1}")
                print(f"Computer's final hand:{dealer}, final score: {sum2}")
                print("Dealer went over. Win with a Blackjack 😎")
                return
            elif sum2 == 21:
                print(f"Your final hand: {you}, final score: {sum1}")
                print(f"Computer's final hand:{dealer}, final score: {sum2}")
                print("Lose, opponent has Blackjack 😱")
                return
            else:
                print(f"Your final hand: {you}, final score: {sum1}")
                print(f"Computer's final hand:{dealer}, final score: {sum2}")
                print("You lose 😭")
                return
        elif sum1 == sum2:
            print(f"Your final hand: {you}, final score: {sum1}")
            print(f"Computer's final hand:{dealer}, final score: {sum2}")
            print("Draw 🙃")
            return

        # if sum1 > sum2:
        #     if sum1 > 21 and sum2 == 21:
        #         print(f"Your final hand: {you}, final score: {sum1}")
        #         print(f"Computer's final hand:{dealer}, final score: {sum2}")
        #         print("You went over. Opponent wins with a blackjack 😭")
        #         return
        #     elif sum1 > 21 and sum2 < 21:
        #         print(f"Your final hand: {you}, final score: {sum1}")
        #         print(f"Computer's final hand:{dealer}, final score: {sum2}")
        #         print("You went over. You lose 😭")
        #         return
        #     elif sum1 == 21:
        #         print(f"Your final hand: {you}, final score: {sum1}")
        #         print(f"Computer's final hand:{dealer}, final score: {sum2}")
        #         print("Win with a Blackjack 😱")
        #         return
        #     else:
        #         print(f"Your final hand: {you}, final score: {sum1}")
        #         print(f"Computer's final hand:{dealer}, final score: {sum2}")
        #         print("You win 😎")
        #         return
        # elif sum2 > sum1:
        #     if sum2 > 21 and sum1 < 21:
        #         print(f"Your final hand: {you}, final score: {sum1}")
        #         print(f"Computer's final hand:{dealer}, final score: {sum2}")
        #         print("Dealer went over. You win😎")
        #         return
        #     elif sum2 > 21 and sum1 == 21:
        #         print(f"Your final hand: {you}, final score: {sum1}")
        #         print(f"Computer's final hand:{dealer}, final score: {sum2}")
        #         print("Dealer went over. Win with a Blackjack 😎")
        #     elif sum2 == 21:
        #         print(f"Your final hand: {you}, final score: {sum1}")
        #         print(f"Computer's final hand:{dealer}, final score: {sum2}")
        #         print("Lose, opponent has Blackjack 😱")
        #         return
        #     else:
        #         print(f"Your final hand: {you}, final score: {sum1}")
        #         print(f"Computer's final hand:{dealer}, final score: {sum2}")
        #         print("You lose 😭")
        #         return
        # elif sum1 == sum2:
        #     print("Draw 🙃")
        #     return

while decision == 'y':

    decision = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    print("\n*20")
    print(logo)
    blackjack(decision)
print("Thanks for playing. See you soon")
