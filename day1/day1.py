def get_fuel(mass):
    result = 0
    fuel = mass
    while (fuel := fuel//3-2) > 0:
        result += fuel

    return result

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        fuel = sum(get_fuel(int(line)) for line in f.readlines())

    print(fuel)
