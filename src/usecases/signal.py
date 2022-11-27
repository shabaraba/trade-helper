"""シグナルエンティティ（enum）"""
from enum import IntEnum, auto

class Signal(IntEnum):
    BUY = auto()
    SELL = auto()
    SETTLE = auto()
