"""init"""
from infrastructures import Dependency
from .services.technical_analyze_service import TechnicalAnalyzeService
from .services.mock_technical_analyze_service_impl import MockTechnicalAnalyzeServiceImpl


Dependency.add(TechnicalAnalyzeService, MockTechnicalAnalyzeServiceImpl)

__all__ = [
    "TechnicalAnalyzeService",
]
