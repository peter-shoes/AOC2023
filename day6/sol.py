def calc_ways(time, goal):
    w = 0
    for t in range(time):
        test = t * (time-t)
        if test > goal:
            w += 1
    return w

def optimized_calc_ways(time, goal):
    # Not used
    min_hold = 0
    for t in range(time):
        test = t*(time-t)
        if test > goal:
            min_hold = test
            break
    print(min_hold)
    print(time-min_hold)
    # binary search time
    start = min_hold
    end = time
    solved = False
    while not solved:
        middle = start + ((end-start)/2)
        if middle * (end-middle) > goal:
            start = middle
        else:
            end = middle
        if end == start:
            solved = True
    return end-min_hold

def main():
    times = []
    distances = []
    p1 = 1
    with open('dat.txt', 'r') as f:
        lines = f.readlines()
        times = [int(i) for i in lines[0].split(':')[1].split(' ') if i != '']
        distances = [int(i) for i in lines[1].split(':')[1].split(' ') if i != '']
    for i in range(len(times)):
        p1 *= calc_ways(times[i], distances[i])
    print(p1)
    
    #part 2
    single_time = int(''.join([str(i) for i in times]))
    single_dist = int(''.join([str(i) for i in distances]))
    print(calc_ways(single_time, single_dist))



if __name__ == "__main__":
    main()