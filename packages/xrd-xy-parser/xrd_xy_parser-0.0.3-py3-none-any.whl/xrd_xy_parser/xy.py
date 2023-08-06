from enum import Enum
from io import TextIOWrapper
import pathlib
import re
import numpy as np


number_patt = r"[0-9]+(?:\.[0-9]+)?"
"""
match integer or numbers like 12.33,0.1
"""
delimiter_patt = r"(?:\s|\t)"

number_re = re.compile(number_patt)
xy_pair_re = re.compile(number_patt + delimiter_patt + number_patt)


class xy_parser:
    class state(Enum):
        HEAD = "head"
        BODY = "body"
        FOOT = "foot"

    def __init__(self) -> None:

        self.current: xy_parser.state = self.state.HEAD
        self.head_: str = ""
        self.body_: np.ndarray = np.ndarray((0, 2))
        self.foot_: str = ""

    def head(self, line: str):
        if not xy_pair_re.fullmatch(line):
            self.head_ += line + "\n"
        else:
            self.body(line)
            self.current = self.state.BODY

    def body(self, line: str):
        tmp = number_re.findall(line)
        if len(tmp) == 2:
            self.body_ = np.vstack((self.body_, [float(tmp[0]), float(tmp[1])]))

        else:
            self.foot(line)
            self.current = self.state.FOOT

    def foot(self, line: str):
        self.foot_ += line

    def transit(self, line: str) -> None:
        line = line.strip()
        if line == "":
            return

        if self.current is self.state.HEAD:
            self.head(line)
        elif self.current is self.state.BODY:
            self.body(line)
        elif self.current is self.state.FOOT:
            self.foot(line)

    def error(self, file: TextIOWrapper) -> None:
        """if cannot parse file,raise Error"""

        if self.current is not self.state.HEAD and self.foot_ == "":
            return None

        raise ParseError(file, self.head_, self.foot_)


class ParseError(Exception):
    """cannot parse xy file."""

    def __init__(self, file: TextIOWrapper, head: str, foot: str) -> None:
        # super.__init__(filename, foot)
        self.file = file
        self.head = head
        self.foot = foot

    def __str__(self) -> str:
        return """Cannot parse ,wrong with something in '{}',
        header is {},
        footer is '{}'
        """.format(
            self.file.name, self.head, self.foot
        )


def read(path: pathlib.Path) -> tuple[str, np.ndarray, str]:
    """
    Parses the xy file specified by path and returns a tuple consisting of error, header, body, and footer.
    パスで指定されたxyファイルをパースし、エラー、ヘッダ、ボディ、フットからなるタプルを返す.

    Parametors
    ---
        `path`:pathlib.Path
            path to xy file

    Returns
    ---
        `header`:str
            path's file header

        `body`:numpy.ndarray
            path's file data

        `footer`:str
            path's file header

    Raises:
        ParseError:
            raise on fail parsing
    """

    parser: xy_parser = xy_parser()
    with path.open() as xyfile:

        for line in xyfile:
            parser.transit(line)

    parser.error(xyfile)
    return parser.head_, parser.body_, parser.foot_


def readstr(path: str) -> tuple[str, np.ndarray, str]:
    return read(pathlib.Path(path))
