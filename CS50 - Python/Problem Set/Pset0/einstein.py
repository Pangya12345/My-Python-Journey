mass = int(input("m: ")) # --------> receive mass from user
def energy(real_mass):
    light = 300000000
    energy = real_mass * (light ** 2)
    print(f"E: {energy}") # 
energy(mass) # ------> set up the function to calculate and print total energy