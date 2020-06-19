from enum import Enum


class State(Enum):
    # -------- State for Number ---------
    InitialNumber = 1
    FinalNumber = 2
    NoNextState = -1

    # -------- State for Identifier ---------
    InitialID = 1
    FinalID = 2
    # NoNextState = -1

