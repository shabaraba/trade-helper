"""DIモジュール"""
import injector
from typing import Type, Any, Callable


class ModuleFactory:
    """DIモジュール"""
    def __init__(self):
        # 依存性注入の初期化はconfigureに移譲
        self._injector = injector.Injector(self.__class__.configure)
    

    def __getitem__(self, klass) -> Callable:
        # 与えられたインタフェースに応じて実体クラスを返す
        return lambda: self._injector.get(klass)


    @classmethod
    def configure(cls, binder: injector.Binder) -> None:
        pass
    

    def add(self, interface_, implement_):
        self._injector.binder.bind(interface_, to=implement_) # type: ignore[type-abstract]
