def read_file_lines():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    return lines

def main():
    lines = read_file_lines()

if __name__ == '__main__':
    main()
