import numpy as np

# ============================= [DO NOT TOUCH] =============================

class RackComponent:
    def __init__(self, circuit):
        d = {
                                # 'NAME' : [COMP, HEAT LIMIT, HEAT CONSTANT, COOL CONSTANT]
                       'Quantum Circuit' : [320, 10000, 10, -1], # UXV
                          'Pico Circuit' : [260, 9500, 12, -1], # UMV

                     'Optical Mainframe' : [260, 8000, 20, -1], # UIV
                      'Optical Computer' : [240, 8000, 22, -1], # UEV
                      'Optical Assembly' : [220, 8000, 24, -1], # UHV
                     'Optical Processor' : [200, 8000, 26, -1], # UV

                         'Bio Mainframe' : [260, 6000, 30, -1], # UEV
                 'Bioware Supercomputer' : [240, 6000, 32, -1], # UHV
             'Biowareprocessor Assembly' : [220, 6000, 34, -1], # UV
                          'Bioprocessor' : [200, 6000, 36, -1], # ZPM

                     'Wetware Mainframe' : [220, 4000, 40, -1], # UHV
                 'Wetware Supercomputer' : [200, 4000, 42, -1], # UV
             'Wetwareprocessor Assembly' : [180, 4000, 44, -1], # ZPM
                      'Wetwareprocessor' : [160, 4000, 46, -1], # LuV

            'Crystalprocessor Mainframe' : [120, 2000, 50, -1], # UV
              'Ultimate Crystalcomputer' : [100, 2000, 52, -1], # ZPM
             'Crystalprocessor Assembly' : [80, 2000, 54, -1], # LuV
                      'Crystalprocessor' : [60, 2000, 56, -1], # IV

                          'APU Creative' : [240, 2000, 40, -1], # OC
                                'APU T3' : [120, 2000, 42, -1], # OC
                      'Graphics Card T3' : [100, 2000, 44, -1], # OC
                                'CPU T3' : [80, 2000, 46, -1], # OC

                    'Advanced Heat Vent' : [0, 10000, -1, 200], # Vent
                 'Overclocked Heat Vent' : [0, 8000, -1, 160], # Vent
                     'Reactor Heat Vent' : [0, 6000, -1, 120], # Vent
                             'Heat Vent' : [0, 4000, -1, 80]} # Vent

        try:
            self.name, [self.computation, self.heatLimit, self.heatConstant, self.coolConstant] = circuit, d[circuit]
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
            if comp.heatLimit <= newHeat:
                print('\033[31m' + f'\nVOID: The heat will exceed the limit for {comp.name} ({comp.heatLimit}).' + '\033[37m')
                print(f'Final Heat Approximation: {int(newHeat)}\n')
                break

        # Print Stats
        else:
            heat = format(newHeat, ',.0f')
            comp = format(round(np.mean(self.computationList) * self.racks, 2), ',.0f')
            powerEU = format(int(131072 * self.overclock * self.overvolt * (self.racks + 1)), ',d')
            powerA = max(0.01, round(self.overclock * self.overvolt * (self.racks + 1) / div, 2))

            print('\033[32m' + '\nSAFE: The heat will NOT exceed the limit for any component.' + '\033[37m')
            print(f'Final Heat Approximation: {heat}')
            print(f'Average Computation: {comp}/s')
            print(f'Total Power: {powerEU} EU/t ({powerA}A {voltage.upper()})\n')


    def getComputation(self):
        computation, rackHeat = 0, 0

        for comp in self.componentList:
            if self.heat >= 0:

                if comp.heatConstant > 0:
                    h = comp.heatConstant * (self.overclock) * (self.overvolt)**2
                else:
                    h = -10

                rackHeat += h * (1 + comp.coolConstant * self.heat / 100000)

                if (self.overvolt > np.random.random()):
                    computation += comp.computation * max(0, (1 + self.overclock**2) / (1 + (self.overclock - self.overvolt)**2))

        self.heat += np.ceil(rackHeat)
        self.computationList.append(np.floor(computation))


    def update(self):

        if self.heat > 0:
            heatC = 0

            for comp in self.componentList:
                if comp.heatConstant < 0:
                    heatC += comp.heatConstant * (self.heat / 10000)

            self.heat += max(-self.heat, np.ceil(heatC))
            self.heat -= max(int(self.heat / 1000), 20)

        elif self.heat < 0:
            self.heat -= min(int(self.heat / 1000), -1)

# =========================== [END DO NOT TOUCH] ===========================

def main():

    # ------------------ EDIT HERE ------------------
    component1 = RackComponent('Wetware Mainframe')
    component2 = RackComponent('Wetware Mainframe')
    component3 = RackComponent('Advanced Heat Vent')
    component4 = RackComponent('Advanced Heat Vent')

    overclock = 1.61
    overvolt = 1.27

    racks = 1
    voltage = 'UV' # No effect other than determining amps (min: ZPM)
    # -----------------------------------------------

    R = Rack([component1, component2, component3, component4], overclock, overvolt, racks, voltage)


if __name__ == "__main__":
    main()