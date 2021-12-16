from functools import reduce

import bitstring
from operator import mul

with open('day_16.txt', 'r') as lines:
    data = bitstring.BitStream(f"0x{next(lines).strip()}")


class Packet:
    def __init__(self, version):
        self.version = version

    def versions(self):
        return self.version


class LiteralValue(Packet):
    def __init__(self, version, value):
        self.version = version
        self.value = value


class Operator(Packet):
    def __init__(self, version, packet_type, sub_packets):
        self.version = version
        self.packet_type = packet_type
        self.sub_packets = sub_packets

    def versions(self):
        return self.version + sum([p.versions() for p in self.sub_packets])

    @property
    def value(self):
        values = [p.value for p in self.sub_packets]
        if self.packet_type == 0:
            return sum(values)
        elif self.packet_type == 1:
            return reduce(mul, values, 1)
        elif self.packet_type == 2:
            return min(values)
        elif self.packet_type == 3:
            return max(values)
        elif self.packet_type == 5:
            return 1 if values[0] > values[1] else 0
        elif self.packet_type == 6:
            return 1 if values[0] < values[1] else 0
        else:
            return 1 if values[0] == values[1] else 0


def parse_package(byte_stream):
    if byte_stream.len - byte_stream.pos < 6:
        return

    vb = byte_stream.read('bin:3')
    version = int(vb, 2)
    packet_type = int(byte_stream.read('bin:3'), 2)
    #print(f"version {version}, type {packet_type}")
    if packet_type == 4:
        """Literal value"""
        last = False
        value = ''
        while not last:
            values = byte_stream.readlist('bin:1, bin:4')
            last = True if values[0] == '0' else False
            value += values[1]
        return LiteralValue(version, int(value, 2))
    else:
        """Operator package"""
        packets = []
        if byte_stream.read('bin:1') == '0':
            length = int(byte_stream.read('bin:15'), 2)
            sub_data = byte_stream.read(f'bin:{length}')
            sub = bitstring.BitStream("0b"+sub_data)
            while True:
                packet = parse_package(sub)
                if not packet:
                    break
                else:
                    packets.append(packet)
        else:
            num_packs = int(byte_stream.read('bin:11'), 2)
            for i in range(0, num_packs):
                packets.append(parse_package(byte_stream))
        return Operator(version, packet_type, packets)


packet = parse_package(data)
print("Part 1: {}".format(packet.versions()))
print("Part 2: {}".format(packet.value))
