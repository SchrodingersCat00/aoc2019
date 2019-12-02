import copy

def read_file_lines():
    with open('input.txt', 'r') as f:
        l = f.readline().strip().split(',')

    return [int(i) for i in l]


def process_list(l, i):
    if l[i] == 1:
        l[l[i+3]] = l[l[i+1]] + l[l[i+2]]
    elif l[i] == 2:
        l[l[i+3]] = l[l[i+1]] * l[l[i+2]]


def run_program(l):
    i = 0
    while i < len(l):
        process_list(l, i)
        i += 4

    return l


def main():
    l = read_file_lines()
    acopy = copy.copy(l)
    for i in range(173):
        for j in range(173):
            l = copy.copy(acopy)
            l[1] = i
            l[2] = j
            run_program(l)
            if l[0] == 19690720:
                print(i, j)

if __name__ == '__main__':
    main()
