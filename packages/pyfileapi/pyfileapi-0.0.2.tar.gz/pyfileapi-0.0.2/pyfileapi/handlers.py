from __future__ import annotations

import os
from typing import Any
from typing import TextIO


def read_file(file: str | bytes | os.PathLike[Any]) -> TextIO:
    f = open(file=file)
    return f
