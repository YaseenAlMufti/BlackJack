

hhh = []
jjj = ""

card = ["diamond", "ace", "11"]
card2 = ["heart", "Five", "5"]
card3 = ["Clubs", "Queen", "10"]
card4 = ["Spades", "King", "10"]

hhh.append(card)
hhh.append(card2)
hhh.append(card3)
hhh.append(card4)


def call_card():
    for item in hhh:
        print("###############    ", sep=" ", end="", flush=True)

    print("")

    for item in hhh:
        print(f"#  {item[1]} of  #      ", sep=" ", end="", flush=True)

    print("")

    for item in hhh:
        print(f"#  {item[0]}  #       ", sep=" ", end="", flush=True)

    print("")

    for item in hhh:
        print("###############    ", sep=" ", end="", flush=True)

    print("")


call_card()





