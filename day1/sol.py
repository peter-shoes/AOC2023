def convert_line(line):
    nums = []
    literals = ['one','two','three','four','five','six','seven','eight','nine']
    for i in range(len(line)):
        if line[i].isnumeric():
            nums.append(int(line[i]))
            continue
        else:
            for j in literals:
                if line[i] == j[0]:
                    matched = True
                    for k in range(len(j)):
                        try:
                            if line[i+k] != j[k]:
                                matched = False
                        except:
                            matched = False
                    if matched:
                        nums.append(literals.index(j)+1)

    final = f'{nums[0]}{nums[-1]}'
    return int(final)

def main():
    s = 0
    with open('dat.txt', 'r') as f:
        lines = f.readlines()
        for l in lines:
            s += convert_line(l)
    print(s)



if __name__ == "__main__":
    main()