class Card:
    def __init__(self, c_num, winning_nums, nums):
        self.c = c_num
        self.w = winning_nums
        self.n = nums
        self.val = 0
        self.matches = []
        for i in self.w:
            if i in self.n:
                self.matches.append(i)
        if len(self.matches) > 0:
            self.val = 2**(len(self.matches)-1)

def parse_line(line):
    s = line.split(':')
    c = int(s[0].split(' ')[-1].strip())
    dat = s[1].split('|')
    return Card(
        c,
        [int(i) for i in dat[0].split(' ') if i.isnumeric()],
        [int(i) for i in dat[1].split(' ') if i.isnumeric()]
    )

def recursive_check(cards, val, mults):
    res = 1
    for i in range(len(cards[val-1].matches)):
        res += mults[val]
        mults[val+i+1] += mults[val]
    return res, mults

def main():
    cards = []
    with open('dat.txt', 'r') as f:
        l = f.readlines()
        for i in l:
            cards.append(parse_line(i[:-1]))
    card_val_sum = 0
    for card in cards:
        card_val_sum += card.val
    print(card_val_sum)

    total_cards = 0
    card_mults = {c.c:1 for c in cards}
    for card in cards:
        ccc = recursive_check(cards, card.c, card_mults)
        total_cards += ccc[0]
        card_mults = ccc[1]
    print(total_cards)

if __name__ == "__main__":
    main()