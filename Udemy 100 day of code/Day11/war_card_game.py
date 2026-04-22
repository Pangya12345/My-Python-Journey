import random
print("Welcome to the 'Card War' game!")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
player_deck = []
computer_deck = []
player_bet = 1000
print(f"You have ${player_bet}")
game_count = 1
player_score = 0
computer_score = 0
round = 0
while game_count <= 10:
    def append_card(p_deck, c_deck, game):
            game = game + 1
            p_deck.append(random.choice(cards))
            c_deck.append(random.choice(cards))
    append_card (game = game_count, c_deck = computer_deck, p_deck = player_deck)

    def battle(p_deck, c_deck, r, p_score, c_score):
        r = r + 1
        print(f"Round {r}")

        p_bet = int(input("Enter You bet?" ))
        p_pop = p_deck.pop()
        c_pop = c_deck.pop()
        print(f"Player Card: {p_pop}")
        print(f"Computer Card: {c_pop}")
        if p_pop > c_pop:
             print("You Win!")
             p_score += 1
             (p_bet * 2) + player_bet
             print(f"Player bet amount: {player_bet}")
             print(f"Player Score: {p_score}")
             print(f"Computer Score: {c_score}")

        elif p_pop < c_pop:
             print("You Lost!")
             c_score += 1
             player_bet - p_bet
             print(f"Player bet amount: {player_bet}")
             print(f"player Score: {p_score}")
             print(f"Computer Score: {c_score}")
        elif player_pop == computer_pop:
             print("Draw")
             print("\n" * 5)
             print("War!")
             war_count = 1
             computer_war_list = []
             player_war_list = []
             while war_count <= 2:
                war_count = war_count + 1
                def war_condition(pp_deck, cc_deck, com_score, pla_score):
                     war_p_pop = pp_deck.pop()
                     player_war_list.append(war_p_pop)
                     war_c_pop = cc_deck.pop()
                     computer_war_list.append(war_c_pop)
                     war_p_condition = player_war_list.pop()
                     war_c_condition = computer_war_list.pop()
                     print(f"Player Card: {war_p_condition}")
                     print(f"Computer Card: {war_c_condition}")
                     if war_p_condition > war_c_condition:
                          print("You win!")
                          pla_score += 3
                          player_bet + (p_bet * 2)
                     elif war_p_condition < war_c_condition:
                          com_score += 3
                          print("You Lost!")
                          com_score += 3
                          player_bet - p_bet
                     elif war_p_condition == war_c_condition:
                          print("Draw")
                     print(f"Player bet amount: {player_bet}")
                     print(f"Player Score: {pla_score}")
                     print(f"Computer Score: {com_score}")
                war_condition(pp_deck = player_deck, cc_deck = computer_deck, com_score = computer_score, pla_score = player_score)
    battle(p_deck = player_deck, c_deck = computer_deck, r = round, p_score = player_score, c_score = computer_score)
    random.shuffle(computer_deck)
    random.shuffle(player_deck)


if player_score > computer_score:
     print(f"You final Score is {player_score}")
elif player_score < computer_score:
     print("You lost the game!")
elif len(player_deck) == 0:
     print("You lost the game!")
elif len(computer_deck) == 0:
     print("You win!")
elif player_bet == 0:
     print("You lost the game!")
