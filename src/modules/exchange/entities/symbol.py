"""銘柄エンティティ"""
import dataclasses

@dataclasses.dataclass(frozen=True)
class Symbol():
    """銘柄エンティティ"""

    ticker: str
    price: float