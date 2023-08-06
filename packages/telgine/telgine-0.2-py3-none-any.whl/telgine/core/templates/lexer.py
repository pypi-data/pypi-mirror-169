from sly import Lexer


class telgineLexer(Lexer):
    tokens = {ID, GT, LT, CLOSE, ASSIGN, TEXT, STRING, COLON, IF, ELSE, FOR}

    @_(r'(?<=>\n)([^<|>|])+(?=<)|(?<=>)([^<|>|])+(?=<)')
    def TEXT(self, t):
        t.value = t.value.strip()

        if len(t.value) > 0:
            return t

    CLOSE = r'</'
    GT = r'>'
    LT = r'<'
    ASSIGN = r'='

    STRING = r'"([^"]+)?"'

    ID = r'[A-z]([A-z]|\d||\-)+[A-z\d]'
    ID['v-if'] = IF
    ID['v-else'] = ELSE
    ID['v-for'] = FOR

    @_(r'"(([^"])+)"')
    def STRING(self, t):
        t.value = t.value[1:-1]
        return t
    COLON = r':'

    ignore = r'\f\r\t\n '
    ignore_newline = r'\n+'


def tokenize(string):
    lexer = telgineLexer()
    return lexer.tokenize(string)
