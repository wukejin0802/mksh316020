#Github-22
cards = []
for i in range(5):
    card = input(f"請輸入第 {i+1} 張牌（數字或 A/J/Q/K）: ")
    card = card.upper()
    if card == 'A':
        value = 1
    elif card == 'J':
        value = 11
    elif card == 'Q':
        value = 12
    elif card == 'K':
        value = 13
    else:
        value = int(card)
        cards.append(value)
total = sum(cards)
print("你輸入的 5 張牌總和為：", total)