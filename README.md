# Introduction
This is a python script for determining the stability of a rack in a Quantum Computer. Each rack has four total slots for circuits (which add heat) and vents (which dissipate heat). When using circuits and vents together, the heat will stabilize at some value 0-10,000. It is important to keep the heat below the maximum heat limit for every component in the rack, otherwise there will be an explosion. Where exactly the heat will stabilize is not immediately obvious nor easily calculated which is where this script can help. Note that every rack is independent of every other rack which means one CANNOT have all circuits and another all vents even if they are part of the same Quantum Computer.

# Usage
  - Download the python script QuantumComputer.py (only file that is needed). If you do not have a way to easily run python scripts, you can copy the code into an online IDE (https://www.online-python.com/)
  - Enter the names of the components that you would like to test under the "EDIT HERE" section at the bottom of the code. The names must be exactly as portrayed in the table (ie. Graphics Card T3)
  - Enter your Overclock and Overvolt values as well as how many racks are on your Quantum Computer
  - Run the script. It will output the final heat approximation (where it will stabilize) and whether or not the Quantum Computer will explode. If it is safe, it will also tell you the average computation and total power consumption. This assumes all racks are identical.

![Edit Here](media/edithere.png?)

![Output](media/output.png?)

# Stable Setups
Here are a few stable combinations of circuits and vents (last tested on GTNH 2.4.0) that you should use to maximize computation depending on your available resources. Computation here is per rack.

Component 1 | Component 2 | Component 3 | Component 4 | Overclock | Overvolt | Computation/s |
--- | --- | --- | --- | --- | --- | ---
Graphics Card T3 | Advanced Heat Vent | Advanced Heat Vent | Advanced Heat Vent | 1.05 | 1.07 | 136
Graphics Card T3 | Graphics Card T3 | Advanced Heat Vent | Advanced Heat Vent | 0.71 | 0.80 | 184
APU Creative | Advanced Heat Vent | Advanced Heat Vent | Advanced Heat Vent | 0.62 | 0.80 | 985
APU Creative | APU Creative | Advanced Heat Vent | Advanced Heat Vent | 0.36 | 0.80 | 1,144

# All Circuits
Tier | Circuit | Computation | Heat Limit | Initial Heat | Heat Coefficient
--- | --- | --- | --- | --- | ---
UXV | Quantum Circuit | 128 | 9000 | 48 | -0.60
UMV | Pico Circuit | 64 | 8500 | 40 | -0.50
UIV	| Nano circuit | 48	| 8000 | 35 | -0.45
UEV	| Bio Mainframe	| 40 | 6000 | 28 | -0.40
UHV	| Bioware Supercomputer | 42 | 6200 | 30 | -0.40
UHV | Wetware Mainframe | 38 |6000 | 25 | -0.40
UV | Biowareprocessor Assembly | 40 | 5900 | 26 | -0.35
UV | Wetware Supercomputer | 35 | 5700 | 22 | -0.30
UV | Crystalprocessor Mainframe | 30 | 5500 | 18 | -0.35
ZPM	| Bioprocessor | 34 | 5800 | 20 | -0.35
ZPM | Wetwareprocessor Assembly | 30 | 5600 | 18 | -0.30
ZPM | Ultimate Crystalcomputer | 26 | 5400 | 16 | -0.30
ZPM | Quantumprocessor Mainframe | 22 | 5200 | 14 | -0.30
LuV	| Wetwareprocessor | 24 | 5300 | 15 | -0.30
LuV | Crystalprocessor Assembly | 20 | 5400 | 14 | -0.25
LuV | Master Quantumcomputer | 16 | 5100 | 13 | -0.20
LuV | Nanoprocessor Mainframe | 16 | 5000 | 12 | -0.20
N/A | High Energy Flow Circuit | 24 | 10000 | 16 | -0.25
N/A | CPU T3 | 374 | 4500 | 241 | -0.20
N/A | Graphics Card T3 | 130 | 4500 | 111 | -0.30
N/A | APU T3 | 606 | 4500 | 398 | -0.20
N/A | APU Creative | 1590 | 9000 | 1006 | -0.30

# All Vents
Vent | Heat Limit | Initial Heat | Heat Coefficient
--- | --- | --- | ---
Heat Vent | 1000 | -1 | 10
Reactor Heat Vent | 2500 | -1 | 20
Overclocked Heat Vent	| 5000 | -1 | 40
Advanced Heat Vent | 10000 | -1 | 80
