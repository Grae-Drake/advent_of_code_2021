import argparse
import math


def get_data(data_path):
    with open(data_path) as file:
        return [line.rstrip() for line in file.readlines()]


def leftpad(binstr, expected_length):
    return '0' * (expected_length - len(binstr)) + binstr


def hex_to_bin(hex_str):
    raw_binary = bin(int(hex_str, 16))[2:]
    return leftpad(raw_binary, len(hex_str) * 4)


def value(packet):
    operation = packet.type_ID
    operations = [
        lambda arguments: sum(arguments),
        lambda arguments: math.prod(arguments),
        lambda arguments: min(arguments),
        lambda arguments: max(arguments),
        None,
        lambda arguments: 1 if arguments[0] > arguments[1] else 0,
        lambda arguments: 1 if arguments[0] < arguments[1] else 0,
        lambda arguments: 1 if arguments[0] == arguments[1] else 0
    ]
    if operation == 4:
        return packet.literal
    else:
        return operations[operation]([value(child) for child in packet.children])


class Packet():

    def __init__(self, binary):
        self.version = int(binary[:3], 2)
        self.type_ID = int(binary[3:6], 2)
        self.children = []
        
        if self.type_ID != 4:
            self.length_type_ID = int(binary[6:7])
            pointer = 7
            
            # Handle operators with a set length.
            if self.length_type_ID == 0:
                sub_packets_length = int(binary[pointer: pointer + 15], 2)
                pointer += 15
                sub_packets_end = pointer + sub_packets_length
                while pointer < sub_packets_end:
                    child = Packet(binary[pointer: sub_packets_end])
                    pointer += child.length
                    self.children.append(child)
            
            # Handle operators with a set number of sub-packets.
            elif self.length_type_ID == 1:
                child_count = int(binary[pointer: pointer + 11], 2)
                pointer += 11
                while len(self.children) < child_count:
                    child = Packet(binary[pointer:])
                    pointer += child.length
                    self.children.append(child)
        
        # Handle literals
        else:
            pointer = 6
            bits = []
            end = 1
            while end:
                end = int(binary[pointer])
                for i in range(1, 5):
                    bits.append(binary[pointer + i])
                pointer += 5
            self.literal = int(''.join(bits), 2)

        self.length = pointer


def main(data_path):
    bin_data = [hex_to_bin(line) for line in get_data(data_path)]

    results = []
    for message in bin_data:
        packet = Packet(message)
        results.append(packet)
    return [value(result) for result in results]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Day 16')
    parser.add_argument('-t', dest='test', action='store_true',
                        help='use test data (default: use real data)')
    args = parser.parse_args()
    day = 16
    data_path = 'data/day' + str(day) + ('_test' if args.test else '') + '.txt'
    print(main(data_path))
