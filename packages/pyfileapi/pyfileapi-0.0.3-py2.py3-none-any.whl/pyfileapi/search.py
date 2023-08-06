from __future__ import annotations

import os
import re
from typing import Any

from pyfileapi.search_helpers import get_match_tuple
from pyfileapi.search_helpers import MatchTuple

FilePath = str | bytes | os.PathLike[Any]


def find_match(
    file: FilePath, search_string: str, all_matches: bool = False,
) -> list[MatchTuple] | MatchTuple:
    if not search_string:
        raise Exception('find_match() requires search_string to be non empty')
    with open(file=file) as f:
        text = f.read()
        matches = [
            get_match_tuple(text, m)
            for m in re.finditer(search_string, text)
        ]
        if not all_matches and matches != []:
            return matches[0]
        return matches
