from enum import Enum
from math import floor


class PositionReference(Enum):
    TOP_LEFT = 1
    CENTER = 2
    BOTTOM_RIGHT = 3


class PositionUnit(Enum):
    PIXELS = 1
    PERCENTAGE = 2


# used to place buttons and other elements on the screen
class Position:
    def __init__(self, window, x: float, y: float, unit: PositionUnit=PositionUnit.PIXELS, reference: PositionReference=PositionReference.TOP_LEFT):
        self.window = window
        self._x = floor(x if unit == PositionUnit.PIXELS else x * window.size[0] / 100)
        self._y = floor(y if unit == PositionUnit.PIXELS else y * window.size[1] / 100)
        self.unit = unit
        self.reference = reference

    def get(self, elementSize: tuple=(0, 0), reference: PositionReference=PositionReference.TOP_LEFT):
        match reference:
            case PositionReference.TOP_LEFT:
                match self.reference:
                    case PositionReference.TOP_LEFT:
                        return (self._x, self._y)
                    case PositionReference.CENTER:
                        return (self._x - elementSize[0] // 2, self._y - elementSize[1] // 2)
                    case PositionReference.BOTTOM_RIGHT:
                        return (self._x - elementSize[0], self._y - elementSize[1])
                    case _:
                        raise ValueError("Invalid position type")
            case PositionReference.CENTER:
                match self.reference:
                    case PositionReference.TOP_LEFT:
                        return (self._x - elementSize[0] // 2, self._y - elementSize[1] // 2)
                    case PositionReference.CENTER:
                        return (self._x, self._y)
                    case PositionReference.BOTTOM_RIGHT:
                        return (self._x - elementSize[0] // 2, self._y - elementSize[1] // 2)
                    case _:
                        raise ValueError("Invalid position type")
            case PositionReference.BOTTOM_RIGHT:
                match self.reference:
                    case PositionReference.TOP_LEFT:
                        return (self._x - elementSize[0], self._y - elementSize[1])
                    case PositionReference.CENTER:
                        return (self._x - elementSize[0] // 2, self._y - elementSize[1] // 2)
                    case PositionReference.BOTTOM_RIGHT:
                        return (self._x, self._y)
                    case _:
                        raise ValueError("Invalid position type")
            case _:
                raise ValueError("Invalid position type")