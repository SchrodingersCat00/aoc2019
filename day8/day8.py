import math

def read_file_lines():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    return lines


def part1(image, width, height):
    mini = [math.inf]
    size = width * height
    layers = [image[i:i+size] for i in range(0, len(image), size)]
    for layer in layers:
        counts = [0, 0, 0]
        for number in layer:
            if number in ['0', '1', '2']:
                counts[int(number)] += 1
        if counts[0] < mini[0]:
            mini = counts

    return mini[1] * mini[2]


def part2(image, width, height):
    size = width * height
    layers = [list(image[i:i+size]) for i in range(0, len(image), size)]
    result = layers[0]
    for layer in layers:
        for i in range(size):
            layer_pix = layer[i]
            result_pix = result[i]
            if result_pix == '2':
                result[i] = layer_pix

    parts = [''.join(['█' if pixel == '1' else ' ' for pixel in result[i:i+width]]) for i in range(0, len(result), width)]

    return '\n'.join(parts)


def main():
    lines = read_file_lines()
    print(part2(lines[0].strip(), 25, 6))

if __name__ == '__main__':
    main()
