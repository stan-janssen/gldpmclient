from enum import Enum


class CurveType(Enum):
    SEQUENTIAL_FIXED_SIZE_BLOCK = "A01"
    POINT                       = "A02"
    VARIABLE_SIZED_BLOCK        = "A03"
    OVERLAPPING_BREAKPOINT      = "A04"
    NON_OVERLAPPING_BREAKPOINT  = "A05"
