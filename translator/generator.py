class PostfixGenerator:
    def __init__(self, postfix_notation: str):
        self.postfix_notation = postfix_notation.split(" ")
        self.index_ident = 1

        self.a = {
            "читать": "read",
            "печатать": "write",
            "вещественные": "real",
            "целые": "integer",
        }

    def generate(self, start_index):
        stack = []
        code = ""
        index = start_index
        while index < len(self.postfix_notation):
            token = self.postfix_notation[index]
            if token == "программа":
                name_program = stack.pop()
                code += f"program {name_program};\n"
            elif token == "var":
                index += 1
                code_indent = ""
                identifiers = []
                while token != ")":
                    index += 1
                    token = self.postfix_notation[index]
                    if token in ["вещественные", "целые"]:
                        identifiers_str = ", ".join(identifiers)
                        code_indent += f"{identifiers_str}: {self.a[token]};\n"
                        identifiers = []
                    else:
                        identifiers.append(token)
                code += f"var\n{code_indent}begin\n"
            elif token == ":=":
                val = stack.pop()
                dest = stack.pop()
                code += f"{dest} := {val};\n"
            elif token == "читать":
                ident = stack.pop()
                code += f"read({ident});\n"
            elif token == "печатать":
                ident = stack.pop()
                code += f"write({ident});\n"
            elif token == "пока":
                # code_fragments[index_code_fragment]
                loop_expression, index = self.generate(index+1)
                loop_body, index = self.generate(index+1)
                code += f"while ({loop_expression}) do\nbegin\n{loop_body}end;\n"
            elif token in ["+", "-", "/", "*"]:
                ident2 = stack.pop()
                ident1 = stack.pop()
                # code += f"T{self.index_ident} := {ident1}{token}{ident2};\n"
                stack.append(f"{ident1}{token}{ident2}")
                self.index_ident += 1
            elif token in ["=", "!=", ">", ">=", "<", "<="]:
                ident2 = stack.pop()
                ident1 = stack.pop()
                code += f"{ident1}{token}{ident2}"
            elif token == ")" and start_index != 0:
                break
            else:
                stack.append(token)
            index += 1
        if start_index == 0:
            code += "end."

        return code, index

