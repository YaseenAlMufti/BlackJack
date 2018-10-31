
class Board:

    def __init__(self):
        pass

    def print_card(self, dcards, pcards):
        # Prints the card with the whole board
        print("\n" * 50)
        self.greetings()
        # prints dealer's cards
        print("Dealer Cards:")
        for item in dcards:
            print("###############    ", sep=" ", end="", flush=True)

        print("")

        for item in dcards:
            print(f"#  {item[1]} of  #      ", sep=" ", end="", flush=True)

        print("")

        for item in dcards:
            print(f"#  {item[0]}  #       ", sep=" ", end="", flush=True)

        print("")

        for item in dcards:
            print("###############    ", sep=" ", end="", flush=True)

        print("\n")

        # prints player's cards
        print("Your Cards:")
        for item in pcards:
            print("###############    ", sep=" ", end="", flush=True)

        print("")

        for item in pcards:
            print(f"#  {item[1]} of  #      ", sep=" ", end="", flush=True)

        print("")

        for item in pcards:
            print(f"#  {item[0]}  #       ", sep=" ", end="", flush=True)

        print("")

        for item in pcards:
            print("###############    ", sep=" ", end="", flush=True)

        print("")

    def greetings(self):
        # prints a greeting for the game
        print("#################################################")
        print("#    Welcome to BlackJack by Yaseen Al Mufti    #")
        print("#################################################")

    def lost(self):
        # prints lost banner
        print("### You Lost!! ###")

    def win(self):
        # prints win banner
        print("### You Won!! ###")

    def goodbye(self):
        # prints goodbye banner at end of game
        print("########################")
        print("#  Thanks for playing  #")
        print("########################")

