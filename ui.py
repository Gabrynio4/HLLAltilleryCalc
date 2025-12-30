import tkinter as tk
from tkinter import ttk
from axisAlliesCalcStrategy import AxiesAlliesCalcStrategy
from britsCalcStrategy import BritsCalcStrategy
from ussrCalcStrategy import UssrCalcStrategy
from calcContext import CalcContext

# Główne okno
root = tk.Tk()
root.title("Hell Let Loose Altillery Calculator")
root.geometry("400x300+100+50")


# Etykieta
label = tk.Label(root, text="Enter the distance:")
label.pack(pady=(10, 0))
# Dystans input
entry = tk.Entry(root, font=("Arial", 10, "normal"), bd=1, relief="solid")
entry.pack(pady=5)
entry.insert(0, "1300")


# Etykieta
label = tk.Label(root, text="Choose your nation:")
label.pack(pady=(20, 0))
# Combobox
opcje = ["Axis/Allies", "British", "Ussr"]
combo = ttk.Combobox(root, values=opcje, state="readonly")
combo.current(0)  # ustawiamy domyślny wybór
combo.pack(pady=5)


# Odpowiedź
label = tk.Label(root, text="", font=("Arial", 15, "normal"))
label.pack(pady=(20, 20))


# Logika
def calculate():
    chosen = combo.get()
    distance = int(entry.get())

    if chosen == "British":
        strategy = BritsCalcStrategy()
    elif chosen == "Ussr":
        strategy = UssrCalcStrategy()
    else:
        strategy = AxiesAlliesCalcStrategy()

    context = CalcContext(strategy)
    result = context.calculate(distance=distance)

    label.config(text=result)


# Przycisk
button = tk.Button(root, text="Calculate", command=calculate)
button.pack(pady=10)

root.mainloop()
