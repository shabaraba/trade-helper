"""DIモジュール"""
import injector
from typing import Type, Any, Callable


class ModuleFactory:
    """DIモジュール"""
    def __init__(self):
        # 依存性注入の初期化はconfigureに移譲
        self._injector = injector.Injector(self.__class__.configure)
    

    def __getitem__(self, klass: Type[Any]) -> Callable:
        # 与えられたインタフェースに応じて実体クラスを返す
        return lambda: self._injector.get(klass)


    @classmethod
    def configure(cls, binder: injector.Binder) -> None:
        pass
    

    def add(self, interface: Type[Any], implement: Type[Any]):
        self._injector.binder.bind(interface, to=implement) # type: ignore[type-abstract]
