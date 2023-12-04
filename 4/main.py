import re

with open('input.txt') as rf:
    txt = rf.readlines()

cards = [c for c in txt if c.strip()]
print(len(cards), cards[0])
total_points = 0
for card in cards:
    card_num = re.findall(r'\d+', card)[0]
    my_nums = re.findall(r'\d+', card.split(':')[1].split('|')[0])
    winning_nums = re.findall(r'\d+', card.split('|')[1])
    print(f"{card_num=} {my_nums=} {winning_nums=}")
    card_value = 0
    for my_num in my_nums:
        if my_num in winning_nums:
            if card_value != 0:
                # Subsequent winning numbers
                card_value *= 2
            else:
                # First winning number
                card_value = 1
    print(f"{card_value=}")
    total_points += card_value

print(f"{total_points=}")
