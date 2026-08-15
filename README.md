# Introduction
This is a python script for determining the stability of a Quantum Computer. Every rack has four total slots for either circuits (to generate heat and computation packets) or vents (to dissipate heat). When turned on, the heat starts to increase but stabilizes at some value 0-10,000. It is important to keep the heat below the maximum heat limit for every component in the rack to prevent them from voiding. Where exactly the heat stabilizes is neither obvious nor easily calculated which is where this script can help. Note that every rack is independent of every other rack meaning you CANNOT have all circuits in one and all vents in another even if they are both part of the same Quantum Computer.

# Usage
  - Download the appropriate `QuantumComputer.py` script depending on your version of GTNH. If you do not have a way to easily run python scripts, you can copy the code into an online IDE (https://www.online-python.com/).
  - Enter the names of the components that you would like to test under the "EDIT HERE" section at the bottom of the code. The names must be exactly as portrayed in the dictionary at the top (ie. APU T3).
  - Enter the Overclock and Overvolt values as well as how many racks are on your Quantum Computer. The voltage setting has no effect other than determining amps.
  - Optionally, set optimize=True to ignore the custom Overclock and Overvolt values and spend a little extra time finding the combination with the highest computation per second.
  - Run the script. It outputs the Overclock/Overvolt values, the final heat approximation (where it stabilizes), and whether or not any of the components void. If it is safe, it also tells you the total computation and total power consumption assuming all racks are identical.

![Edit Here](media/edithere.png?)

![Output](media/output.png?)

# Stable Setups (2.7.0+)
Here are several combinations of circuits and vents for maximizing computation depending on your available resources and progression. The computation and power is per 24 racks or a max length QC. Do not be alarmed if the heat increases rapidly at first--these are designed to converge just below the heat limit of the components. For other circuits, use the actual script.

Comp 1 | Comp 2 | Comp 3 | Comp 4 | Overclock | Overvolt | Amps (UV) | Computation
--- | --- | --- | --- | --- | --- | --- | ---
Crystal Mainframe | Cooling Core | Cooling Core | Cooling Core | 1.73 | 1.41 | 15.25 | 10,416 /s
Crystal Mainframe | Crystal Mainframe | Cooling Core | Cooling Core | 1.21 | 1.00 | 7.56 | 13,584 /s
APU T3 | Cooling Core | Cooling Core | Cooling Core | 1.86 | 1.52 | 17.67 | 23,016 /s
APU T3 | APU Creative | Cooling Core | Cooling Core | 1.43 | 1.03 | 9.21 | 30,216 /s
Wetware Mainframe | Cooling Core | Cooling Core | Cooling Core | 2.15 | 1.87 | 25.13 | 27,528 /s
Wetware Mainframe | Wetware Mainframe | Cooling Core | Cooling Core | 1.63 | 1.26 | 12.84 | 33,960 /s
Bioware Mainframe | Cooling Core | Cooling Core | Cooling Core | 2.63 | 2.35 | 38.63 | 45,792 /s
Bioware Mainframe | Bio Mainframe | Cooling Core | Cooling Core | 1.91 | 1.61 | 19.22 | 53,208 /s
Optical Mainframe | Cooling Core | Cooling Core | Cooling Core | 3.20 | 3.00 | 60.00 | 67,416 /s
Optical Mainframe | Optical Mainframe | Cooling Core | Cooling Core | 2.35 | 2.04 | 29.96 | 74,256 /s
Pico Circuit | Cooling Core | Cooling Core | Cooling Core | 3.95 | 3.80 | 93.81 | 101,304 /s
Pico Circuit | Pico Circuit | Cooling Core | Cooling Core | 2.86 | 2.60 | 46.47 | 107,304 /s
Quantum Circuit | Cooling Core | Cooling Core | Cooling Core | 4.26 | 4.12 | 109.69 | 144,216 /s
Quantum Circuit | Quantum Circuit | Cooling Core | Cooling Core | 3.05 | 2.83 | 53.95 | 150,936 /s
Planck Circuit | Cooling Core | Cooling Core | Cooling Core | 4.59 | 4.44 | 127.37 | 186,456 /s
Planck Circuit | Planck Circuit | Cooling Core | Cooling Core | 3.27 | 3.06 | 62.54 | 193,512 /s

# All Circuits (2.7.0+)
Tier | Circuit | Computation | Heat Limit | Heat Constant | Cool Constant
--- | --- | --- | --- | --- | ---
MAX | Planck Circuit | 360 | 10000 | 8 | -1 
UXV | Quantum Circuit | 320 | 10000 | 10 | -1
UMV | Pico Circuit | 260 | 9500 | 12 | -1
UIV | Optical Mainframe | 260 | 8000 | 20 | -1
UEV | Optical Supercomputer | 240 | 8000 | 22 | -1
UHV | Optical Assembly | 220 | 8000 | 24 | -1
UV | Optical Processor | 200 | 8000 | 26 | -1
UEV | Bioware Mainframe | 260 | 6000 | 30 | -1
UHV | Bioware Supercomputer | 240 | 6000 | 32 | -1
UV | Bioware Assembly | 220 | 6000 | 34 | -1
ZPM | Bioware Processor | 200 | 6000 | 36 | -1
UHV | Wetware Mainframe | 220 | 4000 | 40 | -1
UV | Wetware Supercomputer | 200 | 4000 | 42 | -1
ZPM | Wetware Assembly | 180 | 4000 | 44 | -1
LuV | Wetware Processor | 160 | 4000 | 46 | -1
UV | Crystal Mainframe | 120 | 2000 | 50 | -1
ZPM | Crystal Supercomputer | 100 | 2000 | 52 | -1
LuV | Crystal Assembly | 80 | 2000 | 54 | -1
IV | Crystal Processor | 60 | 2000 | 56 | -1
OC | APU T3 | 240 | 2000 | 40 | -1
OC | APU T2 | 120 | 2000 | 42 | -1
OC | Graphics Card T3 | 100 | 2000 | 44 | -1
OC | CPU T3 | 80 | 2000 | 46 | -1

# All Vents (2.7.0+)
Vent | Heat Limit | Heat Constant | Cool Constant
--- | --- | --- | ---
Cooling Core | 10000 | -1 | 200
Advanced Heat Vent | 8000 | -1 | 160
Overclocked Heat Vent	| 6000 | -1 | 120
Reactor Heat Vent | 4000 | -1 | 80
Heat Vent | 2000 | -1 | 40

# Stable Setups (2.6.0-)
Here are several combinations of circuits and vents for maximizing computation depending on your available resources and progression. The computation and power is per 24 racks or a max length QC. Do not be alarmed if the heat increases rapidly at first--these are designed to converge just below the heat limit of the components. For other circuits, use the actual script.

Comp 1 | Comp 2 | Comp 3 | Comp 4 | Overclock | Overvolt | Computation/s
--- | --- | --- | --- | --- | --- | ---
Graphics Card T3 | Advanced Heat Vent | Advanced Heat Vent | Advanced Heat Vent | 1.05 | 1.07 | 136
Graphics Card T3 | Graphics Card T3 | Advanced Heat Vent | Advanced Heat Vent | 0.71 | 0.80 | 184
CPU T3 | CPU T3 | Advanced Heat Vent | Advanced Heat Vent | 0.47 | 0.80 | 351
APU T3 | APU T3 | Advanced Heat Vent | Advanced Heat Vent | 0.36 | 0.80 | 436
APU Creative | Advanced Heat Vent | Advanced Heat Vent | Advanced Heat Vent | 0.62 | 0.80 | 985
APU Creative | APU Creative | Advanced Heat Vent | Advanced Heat Vent | 0.36 | 0.80 | 1,144
