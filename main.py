import random

num_players = 3

suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
jokers = ["Red Joker", "Black Joker"]


def deck_creation():
    deck = []
    for suit in suits:
        for value in values:
            deck.append(f'{value} of {suit}')
    deck.extend(jokers)
    return deck


def shuffler(deck):
    deck.remove("A of Hearts")
    deck.remove("A of Diamonds")  # strictly for ChaseTheAce
    deck.remove("A of Clubs")
    random.shuffle(deck)
    return deck


def serve(deck):
    hands = {}
    for i in range(num_players):
        hands[f'Player {i+1}'] = []
        for j in range(51):
            if j % num_players == i:
                hands[f'Player {i+1}'].append(deck[j])
    return hands


def print_hand(hand):
    for card in hand:
        print(card)
    print('----------')


def drop_pairs(player, hand):
    sorted_hand = sorted(hand)
    num_cards = len(sorted_hand)
    cards_to_drop = []

    for i in range(num_cards - 1):
        if sorted_hand[i] not in cards_to_drop & sorted_hand[i][
                0] == sorted_hand[i + 1][0]:
            cards_to_drop.extend(sorted_hand[i:i + 2])
    if 'Red Joker' in sorted_hand and 'Black Joker' in sorted_hand:
        cards_to_drop.extend(["Red Joker", "Black Joker"])
    print("------------------")
    if cards_to_drop == []:
        print(f'{player} had nothing to drop.')
    else:
        print(f'{player} dropped the following cards:')
        print_hand(cards_to_drop)
        hand = list(set(hand) - set(cards_to_drop))
    print(f'{player} has {len(hand)} cards left.')
    print('----------')
    return hand


def play_game():
    deck = deck_creation()
    shuffled_deck = shuffler(deck)

    hands = serve(shuffled_deck)
    players = hands.keys()
    print(players)
    print("You are Player 1. Here is your hand:")
    print_hand(hands['Player 1'])
    print("-------------------")
    for player in players:
        hands[player] = drop_pairs(player, hands[player])

    # player1 picks from player2
    card_count = len(hands['Player 2'])
    print(f'Player 2 has {card_count}')
    choice = int(input(f'Type a number between 1-{card_count} to pick.'))
    card_choice = hands['Player 2'].pop(choice - 1)
    hands['Player 1'].append(card_choice)
    print(f'You picked {card_choice} from Player 2.')
    print('Your new hand is:')
    print_hand(hands['Player 1'])

    card_count = len(hands['Player 3'])
    choice = random.randint(1, card_count)
    card_choice = hands['Player 3'].pop(choice-1)
    hands['Player 2'].append(card_choice)


play_game()
