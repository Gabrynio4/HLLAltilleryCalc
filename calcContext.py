from calcStrategy import CalcStrategy


class CalcContext:
    def __init__(self, strategy: CalcStrategy):
        self._calc_strategy = strategy

    def calculate(self, distance: int) -> int:
        return self._calc_strategy.calculate(distance)
