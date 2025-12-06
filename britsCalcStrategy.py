from calcStrategy import CalcStrategy

class BritsCalcStrategy(CalcStrategy):
    def calculate(self, distance: int) -> int:
        if 100 <= distance <= 1600:
            return round(551.4 - (0.18 * distance))
        return 0