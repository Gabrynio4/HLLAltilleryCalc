from calcStrategy import CalcStrategy

class AxiesAlliesCalcStrategy(CalcStrategy):
    def calculate(self, distance: int) -> int:
        if 100 <= distance <= 1600:
            return round(1001.75 - (0.2375 * distance))
        return 0