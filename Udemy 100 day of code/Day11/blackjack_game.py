from art import logo
import random
cards = ["11", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K" ]
player_list = []
computer_list = []
print("Welcome to the blackjack game! 🃏🎴")
rule = input("Do you want to hear the rule of this blackjack game? type 'y' or 'n' ").lower()
while rule == "y":
    print("\n" * 10)
    print("-----Rule-----")
    print("You need to beat the dealer (computer) by having a total score of card closer 21 without exceeding 21")
    print("Cards 2-10 are face value (score count on card number)")
    print("Jack, Madam, King (J,Q, K) count as 10 per card")
    break
game_start = input("you want to play a game of Blackjack? type 'y' or 'n ").lower()
if game_start == "n":
    print("\n" * 3)
    print("See you next time!👋😊👋🏻")
elif game_start == "y":
    print(logo)
    def select_card(user_card, computer_card, cards_deck):
        user_card.append(random.choice(cards_deck))
        user_card.append(random.choice(cards_deck))
        computer_card.append(random.choice(cards_deck))
        computer_card.append(random.choice(cards_deck))
    select_card(cards_deck = cards, computer_card = computer_list, user_card = player_list)
    total = 0
    def calculate_total_score_user(player_card, total_sum):
        for number in player_card:
            if number == "J" or number == "Q" or number == "K":
                total_sum += 10
            elif number != "J" and number != "Q" and number != "K":
                total_sum += int(number)
        return total_sum
    total_c =
    def computer_first_card(c_card):
        return c_card[0]
    def print_out_first():
        print(f"Your cards: {player_list}, current score: {calculate_total_score_user(total_sum = total, player_card = player_list)}")
        print(f"Computer's first card: {computer_first_card(c_card = computer_list)}")
    print_out_first()
    game_over = False
    while not game_over:
        total_sum_over = 0
        def calculate_total(player, total_naja):
            for i in player:
                if i == "J" or i == "Q" or i == "K":
                    total_naja += 10
                elif i == "A":
                    print(f"Your current card is {player_list}")
                    second_decision = input(
                        "Do you want to assume that Aces in your deck is '11' or '10'? type 'eleven' for 11, type 'one' for 1 ").lower()
                    if second_decision == "eleven":
                        total_naja += 11
                    elif second_decision == "one":
                        total_naja += 1
                else:
                    total_naja += int(i)
            return total_naja
        total_com = 0
        def calculate_total_c_score(c_list, total_cc):
            for n in c_list:
                if n == "J" or n == "Q" or n == "K":
                    total_cc += 10
                elif n == "A":
                    total_cc += 11
                else:
                    total_cc += int(n)
            return total_cc


        while calculate_total_c_score(total_cc = total_com, c_list = computer_list) < 17 and calculate_total(total_naja = total_sum_over, player = player_list) <= 21:
            computer_list.append(random.choice(computer_list))

        hit_or_not = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if hit_or_not == "y":
            def append_card(player_card, card_deck):
                player_card.append(random.choice(card_deck))
            append_card(player_card = player_list, card_deck = cards)
            total_com = 0

            print(f"Your cards: {player_list}, current score: {calculate_total(total_naja = total_sum_over, player = player_list)}")
            print(f"Computer's first card: {computer_first_card(c_card = computer_list)}")

        elif hit_or_not == "n":
            game_over = True
            print(f"Your final hand: {player_list}, final score: {calculate_total(total_naja = total_sum_over, player = player_list)}")
            print(f"Computer's final hand: {computer_list}, final score: {calculate_total_c_score(total_cc = total_com, c_list = computer_list)}")
            def compare(c_final_score, u_final_score):
                if u_final_score > 21:
                    print("You went over. You lost😭")
                elif c_final_score > u_final_score:
                    print("You lost😤")
                elif c_final_score < u_final_score:
                    print("You win🎉🥳🎊🎁")
                elif c_final_score == u_final_score and c_final_score <= 21 and u_final_score <= 21:
                    print("Draw⚖️")
            compare(u_final_score = calculate_total(total_naja = total_sum_over, player = player_list), c_final_score = calculate_total_c_score(total_cc = total_com, c_list = computer_list))




















