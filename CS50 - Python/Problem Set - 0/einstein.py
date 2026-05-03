mass = int(input("m: "))
def energy(real_mass):
    light = 300000000
    energy = real_mass * (light ** 2)
    print(f"E: {energy}")
energy(mass)
