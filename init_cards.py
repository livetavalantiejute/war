def init_cards():
    numbers = range(1, 14)
    letters = ["J", "Q", "K", "A"]
    suites = ["heart", "tile", "clover", "spade"]
    values = []

    for suite in suites:
        for card in numbers:
            if card < 10:
                values.append({f"{str(card)} {suite.title()}": card})
            else:
                helper = numbers[-4:]

        for i, value in enumerate(helper):
            values.append({f"{letters[i]} {suite.title()}": value})

    return values