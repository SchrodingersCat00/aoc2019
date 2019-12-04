
def read_file_lines():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    return lines


def part1():
    count = 0
    for i in range(235741, 706948):
        try:
            for c, nc in zip(str(i), str(i)[1:]):
                if int(c) > int(nc):
                    raise ValueError
        except ValueError:
            continue
        for c, nc in zip(str(i), str(i)[1:]):
            if int(c) == int(nc):
                count += 1
                break

    return count


def part2():
    count = 0
    for i in range(235741, 706948):
        try:
            for c, nc in zip(str(i), str(i)[1:]):
                if int(c) > int(nc):
                    raise ValueError
        except ValueError:
            continue

        i_str = str(i)

        j = 0

        while j < len(i_str):
            group = 1
            while j + group < len(i_str) and i_str[j] == i_str[j+group]:
                group += 1
            if group == 2:
                count += 1
                print(i)
                break

            j += group

    return count


def main():
    print(part2())

if __name__ == '__main__':
    main()
