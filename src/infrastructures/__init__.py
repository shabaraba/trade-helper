"""module横断モジュール"""
from .dependencyBuilder import ModuleFactory


Dependency = ModuleFactory()

__all__ = ['Dependency']