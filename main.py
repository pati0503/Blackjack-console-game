import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def play_game(cards):
    print(art.logo)
    game_over = False
    my_cards = [random.choice(cards), random.choice(cards)]
    dealers_card = [random.choice(cards), random.choice(cards)]

    current_score = sum(my_cards)
    current_score_dealer = sum(dealers_card)

    print(f"Your cards: {my_cards}, Current score: {current_score}")
    print(f"Dealer's card: {dealers_card[0]}")

    return my_cards, dealers_card, current_score, current_score_dealer, game_over


def check_score(cards):
    current_score = sum(cards)

    if current_score == 21 and len(cards) == 2:
        return 0

    if 11 in cards and current_score > 21:
        cards.remove(11)
        cards.append(1)
        current_score = sum(cards)

    return current_score


def main():
    my_cards, dealers_card, current_score, current_score_dealer, game_over = play_game(cards)

    while not game_over:
        current_score = check_score(my_cards)
        current_score_dealer = check_score(dealers_card)

        print(f"Your cards: {my_cards}, Current score: {current_score}")
        print(f"Dealer's card: {dealers_card[0]}")

        if current_score == 0 or current_score_dealer == 0 or current_score > 21:
            game_over = True
        else:
            decision = input('Do you want to get another card? "y/n" ')
            if decision == "y":
                new_user_card = random.choice(cards)
                my_cards.append(new_user_card)
            else:
                game_over = True

    while current_score_dealer != 0 and current_score_dealer < 17:
        new_dealer_card = random.choice(cards)
        dealers_card.append(new_dealer_card)
        current_score_dealer = check_score(dealers_card)

    print(f"Dealer's cards: {dealers_card}, Dealer's score: {current_score_dealer}")

    if current_score == current_score_dealer:
        print("Draw!")
    elif current_score_dealer == 0:
        print("Dealer has Blackjack. You lose.")
    elif current_score == 0:
        print("Blackjack! You win.")
    elif current_score > 21:
        print("You went over. Dealer wins.")
    elif current_score_dealer > 21:
        print("Dealer went over. You win.")
    elif current_score > current_score_dealer:
        print("You win!")
    else:
        print("You lose!")


main()