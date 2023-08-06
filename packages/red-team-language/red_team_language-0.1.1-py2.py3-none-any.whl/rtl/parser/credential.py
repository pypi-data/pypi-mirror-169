from rtl.parser.helpers import helper_create_global_char_array


class Credential:
    LINE_TRIGGER = "credential"

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @classmethod
    def parse(cls, tokens, fh):

        id = tokens[1]
        username = False
        password = False

        while True:
            line = fh.readline().strip()

            if line == "":
                break

            line_tokens = line.split(" ")

            if line_tokens[0] == "username":
                username = "".join(line_tokens[1:])

            if line_tokens[0] == "password":
                password = "".join(line_tokens[1:])

        return cls(id, username, password)

    def IR(self, builder):
        helper_create_global_char_array(builder.module, f"{self.id}.username", bytes(self.username, "utf8"))
        helper_create_global_char_array(builder.module, f"{self.id}.password", bytes(self.password, "utf8"))
