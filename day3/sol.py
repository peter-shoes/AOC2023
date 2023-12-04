class num_dat:
    def __init__(self, n, locs, row):
        self.val = n
        self.locs = []
        for i in locs:
            self.locs.append((row, i))

class sym_dat:
    def __init__(self, loc, sym, row):
        self.sym = sym
        self.loc = (row,loc)
        self.neighbors = [
            (row,loc-1),
            (row,loc+1),
            (row-1,loc),
            (row+1,loc),
            (row+1,loc+1),
            (row+1,loc-1),
            (row-1,loc+1),
            (row-1,loc-1)
        ]
        self.gear_neighbor_vals = []


def parse_line(line, row):
    num_mem = []
    loc_mem = []
    num_data = []
    sym_data = []
    for i in range(len(line)):
        if line[i].isnumeric():
            num_mem.append(line[i])
            loc_mem.append(i)
        else:
            if len(num_mem) > 0:
                num_data.append(num_dat(int(''.join(num_mem)), loc_mem, row))
                num_mem = []
                loc_mem = []
            if line[i] != '.' and line[i] != '\n':
                sym_data.append(sym_dat(i, line[i], row))
    if row == 0:
        for i in sym_data:
            print(i.loc)
    return num_data, sym_data
        

def main():
    data_sum = 0
    gear_ratio_sum = 0
    num_data = []
    sym_data = []
    with open('dat.txt', 'r') as f:
        data = f.readlines()
        for line in range(len(data)):
            d = parse_line(data[line], line)
            for i in d[0]:
                num_data.append(i)
            for i in d[1]:
                sym_data.append(i)
    for sd in sym_data:
        for nd in num_data:
            added = False
            for sn in sd.neighbors:
                if sn in nd.locs and not added:
                    data_sum+= nd.val
                    added = True
                    if sd.sym == '*':
                        sd.gear_neighbor_vals.append(nd.val)

    for sd in sym_data:
        if len(sd.gear_neighbor_vals) == 2:
            gear_ratio_sum += (sd.gear_neighbor_vals[0] *sd.gear_neighbor_vals[1])
    print(data_sum)
    print(gear_ratio_sum)
                        

    
                
    


if __name__ == "__main__":
    main()