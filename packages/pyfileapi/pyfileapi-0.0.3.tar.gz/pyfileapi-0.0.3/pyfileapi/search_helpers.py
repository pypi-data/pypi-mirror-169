from __future__ import annotations

from typing import AnyStr
from typing import Match
from typing import Tuple

MatchTuple = Tuple[str, int, Tuple[int, int]]


def get_match_tuple(text: str, m: Match[AnyStr]) -> MatchTuple:
    text_match = text[m.start():m.end()]
    span: tuple[int, int] = m.span()
    line_no: int = 0
    lines = text.split('\n')
    for line_num, line in enumerate(lines):
        if line.find(text_match) != -1:
            line_no = line_num + 1
    return text_match, line_no, span
