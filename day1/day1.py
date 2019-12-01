def get_fuel(mass):
    fuel = 0
    while (mass := mass//3-2) > 0:
        fuel += mass

    return fuel

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        fuel = sum(get_fuel(int(line)) for line in f.readlines())

    print(fuel)
