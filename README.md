# Introduction
This is a python script for determining the stability of a Quantum Computer. Every rack has four total slots for either circuits (to generate heat and computation packets) or vents (to dissipate heat). When turned on, the heat will stabilize at some value 0-10,000. It is important to keep the heat below the maximum heat limit for every component in the rack, otherwise the component(s) will void. Where exactly the heat will stabilize is neither obvious nor easily calculated which is where this script can help. Note that every rack is independent of every other rack meaning you CANNOT have all circuits in one and all vents in another even if they are both part of the same Quantum Computer.

# Usage
  - Download the appropriate `QuantumComputer.py` script depending on your version of GTNH. If you do not have a way to easily run python scripts, you can copy the code into an online IDE (https://www.online-python.com/).
  - Enter the names of the components that you would like to test under the "EDIT HERE" section at the bottom of the code. The names must be exactly as portrayed in the dictionary at the top (ie. APU Creative).
  - Enter the Overclock and Overvolt values as well as how many racks are on your Quantum Computer. The voltage setting has no effect other than determining amps.
  - Run the script. It will output the final heat approximation (where it will stabilize) and whether or not any of the components will void from too much heat. If it is safe, it will also tell you the total computation and total power consumption assuming all racks are identical.

![Edit Here](media/edithere.png?)

![Output](media/output.png?)

# Stable Setups (2.7.0+)
Here are a few stable combinations of circuits and vents for GTNH versions greater than or equal to 2.7.0 that should maximize computation at different stages of the game. The computation here is for a full 24 racks which means a maximum length Quantum Computer can produce up to 151,248 computation per second at a cost of 28,290,580 EU/t (53.96A UV).

Comp 1 | Comp 2 | Comp 3 | Comp 4 | Overclock | Overvolt | Amps (UV) | Computation/s
--- | --- | --- | --- | --- | --- | --- | ---
Crystal Mainframe | Advanced Heat Vent | Advanced Heat Vent | Advanced Heat Vent | 1.74 | 1.41 | 15.33 | 10,440
Crystal Mainframe | Crystal Mainframe | Advanced Heat Vent | Advanced Heat Vent | 1.22 | 1.00 | 7.62 | 13,656
APU Creative | Advanced Heat Vent | Advanced Heat Vent | Advanced Heat Vent | 1.85 | 1.53 | 17.69 | 23,088
APU Creative | APU Creative | Advanced Heat Vent | Advanced Heat Vent | 1.44 | 1.03 | 9.27 | 30,312
Wetware Mainframe | Advanced Heat Vent | Advanced Heat Vent | Advanced Heat Vent | 2.14 | 1.88 | 25.14 | 27,576
Wetware Mainframe | Wetware Mainframe | Advanced Heat Vent | Advanced Heat Vent | 1.61 | 1.27 | 12.78 | 33,984
Bio Mainframe | Advanced Heat Vent | Advanced Heat Vent | Advanced Heat Vent | 2.59 | 2.37 | 38.36 | 45,864
Bio Mainframe | Bio Mainframe | Advanced Heat Vent | Advanced Heat Vent | 1.92 | 1.61 | 19.32 | 53,352
Optical Mainframe | Advanced Heat Vent | Advanced Heat Vent | Advanced Heat Vent | 3.19 | 3.01 | 60.01 | 67,536
Optical Mainframe | Optical Mainframe | Advanced Heat Vent | Advanced Heat Vent | 2.31 | 2.06 | 29.74 | 74,400
Pico Circuit | Advanced Heat Vent | Advanced Heat Vent | Advanced Heat Vent | 3.96 | 3.80 | 94.05 | 101,472
Pico Circuit | Pico Circuit | Advanced Heat Vent | Advanced Heat Vent | 2.84 | 2.61 | 46.33 | 107,448
Quantum Circuit | Advanced Heat Vent | Advanced Heat Vent | Advanced Heat Vent | 4.31 | 4.10 | 110.44 | 143,976
Quantum Circuit | Quantum Circuit | Advanced Heat Vent | Advanced Heat Vent | 3.04 | 2.84 | 53.96 | 151,248

# All Circuits (2.7.0+)
Tier | Circuit | Computation | Heat Limit | Heat Constant | Cool Constant
--- | --- | --- | --- | --- | ---
UXV | Quantum Circuit | 320 | 10000 | 10 | -1
UMV | Pico Circuit | 260 | 9500 | 12 | -1
UIV | Optical Mainframe | 260 | 8000 | 20 | -1
UEV | Optical Computer | 240 | 8000 | 22 | -1
UHV | Optical Assembly | 220 | 8000 | 24 | -1
UV | Optical Processor | 200 | 8000 | 26 | -1
UEV | Bio Mainframe | 260 | 6000 | 30 | -1
UHV | Bioware Supercomputer | 240 | 6000 | 32 | -1
UV | Biowareprocessor Assembly | 220 | 6000 | 34 | -1
ZPM | Bioprocessor | 200 | 6000 | 36 | -1
UHV | Wetware Mainframe | 220 | 4000 | 40 | -1
UV | Wetware Supercomputer | 200 | 4000 | 42 | -1
ZPM | Wetwareprocessor Assembly | 180 | 4000 | 44 | -1
LuV | Wetwareprocessor | 160 | 4000 | 46 | -1
UV | Crystalprocessor Mainframe | 120 | 2000 | 50 | -1
ZPM | Ultimate Crystalcomputer | 100 | 2000 | 52 | -1
LuV | Crystalprocessor Assembly | 80 | 2000 | 54 | -1
IV | Crystalprocessor | 60 | 2000 | 56 | -1
OC | APU Creative | 240 | 2000 | 40 | -1
OC | APU T3 | 120 | 2000 | 42 | -1
OC | Graphics Card T3 | 100 | 2000 | 44 | -1
OC | CPU T3 | 80 | 2000 | 46 | -1

# All Vents (2.7.0+)
Vent | Heat Limit | Heat Constant | Cool Constant
--- | --- | --- | ---
Advanced Heat Vent | 10000 | -1 | 200
Overclocked Heat Vent	| 8000 | -1 | 160
Reactor Heat Vent | 6000 | -1 | 120
Heat Vent | 4000 | -1 | 80

# Stable Setups (2.6.0-)
Here are a few stable combinations of circuits and vents for GTNH versions less than or equal to 2.6.1 that should maximize computation depending on your available resources. Note that the current best setup is available to you as soon as you build your first Quantum Computer. The computation here is per rack which means a full length Quantum Computer can produce up to 27,456 computation per second at a cost of 3,774,873 EU/t (7.2A UV).

Comp 1 | Comp 2 | Comp 3 | Comp 4 | Overclock | Overvolt | Computation/s
--- | --- | --- | --- | --- | --- | ---
Graphics Card T3 | Advanced Heat Vent | Advanced Heat Vent | Advanced Heat Vent | 1.05 | 1.07 | 136
Graphics Card T3 | Graphics Card T3 | Advanced Heat Vent | Advanced Heat Vent | 0.71 | 0.80 | 184
CPU T3 | CPU T3 | Advanced Heat Vent | Advanced Heat Vent | 0.47 | 0.80 | 351
APU T3 | APU T3 | Advanced Heat Vent | Advanced Heat Vent | 0.36 | 0.80 | 436
APU Creative | Advanced Heat Vent | Advanced Heat Vent | Advanced Heat Vent | 0.62 | 0.80 | 985
APU Creative | APU Creative | Advanced Heat Vent | Advanced Heat Vent | 0.36 | 0.80 | 1,144