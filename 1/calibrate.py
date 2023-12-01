import re

word_digits = {'one': 1, 'two': 2, 'three': 3,
               'four': 4, 'five': 5, 'six': 6,
               'seven': 7, 'eight': 8, 'nine': 9}


def calibrate(ln):
    word_positions_start, word_positions_end = {}, {}
    for word, number in word_digits.items():
        try:
            # Scan the string from the end
            for i in range(1, len(ln)+1):
                if word in ln[-i:]:
                    indx = len(ln) - i
                    word_positions_end[indx] = word
                    break
            indx = ln.index(word)
            word_positions_start[indx] = word
        except ValueError:
            continue

    digits = re.findall(r"\d", ln)

    if digits and word_positions_start:
        first_index_word = min(word_positions_start.keys())
        word_in_digit = word_digits[word_positions_start[first_index_word]]
        first_index_digit = ln.index(digits[0])
        digit_comes_first = min(first_index_digit, first_index_word) == first_index_digit
        first_digit = digits[0] if digit_comes_first else word_in_digit

        last_index_word = max(word_positions_end.keys())
        word_in_digit = word_digits[word_positions_end[last_index_word]]
        last_index_digit = len(ln) - ln[::-1].index(digits[-1]) - 1
        digit_comes_last = max(last_index_digit, last_index_word) == last_index_digit
        last_digit = digits[-1] if digit_comes_last else word_in_digit
        return int(f"{first_digit}{last_digit}")

    elif digits and not word_positions_start:
        if len(digits) >= 2:
            return int(f"{digits[0]}{digits[-1]}")
        elif len(digits) == 1:  # only one digit
            return int(f"{digits[0]}{digits[0]}")

    elif word_positions_start:
        least_index_word = min(word_positions_start.keys())
        first_digit = word_digits[word_positions_start[least_index_word]]
        last_index_word = max(word_positions_end.keys())
        last_digit = word_digits[word_positions_end[last_index_word]]
        return int(f"{first_digit}{last_digit}")

    return 0


if __name__ == '__main__':
    with open('calibration.txt') as rf:
        lns = rf.readlines()

    total = 0
    for ln in lns:
        print(f"{ln=} {calibrate(ln)}")
        total += calibrate(ln)
    print(f"{total=}")

