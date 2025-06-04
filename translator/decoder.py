import numpy as np
class Decoder:
    def __init__(self, lexemes_path: str, input_path: str):
        self.input_path = input_path
        self.file = open(self.input_path, "r")

        self.wasCut = False
        self.buf = ""
        self.isLexeme = True
        self.isConst = True
        self.isIdent = True

        self.lexemesMap = {}
        with open(lexemes_path, "r") as lexemes_file:
            for i, lexeme in enumerate(lexemes_file.readlines()):
                self.lexemesMap[lexeme.rstrip()] = i + 2

        self.identifiers_map_name_code = {}
        self.identifiers_map_code_name = {}

        self.ident_start_index = -1
        self.identifiers_matrix_cursor = -1
        self.identifiers_matrix = []
        self.hash_matrix = {}

        self.parseLexemes = []

    def set_input(self, path: str) -> None:
        self.input_path = path

    def hash_func(self, ident: str) -> int:
        return sum([ord(i) for i in ident])

    def cut(self) -> None:
        self.wasCut = True
        self.buf = self.buf[-1]
        self.isLexeme = True
        self.isConst = True
        self.isIdent = True

    def show_maps(self) -> None:
        print("Identifier: 0")
        print("Constant: 1")
        print(f"Lexemes: {self.lexemesMap}")
        print("Identifiers:")
        print(self.identifiers_map_name_code)
        print(self.hash_matrix)
        print(np.array(self.identifiers_matrix))


    def is_lexeme(self) -> None:
        curLexeme = ""
        for lex in self.lexemesMap.keys():
            if self.buf in lex:
                curLexeme = lex
                if self.buf == lex:
                    self.lexeme = lex
                # break
        if curLexeme == "":
            self.isLexeme = False

    def is_const(self) -> None:
        if self.buf.isdigit():
            self.const = self.buf
        else:
            self.isConst = False

    def is_ident(self) -> None:
        if not self.buf[0].isdigit():
            for c in [",", ".", ":", ";", "-", "=", "?", "!", "*", " ", "\n", "+", "/", "(", ")"]:
                if self.buf[-1] == c:
                    self.isIdent = False
                    break
        else:
            self.isIdent = False
        if self.isIdent:
            self.ident = self.buf

    def add_ident(self, ident: str) -> None:
        h = self.hash_func(ident)
        self.identifiers_matrix_cursor += 1
        self.identifiers_matrix.append([ident, 0, 0])

        if self.ident_start_index == -1:
            self.ident_start_index = self.identifiers_matrix_cursor

        if h not in self.hash_matrix:
            self.hash_matrix[h] = self.identifiers_matrix_cursor
        else:
            index = self.hash_matrix[h]
            while self.identifiers_matrix[index][2] != 0:
                index = self.identifiers_matrix[index][2]
            self.identifiers_matrix[index][2] = self.identifiers_matrix_cursor

        if ident not in self.identifiers_map_name_code:
            self.identifiers_map_name_code[ident] = len(self.identifiers_map_name_code)
            self.identifiers_map_code_name[len(self.identifiers_map_code_name)] = ident

    def set_type_ident(self, type):
        for i in range(self.ident_start_index, len(self.identifiers_matrix)):
            self.identifiers_matrix[i][1] = type
        self.ident_start_index = -1

    def read_lexeme(self):
        def reset():
            self.lexeme = ""
            self.const = ""
            self.ident = ""

        while True:
            if not self.wasCut:
                ch = self.file.read(1)
                if not ch:
                    break
                self.buf += ch

            # Проверка на лексему
            self.is_lexeme()
            # Проверка на константу
            self.is_const()
            # Проверка на идентификатор
            self.is_ident()

            if not self.isLexeme and not self.isConst and not self.isIdent:
                # Лексема
                if self.lexeme != "":
                    if self.lexeme in ['целые', 'вещественные']:
                        self.set_type_ident(self.lexeme)
                    lexeme = self.lexeme
                    reset()
                    self.cut()
                    return self.lexemesMap[lexeme]
                # Константа
                elif self.const != "":
                    constant = self.const
                    reset()
                    self.cut()
                    return [1, int(constant)]
                # Идентификатор
                elif self.ident != "":
                    ident = self.ident
                    self.add_ident(self.ident)
                    reset()
                    self.cut()
                    return [0, self.identifiers_map_name_code[ident]]
                else:
                    if self.wasCut and len(self.buf) == 1:
                        self.wasCut = False
                    elif len(self.buf) > 1:
                        reset()
                        self.cut()
            elif self.wasCut:
                self.wasCut = False