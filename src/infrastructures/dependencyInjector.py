"""DIモジュール"""
import injector
from typing import Type, Any, Callable


class DependencyInjector:
    """DIモジュール"""
    def __init__(self):
        # 依存性注入の初期化はconfigureに移譲
        self._injector = injector.Injector(self.__class__.configure)
    

    @classmethod
    def configure(cls, binder: injector.Binder) -> None:
        pass
    

    def resolve(self, klass) -> Callable:
        # 与えられたインタフェースに応じて実体クラスを返す
        return self._injector.get(klass)
        # return lambda: self._injector.get(klass)


    def add(self, interface_, implement_):
        self._injector.binder.bind(interface_, to=implement_) # type: ignore[type-abstract]
