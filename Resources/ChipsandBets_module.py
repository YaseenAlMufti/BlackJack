
class ChipsAndBets:

    def __init__(self, balance=100, bet=0):
        self.balance = balance
        self.bet = bet
        self.balance_statement()

    def place_bet(self, placed_bet):
        # sets the bet
        self.bet = placed_bet
        print("Bet Placed!")

    def win_bet(self):
        # adds the winning bet to balance
        self.balance += self.bet
        self.balance_statement()

    def lose_bet(self):
        # subtracts bet from the balance
        self.balance -= self.bet
        self.balance_statement()

    def balance_statement(self):
        # prints the balance
        print(f"Your balance is: ${self.balance}")

    def __str__(self):
        return f"Your balance is: ${self.balance}"

    def starting_balance(self):
        # function that sets the balance at the beginning of the game
        while True:
            try:
                balance = float(input("Starting balance: \n"))
                if balance > 0:
                    self.balance = balance
                    break
                else:
                    print("Balance have to be more than 0!")
                    continue
            except (ValueError, TypeError):
                print("Invalid Value!")

