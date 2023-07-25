#!/usr/bin/env python3
"""hydrogen_spectrum.py"""

# make sure to install tabulate before running program
from tabulate import tabulate

# modified from class program
def bohr():
    e_charge: float = 1.602e-19
    e_mass: float = 9.109e-31
    permittivity: float = 8.854e-12
    h_plank: float = 6.626e-34
    speed_light: float = 2.998e8

    # Bohr's formula for ground state energy
    e_0: float = (pow(e_charge, 4) * e_mass) / (
        8 * pow(permittivity, 2) * pow(h_plank, 2)
    )

    pfund = []
    humphreys = []

    # print("Bohr Model for Hydrogen Spectral Lines")

    # edit the range of numbers to display pfund and humphreys series
    for final_orbit in range(5,7):
        for init_orbit in range(final_orbit + 1, final_orbit + 6):
            # Initial energy level
            e_i: float = -e_0 / pow(init_orbit, 2)
            # Final energy level
            e_f: float = -e_0 / pow(final_orbit, 2)
            # Formula for waveLength in nanometers
            wave_length: float = h_plank * speed_light / (e_i - e_f) * 1e9
            if final_orbit == 5:
                pfund.append(wave_length)
            else:
                humphreys.append(wave_length)
            #print(f"\t{j:>2} -> {k:>2}{wave_length:8.0f} nm")
    
    # return a tuple
    return pfund, humphreys
    # print()

# modified from class program
def rydberg():
    rydberg_constant: float = 1.0967757e7

    pfund = []
    humphreys = []

    # print("Rydberg Formula for Hydrogen Spectral Lines")

     # edit the range of numbers to display pfund and humphreys series
    for k in range(5,7):
        for j in range(k + 1, k + 6):
            # Formula for waveLength in nanometers
            wave_length: float = (
                1 / (rydberg_constant * (1 / pow(k, 2) - 1 / pow(j, 2))) * 1e9
            )
            if k == 5:
                pfund.append(wave_length)
            else:
                humphreys.append(wave_length)
            #print(f"\t{j:>2} -> {k:>2}{wave_length:8.0f} nm")
    
    # return a tuple
    return pfund, humphreys

def main() -> None:
    # using the same functions as in class, except modified the range number
    a, b = bohr()
    c, d = rydberg()

    # print(a,b,c,d)

    data = []

    # create the rows for pfund series
    for i in range(len(a)):
        num = 5 + i + 1
        string = "pfund - " + str(num) + " -> 5"
        data.append([string,a[i],c[i]])

    # create the rows for hamphreys series
    for i in range(len(b)):
        num = 6 + i + 1
        string = "hamphreys - " + str(num) + " -> 6"
        data.append([string,b[i],d[i]])

    # create a table using tabulate lib
    print(tabulate(data, headers=["series", "bohr (nm)", "rydberg (nm)"]))

if __name__ == "__main__":
    main()


'''score 4'''