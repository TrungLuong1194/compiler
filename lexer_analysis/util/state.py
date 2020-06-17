from enum import Enum


class State(Enum):
    # -------- State for Number ---------
    Initial = 1
    Integer = 2
    BeginNumberWithFractionPart = 3
    NumberWithFractionPart = 4
    NoNextState = -1

    # -------- State for String ---------
    # Initial = 1
    OpenString = 2
    String = 3
    # NoNextState = -1

