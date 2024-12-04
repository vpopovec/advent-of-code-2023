with open('input.txt') as rf:
    txt = [ln.strip().replace('JJJJJ', '00000') \
           .replace('A', 'Z') \
            .replace('K', 'Y') \
           .replace('Q', 'X') \
            .replace('J', '0')
           for ln in rf.readlines()]

print(f"{txt=}")

cards = {strength: [] for strength in range(1, 8)}
for ln_indx, ln in enumerate(txt):
    five_cards, bid_amount = ln.split()
    strength = 1
    without_joker = five_cards.replace('0', '')
    hand = {c: without_joker.count(c) for c in without_joker}
    # For replacing consider card with highest max, then highest ordering

    try:
        hand_max = max(hand.values())
        hand_max_chars = [k for k in hand if hand[k] == hand_max]
        faked = five_cards.replace('0', max(hand_max_chars))
    except ValueError:
        faked = '00000'
    hand = {c: faked.count(c) for c in faked}
    print(f"{hand} {faked=}")

    if max(hand.values()) == 5:
        strength = 7
    elif max(hand.values()) == 4:
        strength = 6
    elif max(hand.values()) == 3 and min(hand.values()) == 2:
        strength = 5
    elif max(hand.values()) == 3 and min(hand.values()) == 1:
        strength = 4
    elif sorted(hand.values()) == [1, 2, 2]:
        strength = 3
    elif sorted(hand.values()) == [1, 1, 1, 2]:
        strength = 2
    elif sorted(hand.values()) == [1, 1, 1, 1, 1]:
        strength = 1
    print(f"{strength=}")

    cards[strength].append((five_cards, bid_amount))

    # cards[ln_indx] = {'cards': five_cards,
    #                   'total': bid_amount * rank}


# Replace chars to be better sorted?

print(f"{cards=}")
rank = 0
cards_ranked = {}
for strength in range(1, 8):
    # lowest_card = ('ZZZZZ', '100')
    # while cards[strength]:
        # for card, bid in cards[strength]:
        #     for i in range(5):
        #         if card[i] < lowest_card[0][i]:
        #             lowest_card = card, bid
        # # print(f"{lowest_card=} {strength=} {cards} {cards_ranked}")
        # if lowest_card not in cards[strength]:  # END
        #     lowest_card = cards[strength].pop()
        #     print('FINAL LOW', lowest_card)
        # if lowest_card in cards[strength]:
        #     cards[strength].remove(lowest_card)
    for card, bid in sorted(cards[strength], key=lambda x: x[0]):
        rank += 1
        cards_ranked[rank] = card, bid
print(f"{cards_ranked=}")

ttl = 0
for rank, (card, bid) in cards_ranked.items():
    ttl += int(bid) * rank
    print(rank-1, card, bid)
print(ttl)
