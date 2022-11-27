"""シグナルエンティティ（enum）"""
from enum import IntEnum, auto

class Sygnal(IntEnum):
    BUY = auto()
    SELL = auto()
    SETTLE = auto()