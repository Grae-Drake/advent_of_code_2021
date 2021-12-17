import argparse
from typing_extensions import Literal


def get_data(data_path):
    with open(data_path) as file:
        return [line.rstrip() for line in file.readlines()]


def leftpad(binstr, expected_length):
    return '0' * (expected_length - len(binstr)) + binstr


def hex_to_bin(hex_str):
    raw_binary = bin(int(hex_str, 16))[2:]
    return leftpad(raw_binary, len(hex_str) * 4)


class Packet():

    def __init__(self, binary):
        self.version = int(binary[:3], 2)
        self.type_ID = int(binary[3:6], 2)
        self.children = []
        
        if self.type_ID != 4:
            print("Handling an operator. Packet info:")
            print("Packet bits:\n{}".format(binary))
            print("Version: {}".format(self.version))
            print("type_ID: {}".format(self.type_ID))
            self.length_type_ID = int(binary[6:7])
            print("length_type_ID: {}".format(self.length_type_ID))
            pointer = 7
            
            # Handle operators with a set length.
            if self.length_type_ID == 0:
                sub_packets_length = int(binary[pointer: pointer + 15], 2)
                pointer += 15
                sub_packets_end = pointer + sub_packets_length
                print('Sub Packet(s) length: {}'.format(sub_packets_length))
                print("Sub packet(s) binary: {}".format(binary[pointer: sub_packets_end]))
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
            print('Handling a literal. Packet info:')
            print(binary)
            print("Version: {}".format(self.version))
            print("type_ID: {}".format(self.type_ID))
            pointer = 6
            print("Literal bits:\n{}".format(binary[pointer:]))
            bits = []
            end = 1
            while end:
                print("Bits: {}".format(bits))
                end = int(binary[pointer])
                print(end)
                for i in range(1, 5):
                    bits.append(binary[pointer + i])
                pointer += 5
            self.literal = int(''.join(bits), 2)
            print("Literal value: {}".format(self.literal))
            # Need to figure out how to handle the "extra" zeros at the end of a literal.

        self.length = pointer


def packet_version_sum(packet):
    return packet.version + sum([packet_version_sum(child) for child in packet.children])


def main(data_path):
    bin_data = [hex_to_bin(line) for line in get_data(data_path)]

    results = []
    for message in bin_data:
        print("\n------ New Test ------")
        packet = Packet(message)
        results.append(packet)
    return [packet_version_sum(result) for result in results]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Day 16')
    parser.add_argument('-t', dest='test', action='store_true',
                        help='use test data (default: use real data)')
    args = parser.parse_args()
    day = 16
    data_path = 'data/day' + str(day) + ('_test' if args.test else '') + '.txt'
    print(main(data_path))
