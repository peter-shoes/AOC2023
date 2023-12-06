class ConversionBlock:
    def __init__(self, data):
        self.type = data[0][:-1]
        self.data = data[1:]
        self.srcs = [int(i[1]) for i in [j.split(' ') for j in self.data[:-1]]]
        self.dsts = [int(i[0]) for i in [j.split(' ') for j in self.data[:-1]]]
        self.rngs = [int(i[2]) for i in [j.split(' ') for j in self.data[:-1]]]

def pt1(data, vals):
    for line in data[2:]:
        # remove newlines
        line = line[:-1]
        if not line:
            continue
        if not line[0].isnumeric():
            new_vals = {}
            for v in vals:
                new_vals[vals[v]] = vals[v]
            vals = new_vals
            
        else:
            line_c = [int(j) for j in line.split(' ')]
            for v in vals:
                if v >= line_c[1] and v < (line_c[1] + line_c[2]):
                    vals[v] = v-line_c[1] + line_c[0]
                    break
    minn = None
    for v in vals:
        if minn  == None or vals[v] < minn:
            minn = vals[v]
    print(minn)

def pt2(data, vals):
    # for this one you have to optimize or your computer will crash
    # start by creating objects for easier work
    blocks = []
    cur_block = []
    for line in data[2:]:
        if not line[0].isnumeric() and line != '\n':
            if len(cur_block) > 0:
                blocks.append(ConversionBlock(cur_block))
            cur_block = [line]
        else:
            cur_block.append(line)
    cur_block.append(data[-1])
    blocks.append(ConversionBlock(cur_block))
    
    #convert the data
    new_vals = []
    vals = [i for i in vals]
    for i in range(0, len(vals), 2):
        new_vals.append((vals[i], vals[i+1]))
    vals = new_vals
    # iterate through your conversion sets
    new_ranges = []
    bb = 0
    for block in blocks:
        print('len vals: ', len(vals))
        print(bb,'/',len(blocks))
        bb+= 1
        # for each seed range, check which sets are being used
        for val in vals:
            # print(val)
            for i in range(len(block.srcs)):
                if val[0] >= block.srcs[i] and val[0] < block.srcs[i]+block.rngs[i]:
                    if (val[0] + val[1]) <= block.srcs[i]+block.rngs[i]:
                        new_range = (
                            val[0]-block.srcs[i] + block.dsts[i],
                            val[0]+val[1]-block.srcs[i] + block.dsts[i]
                        )
                        new_ranges.append(new_range)
                    else:
                        new_range = (
                            val[0]-block.srcs[i] + block.dsts[i],
                            block.rngs[i] + block.dsts[i]
                        )
                        new_ranges.append(new_range)
                        vals.append((block.srcs[i]+block.rngs[i]+1, val[0] + val[1]))
        vals = new_ranges
        new_ranges = []
        # return
    minn = None
    for i in vals:
        if minn == None or i[0] < minn:
            minn = i[0]
    print(minn)
    

def main():
    data = []
    with open('dat.txt', 'r') as f:
        data = f.readlines()
    vals = {int(i):int(i) for i in (data[0][:-1].split(':')[1][1:].split(' '))}
    pt1(data, vals)
    pt2(data, vals)




            

if __name__ == "__main__":
    main()