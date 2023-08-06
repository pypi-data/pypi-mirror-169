import enum
import os
import string

from .preprocess import Preprocessor
from .error import lex_error
from .util import Position, sanitize


class TokenType(enum.Enum):
    """
    token types
    """

    NONE = enum.auto()
    ID = enum.auto()
    STRING = enum.auto()
    NUMBER = enum.auto()
    LPAREN = enum.auto()
    RPAREN = enum.auto()
    LBRACE = enum.auto()
    RBRACE = enum.auto()
    LBRACK = enum.auto()
    RBRACK = enum.auto()
    COMMA = enum.auto()
    SEMICOLON = enum.auto()
    COLON = enum.auto()
    OPERATOR = enum.auto()
    SET = enum.auto()
    LOGIC = enum.auto()


class Token:
    """
    token of code
    """

    type: TokenType
    value: str
    pos: Position

    def __init__(self, type_: TokenType, value: str, pos: Position):
        self.type = type_
        self.value = value
        self.pos = pos

    def __repr__(self) -> str:
        return f"[{self.type}, \"{sanitize(self.value)}\"]"

    def pos(self) -> Position:
        return self.pos


class Lexer:
    ID_CHARS_START = string.ascii_letters + "_@"
    ID_CHARS = ID_CHARS_START + "-." + string.digits

    STRING_CHARS = string.printable

    NUMBER_CHARS_START = string.digits
    NUMBER_CHARS = NUMBER_CHARS_START + "."

    OPERATOR_CHARS_START = "+-*/%=<>!&|^~"

    SET_CHARS_START = "=+-*/%&|^<>"

    LOGIC_CHARS_START = "&|"

    include_search_dir: str
    imported_files: set

    current_input_file: str
    current_code: str
    i: int
    line: int
    char: int

    def __init__(self, include_search_dir: str):
        self.include_search_dir = include_search_dir
        self.imported_files = set()

        self.current_input_file = ""
        self.current_code = ""
        self.i = -1
        self.line = 0
        self.char = 0

    def next_char(self, char: str | None = None) -> str:
        self.i += 1
        if self.i >= len(self.current_code):
            return ""
        ch = self.current_code[self.i]
        if char is not None and ch != char:
            lex_error(f"Unexpected character [{ch}]", Position(self.line, self.char, self.char + 1,
                                                               self.current_code.splitlines()[self.line], self.current_input_file))
        self.char += 1
        if ch == "\n":
            self.char = 0
            self.line += 1
        return ch

    def lookahead_char(self, char: str | None = None) -> str | bool:
        if self.i + 1 >= len(self.current_code):
            return ""
        if self.current_code[self.i + 1] == char:
            self.i += 1
            return True
        elif char is not None:
            return False
        return self.current_code[self.i + 1]

    def prev_char(self):
        if self.i > -1:
            self.i -= 1

    def make_position(self, length: int) -> Position:
        return Position(self.line, self.char, self.char + length, self.current_code.splitlines()[self.line], self.current_input_file)

    def make_token(self, type_: TokenType, value: str) -> Token:
        return Token(type_, value, self.make_position(len(value)))

    def lex(self, code: str, input_file: str) -> list[Token]:
        old_current_code = self.current_code
        self.current_code = code
        old_current_input_file = self.current_input_file
        self.current_input_file = input_file
        old_i = self.i
        self.i = -1
        old_line = self.line
        self.line = 0
        old_char = self.char
        self.char = 0

        tokens = []
        while ch := self.lookahead_char():
            if ch == "":
                break

            if not ch.strip():
                self.next_char()
                continue

            if ch == "#":
                self.lex_until_eol()
                continue

            if ch == "%" and self.char == 0:
                token = self.lex_until_eol()
                if len(token) > 1:
                    path = os.path.join(self.include_search_dir, token[1:])
                    if os.path.isfile(path):
                        if path in self.imported_files:
                            lex_error(f"File [\"{path}\"] is already imported", self.make_position(len(token)))
                        self.imported_files.add(path)

                        with open(path, "r") as f:
                            imported_code = f.read()

                        imported_code = Preprocessor.preprocess(imported_code)
                        tokens += self.lex(imported_code, path)

                    else:
                        lex_error(f"Cannot find file [\"\"]", self.make_position(len(token)))

            elif ch in self.ID_CHARS_START and (token := self.lex_id()) is not None:
                tokens.append(self.make_token(TokenType.ID, token))

            elif ch == '"' and (token := self.lex_string()) is not None:
                tokens.append(self.make_token(TokenType.STRING, token))

            elif ch in self.NUMBER_CHARS_START and (token := self.lex_number()) is not None:
                tokens.append(self.make_token(TokenType.NUMBER, token))

            elif ch == "(":
                self.next_char()
                tokens.append(self.make_token(TokenType.LPAREN, ch))
            elif ch == ")":
                self.next_char()
                tokens.append(self.make_token(TokenType.RPAREN, ch))

            elif ch == "{":
                self.next_char()
                tokens.append(self.make_token(TokenType.LBRACE, ch))
            elif ch == "}":
                self.next_char()
                tokens.append(self.make_token(TokenType.RBRACE, ch))

            elif ch == "[":
                self.next_char()
                tokens.append(self.make_token(TokenType.LBRACK, ch))
            elif ch == "]":
                self.next_char()
                tokens.append(self.make_token(TokenType.RBRACK, ch))

            elif ch == ",":
                self.next_char()
                tokens.append(self.make_token(TokenType.COMMA, ch))
            elif ch == ";":
                self.next_char()
                tokens.append(self.make_token(TokenType.SEMICOLON, ch))
            elif ch == ":":
                self.next_char()
                tokens.append(self.make_token(TokenType.COLON, ch))

            elif ch in self.LOGIC_CHARS_START and (token := self.lex_logic()) is not None:
                tokens.append(self.make_token(TokenType.LOGIC, token))

            elif ch in Lexer.SET_CHARS_START and (token := self.lex_set()) is not None:
                tokens.append(self.make_token(TokenType.SET, token))

            elif ch in Lexer.OPERATOR_CHARS_START and (token := self.lex_operator()) is not None:
                tokens.append(self.make_token(TokenType.OPERATOR, token))

        self.current_code = old_current_code
        self.current_input_file = old_current_input_file
        self.i = old_i
        self.line = old_line
        self.char = old_char

        return tokens

    def lex_until_eol(self) -> str:
        token = ""
        while (ch := self.next_char()) != "\n":
            token += ch
        return token

    def lex_id(self) -> str:
        token = ""
        while (ch := self.lookahead_char()) in Lexer.ID_CHARS:
            self.next_char()
            token += ch
        return token

    def lex_string(self) -> str:
        self.next_char()
        token = ""
        while (ch := self.next_char()) in Lexer.STRING_CHARS:
            if ch == '"':
                return f"\"{token}\""
            token += ch
        return f"\"{token}\""

    def lex_number(self) -> str:
        token = ""
        while (ch := self.lookahead_char()) in Lexer.NUMBER_CHARS:
            self.next_char()
            token += ch
        return token

    def lex_operator(self) -> str | None:
        match ch := self.next_char():
            case "+" | "-" | "~" | "&" | "|" | "^" | "%":
                return ch
            case "*":
                if self.lookahead_char("*"):
                    return "**"
                return "*"
            case "/":
                if self.lookahead_char("/"):
                    return "//"
                return "/"
            case "=":
                if self.lookahead_char("="):
                    if self.lookahead_char("="):
                        return "==="
                    return "=="
            case "<" | ">":
                if self.lookahead_char("="):
                    return ch + "="
                elif self.lookahead_char(ch):
                    return ch + ch
                return ch
            case "!":
                if self.lookahead_char("="):
                    return "!="
                return "!"

        self.prev_char()

    def lex_set(self) -> str | None:
        match ch := self.next_char():
            case "=":
                if self.lookahead_char() == "=":
                    self.prev_char()
                    return None
                return ch
            case "+" | "-" | "%" | "&" | "|" | "^":
                if self.lookahead_char("="):
                    return ch + "="
            case "*" | "/":
                if self.lookahead_char() == ch:
                    self.next_char()
                    if self.lookahead_char("="):
                        return ch + ch + "="
                    self.prev_char()
                elif self.lookahead_char("="):
                    return ch + "="
            case "<" | ">":
                if self.lookahead_char(ch):
                    if self.lookahead_char("="):
                        return ch + ch + "="
                    self.prev_char()

        self.prev_char()

    def lex_logic(self) -> str | None:
        ch = self.next_char()
        if self.lookahead_char(ch):
            return ch + ch

        self.prev_char()
