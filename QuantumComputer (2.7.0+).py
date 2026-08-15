import numpy as np

# ============================= [DO NOT TOUCH] =============================

class rackComponent:
    def __init__(self, circuit):
        d = {
                       # 'NAME' : [COMP, HEAT LIMIT, HEAT CONSTANT, COOL CONSTANT]
               'Planck Circuit' : [360, 10000, 8, -1], # MAX
              'Quantum Circuit' : [320, 10000, 10, -1], # UXV
                 'Pico Circuit' : [260, 9500, 12, -1], # UMV

            'Optical Mainframe' : [260, 8000, 20, -1], # UIV
        'Optical Supercomputer' : [240, 8000, 22, -1], # UEV
             'Optical Assembly' : [220, 8000, 24, -1], # UHV
            'Optical Processor' : [200, 8000, 26, -1], # UV

            'Bioware Mainframe' : [260, 6000, 30, -1], # UEV
        'Bioware Supercomputer' : [240, 6000, 32, -1], # UHV
             'Bioware Assembly' : [220, 6000, 34, -1], # UV
            'Bioware Processor' : [200, 6000, 36, -1], # ZPM

            'Wetware Mainframe' : [220, 4000, 40, -1], # UHV
        'Wetware Supercomputer' : [200, 4000, 42, -1], # UV
             'Wetware Assembly' : [180, 4000, 44, -1], # ZPM
            'Wetware Processor' : [160, 4000, 46, -1], # LuV

            'Crystal Mainframe' : [120, 2000, 50, -1], # UV
        'Crystal Supercomputer' : [100, 2000, 52, -1], # ZPM
             'Crystal Assembly' : [80, 2000, 54, -1], # LuV
            'Crystal Processor' : [60, 2000, 56, -1], # IV

                       'APU T3' : [240, 2000, 40, -1], # OC
                       'APU T2' : [120, 2000, 42, -1], # OC
             'Graphics Card T3' : [100, 2000, 44, -1], # OC
                       'CPU T3' : [80, 2000, 46, -1], # OC

                 'Cooling Core' : [0, 10000, -1, 200], # Vent
           'Advanced Heat Vent' : [0, 8000, -1, 160], # Vent
        'Overclocked Heat Vent' : [0, 6000, -1, 120], # Vent
            'Reactor Heat Vent' : [0, 4000, -1, 80], # Vent
                    'Heat Vent' : [0, 2000, -1, 40]} # Vent

        try:
            self.name, [self.computation, self.heatLimit, self.heatConstant, self.coolConstant] = circuit, d[circuit]
        except:
            print('\033[31m' + '\nERROR: Check Spelling of Component Names\n' + '\033[37m')


def getHeat(components, overclock, overvolt):
    oldHeat, newHeat = -1, 0
    while abs(newHeat - oldHeat) > 0:
        oldHeat = newHeat

        # Component Heat
        rackHeat = 0
        for comp in components:
            if newHeat >= 0:
                h = comp.heatConstant * overclock * (overvolt**2) if comp.heatConstant > 0 else -10
                rackHeat += h * (1 + comp.coolConstant * newHeat / 100000)

        newHeat += np.ceil(rackHeat)

        # Computer Heat
        if newHeat > 0:

            heatC = 0
            for comp in components:
                if comp.heatConstant < 0:
                    heatC += comp.heatConstant * (newHeat / 10000)

            newHeat += max(-newHeat, np.ceil(heatC))
            newHeat -= max(int(newHeat / 1000), 20)

        elif newHeat < 0:
            newHeat -= min(int(newHeat / 1000), -1)

        newHeat = max(0, newHeat)

    return int(newHeat)


def getComputation(components, overclock, overvolt, racks):
    computation = min(overvolt, 1) * sum(component.computation for component in components) * (1 + overclock**2) / (1 + (overclock - overvolt)**2)
    return int(computation) * racks


def getPower(voltage, overclock, overvolt, racks):
    d = {'ZPM':1, 'UV':4, 'UHV':16, 'UEV':64, 'UIV':256, 'UMV':1024, 'UXV':4096}

    powerEU = max(32768, 131072 * overclock * overvolt)
    powerA = max(0.01, overclock * overvolt * (racks + 1) / d[voltage.upper()])

    return int(powerEU) * (racks + 1), round(powerA, 2)


def printStats(components, voltage, overclock, overvolt, heat, computation, powerEU, powerA):

    # Heat is NOT safe
    for comp in components:
        if heat >= comp.heatLimit:
            print('\033[31m' + f'\nVOID: The final heat exceeds the limit for {comp.name} ({comp.heatLimit}).' + '\033[37m')
            print(f'Overclock/Overvolt: {overclock}/{overvolt}')
            print(f'Final Heat Approximation: {int(heat)}\n')
            break

    # Heat is safe
    else:
        print('\033[32m' + '\nSAFE: The final heat does NOT exceed the limit for any component.' + '\033[37m')
        print(f'Overclock/Overvolt: {overclock:.2f}/{overvolt:.2f}')
        print(f'Final Heat Approximation: {heat:,d}')
        print(f'Average Computation: {computation:,d}/s')
        print(f'Total Power: {powerEU:,d} EU/t ({powerA}A {voltage.upper()})\n')

# =========================== [END DO NOT TOUCH] ===========================

def main():

    # ------------------ EDIT HERE ------------------
    components = [
        rackComponent('APU T3'),
        rackComponent('APU T3'),
        rackComponent('Cooling Core'),
        rackComponent('Cooling Core')]

    overclock = 1.43
    overvolt = 1.03
    optimize = True # Ignore the custom OC/OV values to instead find the optimal OC/OV values

    racks = 24
    voltage = 'UV' # No effect other than determining amps (min:ZPM)
    # -----------------------------------------------

    if optimize:
        maxHeat = min(component.heatLimit for component in components) - 20
        overclock, overvolt = 1, 1

        # Start with Big Increments
        while getHeat(components, overclock + 0.1, overvolt + 0.1) < maxHeat:
            overclock += 0.1
            overvolt += 0.1

        bestComputation = getComputation(components, overclock, overvolt, racks)

        # Narrow the Search and Fine Tune
        for oc in np.arange(max(1, overclock - 0.4), overclock + 0.4, 0.01):
            for ov in np.arange(max(1, overvolt - 0.4), overvolt + 0.4, 0.01):
                computation = getComputation(components, oc, ov, racks)
                if getHeat(components, oc, ov) < maxHeat and computation > bestComputation:
                    bestComputation = computation
                    overclock, overvolt = oc, ov

    heat = getHeat(components, overclock, overvolt)
    computation = getComputation(components, overclock, overvolt, racks)
    powerEU, powerA = getPower(voltage, overclock, overvolt, racks)

    printStats(components, voltage, overclock, overvolt, heat, computation, powerEU, powerA)


if __name__ == "__main__":
    main()