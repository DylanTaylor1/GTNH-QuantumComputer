import numpy as np

# ============================= [DO NOT TOUCH] =============================

class RackComponent:
    def __init__(self, circuit):
        d = {
                                # 'NAME' : [COMP, HEAT LIMIT, HEAT CONSTANT, HEAT COEFFICIENT]
                       'Quantum Circuit' : [128, 9000, 48, -0.60], # UXV
                          'Pico Circuit' : [64, 8500, 40, -0.50], # UMV

                         'Bio Mainframe' : [40, 6000, 28, -0.40], # UEV
                 'Bioware Supercomputer' : [42, 6200, 30, -0.40], # UHV
             'Biowareprocessor Assembly' : [40, 5900, 26, -0.35], # UV
                          'Bioprocessor' : [34, 5800, 20, -0.35], # ZPM

                     'Wetware Mainframe' : [38, 6000, 28, -0.40], # UHV
                 'Wetware Supercomputer' : [35, 5700, 22, -0.30], # UV
             'Wetwareprocessor Assembly' : [30, 5600, 18, -0.30], # ZPM
                      'Wetwareprocessor' : [24, 5300, 15, -0.30], # LuV

            'Crystalprocessor Mainframe' : [30, 5500, 18, -0.35], # UV
              'Ultimate Crystalcomputer' : [26, 5400, 16, -0.30], # ZPM
             'Crystalprocessor Assembly' : [20, 5400, 14, -0.25], # LuV
                      'Crystalprocessor' : [18, 5000, 10, -0.15], # IV

                      'Graphics Card T3' : [130, 4500, 111, -0.30], # OC
                                'CPU T3' : [374, 4500, 241, -0.20], # OC
                                'APU T3' : [606, 4500, 398, -0.20], # OC
                          'APU Creative' : [1590, 9000, 1006, -0.30], # OC

                    'Advanced Heat Vent' : [0, 10000, -1, 80], # Vent
                 'Overclocked Heat Vent' : [0, 5000, -1, 40], # Vent
                     'Reactor Heat Vent' : [0, 2500, -1, 20], # Vent
                             'Heat Vent' : [0, 1000, -1, 10]} # Vent

        try:
            self.name, [self.computation, self.heatLimit, self.heatFac, self.heatCoeff] = circuit, d[circuit]
        except:
            print('\033[31m' + '\nERROR: Check Spelling of Component Names\n' + '\033[37m')


class Rack:
    def __init__(self, componentList, overclock, overvolt, racks, voltage):
        self.componentList = componentList
        self.overclock = overclock
        self.overvolt = overvolt
        self.racks = racks
        self.computationList = []
        self.heat = 0

        d = {'ZPM':1, 'UV':4, 'UHV':16, 'UEV':64, 'UIV':256, 'UMV':1024, 'UXV':4096}
        div = d[voltage.upper()]

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
                print('\033[31m' + f'\nVOID: The heat will exceed the limit for {comp.name} ({comp.heatLimit}).' + '\033[37m')
                print(f'Final Heat Approximation: {int(newHeat)}\n')
                break

        # Print Stats
        else:
            heat = format(newHeat, ',.0f')
            comp = format(round(np.mean(self.computationList) * self.racks, 2), ',.0f')
            powerEU = format(int(524288 * self.overclock * self.overvolt * (self.racks + 1)), ',d')
            powerA = max(0.01, round(self.overclock * self.overvolt * (self.racks + 1) / div, 2))

            print('\033[32m' + '\nSAFE: The heat will NOT exceed the limit for any component.' + '\033[37m')
            print(f'Final Heat Approximation: {heat}')
            print(f'Average Computation: {comp}/s')
            print(f'Total Power: {powerEU} EU/t ({powerA}A {voltage.upper()})\n')


    def getComputation(self):
        computation, rackHeat = 0, 0

        for comp in self.componentList:
            if self.heat >= 0:

                if comp.heatFac > 0:
                    h = comp.heatFac * self.overvolt * (self.overclock**2)
                else:
                    h = comp.heatFac

                rackHeat += h * (1 + comp.heatCoeff * self.heat / 10000)
            
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

# =========================== [END DO NOT TOUCH] ===========================

def main():

    # ------------------ EDIT HERE ------------------
    component1 = RackComponent('APU Creative')
    component2 = RackComponent('APU Creative')
    component3 = RackComponent('Advanced Heat Vent')
    component4 = RackComponent('Advanced Heat Vent')

    overclock = 0.36
    overvolt = 0.80

    racks = 2
    voltage = 'UV' # No effect other than determining amps (min: ZPM)
    # -----------------------------------------------

    R = Rack([component1, component2, component3, component4], overclock, overvolt, racks, voltage)


if __name__ == "__main__":
    main()