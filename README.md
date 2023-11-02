## Introduction
This is a python script for determining the stability of a rack in a Quantum Computer. Each rack has four total slots for circuits (which add heat) and vents (which dissipate heat). When using circuits and vents together, the heat will stabilize at some value 0-10000 which is equivalent to 0%-100%. It is important to keep the heat below the maximum heat limit for every component in the rack, otherwise there will be an explosion. Where exactly the heat will stabilize is not immediately obvious nor easily calculated which is where this script can help. Note that every rack is independent of every other rack which means one CANNOT have all circuits and another all vents even if they are part of the same Quantum Computer.

## Stable Combinations
Here are a few stable combinations of circuits and vents that you should use to maximize computation at different points in the game.

Attempt | #1 | #2 | #3 | #4 | #5 | #6 | #7 | #8 | #9 | #10 | #11
--- | --- | --- | --- |--- |--- |--- |--- |--- |--- |--- |---
Seconds | 301 | 283 | 290 | 286 | 289 | 285 | 287 | 287 | 272 | 276 | 269
