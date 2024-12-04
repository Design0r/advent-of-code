from dataclasses import dataclass
from enum import StrEnum, auto
from pathlib import Path
from typing import Any, Optional

with open(Path(__file__).parent.parent / "samples/day_03.txt") as f:
    file = f.read().strip()


def peek(input: str, start: int, stop: int) -> Optional[str]:
    if stop >= len(input):
        stop -= abs(stop - len(input))
    return "".join(input[start:stop])


class TokenType(StrEnum):
    MUL = "mul"
    PARENS_OPEN = "("
    PARENS_CLOSE = ")"
    COMMA = ","
    DO = "do()"
    DONT = "don't()"
    NUM = auto()
    INVALID = auto()

    def __repr__(self) -> str:
        return self.name


@dataclass(match_args=True)
class Token:
    type: TokenType
    value: Any


def lex(data: str) -> list[Token]:
    tokens: list[Token] = []
    cursor = 0
    while True:
        window = peek(data, cursor, cursor + 7)
        if not window:
            break

        if window[:3] == "mul":
            tokens.append(Token(TokenType.MUL, "mul"))
            cursor += 3
        elif window[:1] == "(":
            tokens.append(Token(TokenType.PARENS_OPEN, "("))
            cursor += 1
        elif window[:1] == ")":
            tokens.append(Token(TokenType.PARENS_CLOSE, ")"))
            cursor += 1
        elif window[:1] == ",":
            tokens.append(Token(TokenType.COMMA, ","))
            cursor += 1
        elif window[0].isdigit():
            num: list[str] = []
            for idx, i in enumerate(window):
                if idx > 2:
                    break
                if not i.isdigit():
                    break
                num.append(i)
            tokens.append(Token(TokenType.NUM, int("".join(num))))
            cursor += len(num)
        elif window == "don't()":
            tokens.append(Token(TokenType.DONT, window))
            cursor += 7
        elif window[:4] == "do()":
            tokens.append(Token(TokenType.DO, window[:3]))
            cursor += 4
        else:
            tokens.append(Token(TokenType.INVALID, window[0]))
            cursor += 1

    return tokens


def validate_mul(tokens: list[Token]) -> int:
    valid_seq = [
        TokenType.MUL,
        TokenType.PARENS_OPEN,
        TokenType.NUM,
        TokenType.COMMA,
        TokenType.NUM,
        TokenType.PARENS_CLOSE,
    ]

    if len(tokens) != len(valid_seq):
        return 0

    for token, type in zip(tokens, valid_seq):
        if token.type != type:
            return 0

    return tokens[2].value * tokens[4].value


def parse(tokens: list[Token], extended: bool = False) -> int:
    result = 0
    enabled = True
    cursor = 0
    while True:
        if cursor >= len(tokens):
            break
        curr_token = tokens[cursor]
        match curr_token:
            case Token(type=TokenType.DONT):
                if extended:
                    enabled = False
                cursor += 1
            case Token(type=TokenType.DO):
                if extended:
                    enabled = True
                cursor += 1
            case Token(type=TokenType.MUL):
                window = tokens[cursor : cursor + 6]
                if enabled:
                    result += validate_mul(window)
                cursor += 6
            case _:
                cursor += 1

    return result


def part_1() -> None:
    tokens = lex(file)
    result = parse(tokens)
    print(f"Day 3, Part 1: {result}")


def part_2() -> None:
    tokens = lex(file)
    result = parse(tokens, extended=True)
    print(f"Day 3, Part 2: {result}")


if __name__ == "__main__":
    part_1()
    part_2()
