from rtl.parser.helpers import helper_create_global_char_array


class Host:
    LINE_TRIGGER = "host"

    def __init__(self, id, address):
        self.id = id
        self.address = address

    @classmethod
    def parse(cls, tokens, fh):

        id = tokens[1]
        address = False

        while True:
            line = fh.readline().strip()

            if line == "":
                break

            line_tokens = line.split(" ")

            if line_tokens[0] == "address":
                address = "".join(line_tokens[1:])

        return cls(id, address)

    def IR(self, builder):
        helper_create_global_char_array(builder.module, self.id, self.address)
