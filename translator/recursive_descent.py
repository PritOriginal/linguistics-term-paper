from translator.decoder import Decoder


class RecursiveDescent:
    def __init__(self, input_path: str):
        self.lexemes = []
        self.lexemes.append(0)

        self.cursor = 1
        self.postfix_notation = []

        self.decoder = Decoder("lexemes.txt", input_path)
        self.lexemesMap = self.decoder.lexemesMap
        self.identifiersMap = self.decoder.identifiers_map_code_name

        self.lexemes.append(self.decoder.read_lexeme())
        self.lexemes.append(self.decoder.read_lexeme())
        self.lexemes.append(self.decoder.read_lexeme())

    def add_postfix(self, lexeme):
        if type(lexeme) is list:
            if lexeme[0] == 0:
                self.postfix_notation.append(self.identifiersMap[lexeme[1]])
            else:
                self.postfix_notation.append(str(lexeme[1]))
        elif type(lexeme) is int:
            self.postfix_notation.append(lexeme)
        else:
            self.postfix_notation.append(lexeme)

    def currentLexemeIs(self, lexemes: list[str] ) -> (bool, str):
        for lexeme in lexemes:
            if self.lexemes[self.cursor] == self.lexemesMap[lexeme]:
                self.cursor += 1
                self.lexemes.append(self.decoder.read_lexeme())
                return True, lexeme
        return False, ""

    def disassemble(self) -> tuple[list[str], bool]:
        if self.program():
            return self.postfix_notation, True
        else:
            return self.postfix_notation, False

    # <программа> -> <имя программы> переменные <раздел переменных> <раздел операторов> конец.
    def program(self):
        succeeded = False
        if self.name_program():
            correct, _ = self.currentLexemeIs(["переменные"])
            if correct:
                self.add_postfix("var")
                self.add_postfix("(")
                if self.variable_section():
                    self.add_postfix(")")
                    if self.operators_section():
                        correct, _ = self.currentLexemeIs(["конец."])
                        if correct:
                            succeeded = True
        return succeeded


    # <имя программы> -> программа ид ;
    def name_program(self):
        succeeded = False
        correct, _ = self.currentLexemeIs(["программа"])
        if correct:
            if type(self.lexemes[self.cursor]) is list and self.lexemes[self.cursor][0] == 0:
                current_ident = self.lexemes[self.cursor]
                self.cursor += 1
                self.lexemes.append(self.decoder.read_lexeme())
                correct, _ = self.currentLexemeIs([";"])
                if correct:
                    succeeded = True
                    # self.add_postfix(";")
                self.add_postfix(current_ident)
            self.add_postfix("программа")
        return succeeded

    # <раздел переменных> -> <объявление переменных> { ; <объявление переменных> } ;
    def variable_section(self):
        succeeded = False
        if self.declaration_variables():
            succeeded = True
            while True:
                if self.lexemes[self.cursor + 2] == self.lexemesMap[":"]:
                    correct, _ = self.currentLexemeIs([";"])
                    if not correct:
                        break
                if not self.declaration_variables():
                    succeeded = False
                    break
            correct, _ = self.currentLexemeIs([";"])
            if correct:
                succeeded = True

        return succeeded

    # <объявление переменных> -> <список переменных> : <тип>
    def declaration_variables(self) -> bool:
        succeeded = False
        if self.list_variables():
            correct, _ = self.currentLexemeIs([":"])
            if correct:
                if self.type():
                    succeeded = True
        return succeeded


    # <список переменных> -> ид {, ид}
    def list_variables(self):
        succeeded = False
        if self.is_ident():
            self.add_postfix(self.lexemes[self.cursor])
            self.cursor += 1
            self.lexemes.append(self.decoder.read_lexeme())
            succeeded = True
            while True:
                correct, _ = self.currentLexemeIs([","])
                if not correct:
                    break

                if not self.is_ident():
                    succeeded = False
                self.add_postfix(self.lexemes[self.cursor])
                self.cursor += 1
                self.lexemes.append(self.decoder.read_lexeme())
        return succeeded


    # <тип> -> целые / вещественные
    def type(self):
        succeeded = False
        correct, lexeme = self.currentLexemeIs(["целые", "вещественные"])
        if correct:
            succeeded = True
            self.add_postfix(lexeme)
        return succeeded


    # <раздел операторов> -> <оператор> {; <оператор>}
    def operators_section(self) -> bool:
        succeeded = False
        if self.operator():
            succeeded = True
            while True:
                correct, _ = self.currentLexemeIs([";"])
                if not correct:
                    break
                if not self.operator():
                    succeeded = False

        return succeeded

    # <оператор> -> <присваивание> / <условный оператор>
    def operator(self) -> bool:
        succeeded = False
        if self.assignment() or self.conditional_operator() or self.loop() or self.input_val() or self.output_val():
            succeeded = True
        return succeeded

    # <присваивание> -> ид := <арифмитическое выражение>
    def assignment(self) -> bool:
        succeeded = False
        if self.is_ident():
            ident = self.lexemes[self.cursor]
            self.cursor += 1
            self.lexemes.append(self.decoder.read_lexeme())
            self.add_postfix(ident)
            correct, _ = self.currentLexemeIs([":="])
            if correct:
                if self.arithmetic_expression():
                    succeeded = True
                self.add_postfix(":=")
        return succeeded

    # <цикл> -> пока <выражение цикла> выполнить <тело цикла>
    def loop(self) -> bool:
        succeeded = False
        correct, _ = self.currentLexemeIs(["пока"])
        if correct:
            self.add_postfix("пока")
            self.add_postfix("(")
            if self.conditional_expression():
                self.add_postfix(")")
                correct, _ = self.currentLexemeIs(["выполнить"])
                if correct:
                    if self.loop_body():
                        succeeded = True
        return succeeded

    def loop_body(self) -> bool:
        succeeded = False
        if self.operator():
            succeeded = True
        else:
            correct, _ = self.currentLexemeIs(["("])
            self.add_postfix("(")
            if correct:
                if self.operators_section():
                    correct, _ = self.currentLexemeIs([")"])
                    if correct:
                        succeeded = True
                        self.add_postfix(")")
        return succeeded


    # <условный оператор> -> if <условное выражение> THEN <тело условия>
    def conditional_operator(self) -> bool:
        succeeded = False
        correct, _ = self.currentLexemeIs(["if"])
        if correct:
            if self.conditional_expression():
                correct, _ = self.currentLexemeIs(["THEN"])
                if correct:
                    if self.condition_body():
                        succeeded = True
                    self.postfix_notation.append(self.lexemesMap["THEN"])
            self.postfix_notation.append(self.lexemesMap["if"])
        return succeeded

    # <условное выражение> -> <арифмитическое выражение> < / > / >= / <= / = / != <арифмитическое выражение>
    def conditional_expression(self) -> bool:
        succeeded = False
        if self.arithmetic_expression():
            correct, lexeme = self.currentLexemeIs(["<", ">", ">=", "<=", "=", "!="])
            if correct:
                if self.arithmetic_expression():
                    succeeded = True
                self.postfix_notation.append(lexeme)
        return succeeded

    # <тело условия> -> <оператор> / begin <раздел операторов> end
    def condition_body(self) -> bool:
        succeeded = False
        if self.operator():
            succeeded = True
        else:
            correct, _ = self.currentLexemeIs(["("])
            if correct:
                if self.operators_section():
                    correct, _ = self.currentLexemeIs([")"])
                    if correct:
                        succeeded = True
                        self.postfix_notation.append(self.lexemesMap["end"])
                self.postfix_notation.append(self.lexemesMap["begin"])
        return succeeded

    # <арифмитическое выражение> -> <слагаемое> {+ <слагаемое>} {- <слагаемое>}
    def arithmetic_expression(self) -> bool:
        succeeded = False
        if self.summand():
            succeeded = True
            while True:
                correct, lexeme = self.currentLexemeIs(["+", "-"])
                if not correct:
                    break

                if not self.summand():
                    succeeded = False
                self.add_postfix(lexeme)
        return succeeded

    # <слагаемое> -> <значение> {* <значение>} {DIV <значение>} {MOD <значение>} {DIY <значение>}
    def summand(self) -> bool:
        succeeded = False
        if self.value():
            succeeded = True
            while True:
                correct, lexeme = self.currentLexemeIs(["*", "/"])
                if not correct:
                    break

                if not self.value():
                    succeeded = False
                self.add_postfix(lexeme)
        return succeeded

    # <значение>: <значение> -> ид / конст / ( <арифметическое выражение> )
    def value(self) -> bool:
        succeeded = False
        if type(self.lexemes[self.cursor]) is list:
            self.add_postfix(self.lexemes[self.cursor])
            self.cursor += 1
            self.lexemes.append(self.decoder.read_lexeme())
            succeeded = True
        else:
            correct, _ = self.currentLexemeIs(["("])
            if correct:
                if self.arithmetic_expression():
                    correct, _ = self.currentLexemeIs([")"])
                    if correct:
                        succeeded = True
                        self.add_postfix(")")
                self.add_postfix("(")
        return succeeded

    def is_ident(self) -> bool:
        return type(self.lexemes[self.cursor]) is list and self.lexemes[self.cursor][0] == 0

    # <ввод> -> читать(ид)
    def input_val(self):
        succeeded = False
        correct, _ = self.currentLexemeIs(["читать"])
        if correct:
            correct, _ = self.currentLexemeIs(["("])
            if correct:
                if self.is_ident():
                    ident = self.lexemes[self.cursor]
                    self.cursor += 1
                    correct, _ = self.currentLexemeIs([")"])
                    if correct:
                        succeeded = True
                    self.add_postfix(ident)
            self.add_postfix("читать")

        return succeeded

    # <вывод> -> печатать ( ид )
    def output_val(self):
        succeeded = False
        correct, _ = self.currentLexemeIs(["печатать"])
        if correct:
            correct, _ = self.currentLexemeIs(["("])
            if correct:
                if self.is_ident():
                    ident = self.lexemes[self.cursor]
                    self.cursor += 1
                    correct, _ = self.currentLexemeIs([")"])
                    if correct:
                        succeeded = True
                    self.add_postfix(ident)
            self.add_postfix("печатать")

        return succeeded