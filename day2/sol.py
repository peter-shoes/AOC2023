def parse(line):
    s = line.split(':')
    id = int(s[0].split(' ')[1])
    games_raw = s[1].split(';')
    games = []
    for game in games_raw:
        game_dat = {'blue':0, 'green':0, 'red':0}
        draws_raw = game.split(',')
        for d in draws_raw:
            draw = d.strip().split(' ')
            game_dat[draw[1]] = int(draw[0])
        games.append(game_dat)
    return id, games

def possible(games):
    valid = True
    for game in games:
        if game['red'] > 12 or game['blue'] > 14 or game['green'] > 13:
            valid = False
    return valid

def calc_power(games):
    power = 1
    mins = {'blue':0, 'green':0, 'red':0}
    for game in games:
        for m in mins:
            if game[m] > mins[m]:
                mins[m] = game[m]
    for m in mins:
        power *= mins[m]
    return power



def main():
    sum = 0
    sum_power = 0
    with open('dat.txt', 'r') as f:
        lines = f.readlines()
        games = []
        for l in lines:
            games.append(parse(l))
    for g in games:
        if possible(g[1]):
            sum += g[0]
        sum_power += calc_power(g[1])
    print(sum)
    print(sum_power)


if __name__ == "__main__":
    main()