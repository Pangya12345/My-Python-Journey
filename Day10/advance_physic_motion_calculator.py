print("Welcome to the Advance physics motion Calculator")
def calculate_final_velocity(u, a, t):
    final_velocity = u + (a * t)
    return final_velocity

def calculate_displacement(u, t, a):
    displacement = (u * t) + (1 / 2) * (a * t ** 2)
    return displacement

def calculate_average_velocity(u, v):
    average_velocity = (u + v) / 2
    return average_velocity

stop = False
while not stop:
    from art import logo
    print(logo)
    def main():
        initial = float(input("What is the initial velocity? "))
        time = float(input("What is the time? "))
        acceleration = float(input("What is the acceleration? "))
        final_velocity = float(input("What is the final velocity? "))
        Final_velocity = calculate_final_velocity(t = time, a = acceleration, u = initial)
        Displacement = calculate_displacement(t = time, u = initial, a = acceleration)
        Average_velocity = calculate_average_velocity(v = final_velocity, u = initial)
        print(f"Final Velocity: {Final_velocity}")
        print(f"Displacement: {Displacement}")
        print(f"Average Velocity: {Average_velocity}")
    main()
    should_continue = input("Do you want to restart the program again? type 'yes' or 'no' ").lower()
    if should_continue == "no":
        stop = True
    elif should_continue == "yes":
        print("\n" * 10)
print("Finished")
