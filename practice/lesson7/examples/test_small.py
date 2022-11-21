# Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa.
# Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec,
# pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec,
# vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis
# pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo
# ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a,
"""Example code"""


# comment
def read_data_from_file(filename: str):
    """Read lines from txt file"""
    result = []
    # comment
    with open(filename, 'r') as file:  # comment
        for line in file:
            line = line.strip()
            if line:
                result.append(line)
    return result


def write_line_count_file(filename: str, data_to_write):
    """Write lines count to file"""
    with open(filename, 'w') as file:
        for counter, data in enumerate(data_to_write, start=1):  # comment
            file.write(f'{counter}. {data}\n') # comment


# comment
def main(filename):
    """Main controller"""
    data = read_data_from_file(filename)
    write_line_count_file(filename, data)


if __name__ == '__main__':
    # comment
    main('example.txt')  # comment


