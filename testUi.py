from axisAlliesCalcStrategy import AxiesAlliesCalcStrategy
from britsCalcStrategy import BritsCalcStrategy
from ussrCalcStrategy import UssrCalcStrategy
from calcContext import CalcContext

print("Select nation:")
print("a - axis/allies")
print("b - brits")
print("u - soviets")
nation = input()
distance = int(input("\nSelect Distance: "))

if nation == "a":
    strategy = AxiesAlliesCalcStrategy()
elif nation == "b":
    strategy = BritsCalcStrategy()
elif nation == "u":
    strategy = UssrCalcStrategy()
else:
    raise ValueError("Invalid input. 'a', 'b' or 'u' expected")
    
context = CalcContext(strategy)
result = context.calculate(distance=distance)
if result == 0:
    print("Out of range")
else:
    print(f"\nCalculated elevation: {result} MIL")