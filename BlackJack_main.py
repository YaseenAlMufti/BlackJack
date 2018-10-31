
from Resources import Deck_module
from Resources import ChipsandBets_module
from Resources import Board_module
import time

board = Board_module.Board()
chips = ChipsandBets_module.ChipsAndBets()
# declares one deck. could be changed to be more. could also be changed to 0 but add specific cards using (deckcards=[])
dk = Deck_module.Deck(decks=1)
# creates the deck and shuffles it
dk.create_a_deck()

# clears the screen and prints greetings at beginning of game
print("\n" * 50)
board.greetings()

# beginning of global declarations
dealer_hidden_card = []
dealertotal = 0
playertotal = 0
dealercards = []
playercards = []
dealeraces = []
playeraces = []
# end of global declarations


def playing():
    # main game function
    global dealercards, playercards
    global dealertotal, playertotal
    dealerplays = False
    global dealer_hidden_card
    place_a_bet()

    dcard1 = dk.hit()
    dealercards.append(dcard1)
    if dcard1[1] == "Ace":
        # when dealer draw an Ace
        dealeraces.append(11)
        dealertotal += 11
    else:
        # when dealer draw a regular card
        dealertotal += int(dcard1[2])
    board.print_card(dealercards, playercards)

    card = dk.hit()
    dealer_hidden_card = card
    if card[1] == "Ace":
        # when dealer draws an Ace
        dealeraces.append(11)
        dealertotal += 11
        check_dealer_aces()
    else:
        # when dealer draws a regular card
        dealertotal += int(card[2])

    # beginning of players turn
    card = dk.hit()
    playercards.append(card)
    if card[1] == "Ace":
        # when player draws an Ace
        playeraces.append(11)
        playertotal += 11
    else:
        # when player draws a regular card
        playertotal += int(card[2])
    board.print_card(dealercards, playercards)

    card = dk.hit()
    playercards.append(card)
    if card[1] == "Ace":
        # when player draws an Ace
        playeraces.append(11)
        playertotal += 11
        check_player_aces()
    else:
        # when player draws a regular card
        playertotal += int(card[2])
    board.print_card(dealercards, playercards)

    if playertotal != 21:
        # beginning of player's hit or stand event
        while True:
            if hit_stand():
                # when player decides to hit
                card = dk.hit()
                playercards.append(card)
                if card[1] == "Ace":
                    playeraces.append(11)
                    playertotal += 11
                    check_player_aces()
                else:
                    playertotal += int(card[2])
                board.print_card(dealercards, playercards)
                check_player_aces()
                if playertotal < 21:
                    continue
                elif playertotal == 21:
                    board.win()
                    chips.win_bet()
                    playing_again()
                    break
                else:
                    print("Bust!!")
                    board.lost()
                    chips.lose_bet()
                    playing_again()
                    break
            else:
                # when player decides to stand
                dealerplays = True
                break
    else:
        # when player's sum is 21
        board.win()
        chips.win_bet()
        playing_again()

    if dealerplays:
        # dealer's turn event
        dealercards.append(dealer_hidden_card)
        board.print_card(dealercards, playercards)
        check_dealer_aces()
        while dealertotal < 17:
            # when dealer's sum is less than 17, it decides to hit
            time.sleep(1)
            card = dk.hit()
            dealercards.append(card)
            if card[1] == "Ace":
                dealeraces.append(11)
                dealertotal += 11
                check_dealer_aces()
            else:
                dealertotal += int(card[2])
            board.print_card(dealercards, playercards)
            check_dealer_aces()
            if dealertotal == 21:
                # when dealer's sum is 21, the player loses
                board.lost()
                chips.lose_bet()
                playing_again()
                break
            elif 17 <= dealertotal < 21:
                # when dealer's sum is 17 or above but below 21, it decides to stand and check if it won
                if dealertotal == playertotal:
                    # when the dealer is tied with the player, the player doesn't lose the bet
                    print("Tie")
                    chips.bet = 0
                    playing_again()
                    break
                elif dealertotal < playertotal:
                    # when the dealer's sum is less than the player's sum, the player wins
                    board.win()
                    chips.win_bet()
                    playing_again()
                    break
                else:
                    # when the dealer's sum is more than the player's sum but less than 21, the player loses
                    board.lost()
                    chips.lose_bet()
                    playing_again()
                    break
            else:
                # when the dealer can still hit because the sum is less than 17
                continue
        else:
            # when the dealer has 17 or more from the first two cards
            check_dealer_aces()
            if dealertotal == playertotal:
                # when a tie happens
                print("Tie")
                chips.bet = 0
                chips.balance_statement()
                playing_again()
            elif dealertotal < playertotal:
                # when dealer's sum is less than player's sum and cannot hit again
                board.win()
                chips.win_bet()
                playing_again()
            elif 21 >= dealertotal > playertotal:
                # when dealer's sum is more than player's sum
                board.lost()
                chips.lose_bet()
                playing_again()
            else:
                # when dealer's sum is more than 21
                print("Bust!!")
                board.win()
                chips.win_bet()
                playing_again()


def check_dealer_aces():
    # this function checks if the dealer has Aces and modifies the sum accordingly
    global dealertotal, dealeraces
    if len(dealeraces) > 0:
        # when dealer has Aces
        while dealertotal > 21:
            # if sum is more than 21 and has Aces, it subtracts 10 from the sum and checks if it needs to do it again
            dealertotal -= 10
            dealeraces.pop(0)
            check_dealer_aces()
            break


def check_player_aces():
    # this function checks if the player has Aces and modifies the sum accordingly
    global playertotal, playeraces
    if len(playeraces) > 0:
        # when player has Aces
        while playertotal > 21:
            # if sum is more than 21 and has Aces, it subtracts 10 from the sum and checks if it needs to do it again
            playertotal -= 10
            playeraces.pop(0)
            check_player_aces()
            break


def hit_stand():
    # this function asks the player whether to hit or stand
    while True:
        response = input("(H)it or (S)tand?\n")
        if response.lower() == "hit" or response.lower() == "h":
            # if player responds with (hit, Hit, HIT, h, or H)
            return True
        elif response.lower() == "stand" or response.lower() == "s":
            # if player responds with (stand, STAND, Stand, S, s)
            return False
        else:
            # if player's response is not valid (integer or anything else not valid as a response) it asks again
            print("Not a valid response. Try again!")
            continue


def playing_again():
    # function that asks the player to play again or not
    global dealertotal, playertotal, dealeraces, playeraces, dealercards, playercards
    dealertotal, playertotal = 0, 0
    dealeraces, playeraces = [], []
    dealercards, playercards = [], []
    while True:
        response = input("Do you want to play again? [(y)es or (n)o]\n")
        if (response.lower() == "yes" or response.lower() == "y") and chips.balance != 0:
            # if player decides to play again and have the funds for it
            playing()
            break
        elif (response.lower() == "yes" or response.lower() == "y") and chips.balance == 0:
            # if player decides to play again but do not have the funds for it. it quits.
            print("Insufficient funds!")
            board.goodbye()
            break
        elif response.lower() == "no" or response.lower() == "n":
            # if player decides to stop playing
            board.goodbye()
            break
        else:
            # if response is not valid
            print("Not a valid response. Try again!")
            continue


def place_a_bet():
    # function that asks the player to place a bet
    while True:
        try:
            bet = float(input("Please place a bet:\n"))
            break
        except (ValueError, TypeError):
            print("Not a valid response. Try again!")
            continue
    if 0 < bet <= chips.balance:
        # if bet is valid (more than 0 and less than balance or funds). it places the bet
        chips.place_bet(bet)
    elif bet > chips.balance:
        # if bet is more than funds. it asks again
        print("Insufficient funds!")
        place_a_bet()
    else:
        # if response is not valid. it asks again
        print("Bet cannot be 0 or less. Try again!")
        place_a_bet()


# main game function callings
chips.starting_balance()
print(chips)

playing()




