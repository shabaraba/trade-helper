"""init"""
from infrastructures import Dependency
from .services.exchange_service import ExchangeService
from .services.exchange_service_impl import ExchangeServiceImpl


Dependency.add(ExchangeService, ExchangeServiceImpl)

__all__ = [
    "ExchangeService",
]