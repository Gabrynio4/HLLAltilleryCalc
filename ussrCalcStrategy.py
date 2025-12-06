from calcStrategy import CalcStrategy

class UssrCalcStrategy(CalcStrategy):
    def calculate(self, distance: int) -> int:
        if 100 <= distance <= 1600:
            return round(1127.0 - (0.2 * distance))
        return 0