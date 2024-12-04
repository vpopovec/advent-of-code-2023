import re

with open('input.txt') as rf:
    txt = rf.readlines()

cards = [c for c in txt if c.strip()]
print(len(cards), cards[0])
cards_total = {indx: 1 for indx, card in enumerate(cards)}

for card_indx, card in enumerate(cards):
    card_num = re.findall(r'\d+', card)[0]
    my_nums = re.findall(r'\d+', card.split(':')[1].split('|')[0])
    winning_nums = re.findall(r'\d+', card.split('|')[1])
    print(f"{card_num=} {my_nums=} {winning_nums=}")

    card_matches = 0
    for my_num in my_nums:
        if my_num in winning_nums:
            card_matches += 1

    # For each copy of this card
    for i in range(cards_total[card_indx]):
        # print(f"{i=}")
        for subseq_indx in range(card_indx + 1, card_indx + card_matches + 1):
            # print(f"{subseq_indx=}")
            cards_total[subseq_indx] += 1

print(f"{cards_total=}")
print(sum(cards_total.values()))