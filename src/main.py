"""メインモジュール"""
from infrastructures import Dependency
from usecases.program_trade_usecase import ProgramTradeUsecase

if __name__ == "__main__":
    programTradeUsecase = Dependency.resolve(ProgramTradeUsecase)