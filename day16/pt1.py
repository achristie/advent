packets = [
    bin(int("1" + h, 16))[3:] for h in open("input_test.txt").read().splitlines()
]


class Packet:
    def __init__(self, p):
        self.version = p[:3]
        self.type_id = p[3:6]
        self.type = "Literal" if self.type_id == "100" else "Operator"
        self.length_type_id = None if self.type == "Literal" else p[6]
        self.sp_length = None if self.type == "Literal" else p[7:22]
        self.value, self.rest = (
            self.parse_value(p[6:])
            if self.type == "Literal"
            else self.parse_value(p[22:])
        )
        # self.rest = p[22:] if self.type == "Operator" else p[6:]
        # self.value = None if self.type == "Operator" else

    def parse_value(self, p):
        num = ""
        rest = ""
        if self.type == "Operator":
            return None, p
        for x in range(0, len(p), 5):
            cont, b = int(p[x]), p[x + 1 : x + 5]
            if len(b) == 4:
                num += b
            if not cont:
                rest = p[x + 5 :]
                break
        return num, rest

    def __str__(self):
        return f"version - {self.version} \ntype id - {self.type_id} \ntype - {self.type}\nlength - {self.length_type_id}\nsp length - {self.sp_length}\nvalue - {self.value}\nrest - {self.rest}\n"


# parse_packet(data[0])

# print(Packet(data[0]))


def run(packets):
    p = Packet(packets)
    versions = []

    while True:
        if len(p.rest) == 0:
            break

        versions.append(p.version)
        p = Packet(p.rest)

    return versions


print(run(packets[1]))
