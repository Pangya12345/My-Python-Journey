def calculate_final_velocity(u, a, t):
    v = u + a * t
    return v
def calculate_distance(u, a, t):
    s = (u * t) + (1 / 2) * (a * (t ** 2))
    return s
def calculate_kinetic_energy(m, v):
    KE = (1 / 2) * (m * (v ** 2))
    return KE

stop = False
while not stop:

    def main():
        initial_velocity = float(input("What is the initial velocity? "))
        acceleration = float(input("What is the acceleration? "))
        time = float(input("What is the time? "))
        mass = float(input("What is the mass? "))
        velocity = float(input("What is the velocity? "))
        final_velocity = calculate_final_velocity(u = initial_velocity, a = acceleration, t = time)
        distance = calculate_distance(u = final_velocity, a = acceleration, t = time)
        Kinetic = calculate_kinetic_energy(m = mass, v = velocity)
        print(f"Final velocity: {final_velocity}m/s")
        print(f"Final distance: {distance}m")
        print(f"Kinetic energy: {Kinetic}J")
    main()

    restart = input("Do you want to restart the calculation? type 'yes' or 'no'\n").lower()
    if restart == "no":
        stop = True
    elif restart == "yes":
        print("\n" * 10)
print("Finished")
