from itertools import combinations
import copy

class Moon:
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel


def read_file_lines():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    return lines


def update_velocity(moons):
    new_moons = copy.copy(moons)
    for a, b in combinations(range(4), 2):
        for a_pos, b_pos, index in zip(moons[a].pos, moons[b].pos, range(3)):
            if a_pos < b_pos:
                new_moons[a].vel[index] += 1
                new_moons[b].vel[index] -= 1
            elif a_pos > b_pos:
                new_moons[a].vel[index] -= 1
                new_moons[b].vel[index] += 1
    
    return new_moons
            

def update_positions(moons):
    moons = copy.copy(moons)
    
    for moon in moons:
        for i in range(len(moon.vel)):
            moon.pos[i] += moon.vel[i]

    return moons


def get_period(coords):
    start = coords[0]
    i = 0
    for coord in coords[1:]:
        i += 1
        if coord == start:
            return i
    
    raise ValueError("No period was found")

def generate_state(starting_state):
    moons = starting_state
    yield moons
    while True:
        moons = copy.deepcopy(moons)
        moons = update_velocity(moons)
        moons = update_positions(moons)
        yield moons


def potential_energy(moons):
    def abs_sum(l):
        return sum(abs(x) for x in l)
    return sum(abs_sum(moon.vel) * abs_sum(moon.pos) for moon in moons)


def part1(moons):
    for _ in range(1000):
        moons = update_velocity(moons)
        moons = update_positions(moons)
    
    print(potential_energy(moons))


def part2(moons):
    states = []
    gen = generate_state(moons)
    for _ in range(999999):
        states.append(next(gen))
    # state = [moonA, moonB, moonC, moonD]
    periods = [
        get_period(
            [
                tuple(moon.pos[i] for moon in state) + tuple(moon.vel[i] for moon in state) 
                for state in states
            ]
        ) for i in range(3)
    ]
    for period in periods:
        print(period)


def compute_lcm(x, y):
   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm


def parse_moon(line):
    vel = [0, 0, 0]
    pos = list(int(part.split('=')[1]) for part in line.split(','))

    return Moon(pos, vel)


def main():
    lines = read_file_lines()
    moons = [parse_moon(line.strip().rstrip('>')) for line in lines]
    part2(moons)


if __name__ == '__main__':
    main()
