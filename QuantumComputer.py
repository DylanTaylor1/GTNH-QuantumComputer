import numpy as np
from colorama import Fore

# ============================= DO NOT TOUCH =============================

class RackComponent:
    def __init__(self, circuit):
        d = {'Quantum Circuit' : [128, 9000, 48, -0.60], # UXV
            'Pico Circuit' : [64, 8500, 40, -0.50], # UMV
            'Nano Circuit' : [48, 8000, 35, -0.45], # UIV
            'Bio Mainframe' : [40, 6000, 28, -0.40], # UEV
            'Bioware Supercomputer' : [42, 6200, 30, -0.40], # UHV
            'Wetware Mainframe' : [38, 6000, 28, -0.40], # UHV
            'Biowareprocessor Assembly' : [40, 5900, 26, -0.35], # UV
            'Wetware Supercomputer' : [35, 5700, 22, -0.30], # UV
            'Crystalprocessor Mainframe' : [30, 5500, 18, -0.35], # UV
            'Bioprocessor' : [34, 5800, 20, -0.35], # ZPM
            'Wetwareprocessor Assembly' : [30, 5600, 18, -0.30], # ZPM
            'Ultimate Crystalcomputer' : [26, 5400, 16, -0.30], # ZPM
            'Quantumprocessor Mainframe' : [22, 5200, 14, -0.30], # ZPM
            'Wetwareprocessor' : [24, 5300, 15, -0.30], # LuV
            'Crystalprocessor Assembly' : [20, 5400, 14, -0.25], # LuV
            'Master Quantumcomputer' : [16, 5100, 13, -0.20], # LuV
            'Nanoprocessor Mainframe' : [16, 5000, 12, -0.20], # LuV
            'High Energy Flow Circuit' : [24, 10000, 16, -0.25], # Other
            'Graphics Card T3' : [130, 4500, 111, -0.30], # Other
            'Accelerated Processing Unit T3' : [1590, 9000, 1006, -0.30], # Other

            'Heat Vent' : [0, 1000, -1, 10],
            'Reactor Heat Vent' : [0, 2500, -1, 20],
            'Overclocked Heat Vent' : [0, 5000, -1, 40],
            'Advanced Heat Vent' : [0, 10000, -1, 80]}

        try:
            self.name = circuit
            [self.computation, self.heatLimit, self.heatFac, self.heatCoeff] = d[circuit]
        except:
            print('ERROR: Check Spelling of Component Names\n')


class Rack:
    def __init__(self, componentList, overclock, overvolt, racks):
        self.componentList = componentList
        self.overclock = overclock
        self.overvolt = overvolt
        self.racks = racks
        self.computationList = []
        self.heat = 0

        # Loop
        oldHeat, newHeat = 0, 10000
        while np.abs(newHeat - oldHeat) > 0:
            oldHeat = newHeat
            self.getComputation()
            self.update()
            newHeat = self.heat
        
        # Check Heat Limits
        for comp in self.componentList:
            if comp.heatLimit < newHeat:
                print(Fore.RED + f'\nEXPLODE: The heat will exceed the limit for {comp.name}' + Fore.WHITE)
                print(f'Final Heat Approximation: {int(newHeat)}\n')
                break

        # Print Stats
        else:
            print(Fore.GREEN + '\nSAFE: The heat will NOT exceed the limit for any component.' + Fore.WHITE)
            print(f'Final Heat Approximation: {int(newHeat)}')
            print(f'Average Computation: {round(np.mean(self.computationList) * self.racks, 2)}/s')

            powerEU = int(524288 * self.overclock * self.overvolt * (self.racks + 1))
            powerA = round(self.overclock * self.overvolt * (self.racks + 1), 2)
            print(f'Total Power: {powerEU} EU/t ({powerA}A UV)\n')

    
    def getComputation(self):
        computation, rackHeat = 0, 0

        for comp in self.componentList:
            if self.heat >= 0:

                if comp.heatFac > 0:
                    c = comp.heatFac * self.overvolt * (self.overclock**2)
                else:
                    c = comp.heatFac

                rackHeat += c * (1 + comp.heatCoeff * self.heat / 10000)
            
                if (self.overvolt * 10 > 7 + np.random.random()):
                    computation += comp.computation * max(0, min(1 + np.random.random() + (self.overvolt - 1) - (self.overclock - 1)/2, min(self.overclock, self.overvolt*2 - 0.25)))

        self.heat += np.ceil(rackHeat)
        self.computationList.append(np.floor(computation))

    
    def update(self):
        if self.heat > 0:
            heatC = 0

            for comp in self.componentList:
                if comp.heatFac < 0:
                    heatC += comp.heatFac * (self.heat / 10000)
                self.heat += max(-self.heat, np.ceil(heatC))
            
            self.heat -= max(int(self.heat / 1000), 1)
        
        elif self.heat < 0:
            self.heat -= min(int(self.heat / 1000), -1)

# ============================= DO NOT TOUCH =============================

def main():

    # ------------------ EDIT HERE ------------------
    component1 = RackComponent('Graphics Card T3')
    component2 = RackComponent('Advanced Heat Vent')
    component3 = RackComponent('Advanced Heat Vent')
    component4 = RackComponent('Advanced Heat Vent')

    overclock = 1.0
    overvolt = 1.0

    racks = 2
    # -----------------------------------------------

    R = Rack([component1, component2, component3, component4], overclock, overvolt, racks)


if __name__ == "__main__":
    main()