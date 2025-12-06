# Artillery Distance Calculator for Hell Let Loose

This is a **command-line artillery distance calculator** for the game *Hell Let Loose*. It allows players to convert target distances from meters to MILs, helping with artillery aiming for different nations in the game.

## Features

- Command-line interface (CLI) in `testUi.py`.
- Calculates MIL values for 4 nations:
  - Axis
  - Allies
  - British
  - USSR
- Axis and Allies share the same calculation system.
- Prompts the user to select a nation and enter the target distance in meters.
- Outputs the calculated distance in MILs.

## Installation

1. Make sure you have Python 3 installed.
2. Clone or download this repository.
3. Run the program:

```bash
python testUi.py
```
## Usage

1. Start the program.
2. Select your nation from the list.
3. Enter the distance to the target.
4. The program will calculate and display the distance in MILs.

## Example
```
Select nation:
a - axis/allies
b - brits
u - soviets
>a
Select Distance: >500
Calculated elevation: 883 MIL
```
