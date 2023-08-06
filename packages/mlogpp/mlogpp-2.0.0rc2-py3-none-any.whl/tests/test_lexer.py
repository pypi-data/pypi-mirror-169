import unittest

from mlogpp.lexer import *


class LexerTestCase(unittest.TestCase):
    SOURCE_CODE = """\
# testing source code

x = 23
a = x + 1
x += 80

cell1[10] = 2
cell1[10] += cell1[4]

function func(a, b) {
    global a, x
    return a + x
}

ucontrol.move(x, x + 1)

string = "Hello, World!"
unit = @zenith

print(string)
print(unit)

if (unit == @surge-alloy) {
    s = true
} else {
    s = false
}

while (true) {
    a += 1
    if (a > x) {
        break
    }
}

for (i = 1; i <= 10; i += 1) {
    print(i)
    if (i == 5) {
        continue
    }
}

ubind(@mega)
"""

    def test_lex(self):
        tokens = Lexer.lex(LexerTestCase.SOURCE_CODE)

    def test_match(self):
        self.assertEqual(Lexer.match("@surge-alloy.property"), TokenType.ID)
        self.assertEqual(Lexer.match("\"Hello, World!\""), TokenType.STRING)
        self.assertEqual(Lexer.match("437689"), TokenType.NUMBER)
        self.assertEqual(Lexer.match("12.569"), TokenType.NUMBER)
        self.assertEqual(Lexer.match("("), TokenType.LPAREN)
        self.assertEqual(Lexer.match(")"), TokenType.RPAREN)
        self.assertEqual(Lexer.match("{"), TokenType.LBRACE)
        self.assertEqual(Lexer.match("}"), TokenType.RBRACE)
        self.assertEqual(Lexer.match("["), TokenType.LBRACK)
        self.assertEqual(Lexer.match("]"), TokenType.RBRACK)
        self.assertEqual(Lexer.match(","), TokenType.COMMA)
        self.assertEqual(Lexer.match(";"), TokenType.SEMICOLON)

        operator_tokens = ("+", "-", "*", "/", "!", "**", "===", "<=", ">=", "==", "!=", "<", ">", "~")
        self.assertEqual(
            tuple(map(Lexer.match, operator_tokens)),
            (TokenType.OPERATOR,) * len(operator_tokens)
        )

        set_tokens = ("=", "+=", "-=", "*=", "+=")
        self.assertEqual(
            tuple(map(Lexer.match, set_tokens)),
            (TokenType.SET,) * len(set_tokens)
        )

        self.assertEqual(Lexer.match("&&"), TokenType.LOGIC)
        self.assertEqual(Lexer.match("||"), TokenType.LOGIC)

        none_tokens = (
            "\"Hello, World!",
            "#500",
            "12value"
        )
        self.assertEqual(
            tuple(map(Lexer.match, none_tokens)),
            (TokenType.NONE,) * len(none_tokens)
        )


if __name__ == '__main__':
    unittest.main()
