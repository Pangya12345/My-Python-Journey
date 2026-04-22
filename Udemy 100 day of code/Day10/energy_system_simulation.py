print("Welcome to the 'Energy System Simulation' program")

def calculate_work(f, d):
    w = f * d
    return w
def calculate_power(work, time):
    power = work / time
    return power
def calculate_efficiency(useful_output, useful_input):
    efficiency = (useful_output / useful_input) * 100
    return efficiency
system_energy_data = {}
def main():
    enough = False
    while not enough:
        from art import logo
        print(logo)
        name = input("What is the name of the station? ")
        system_energy_data[name] = {}
        Force = float(input("What is the force? "))
        system_energy_data[name]["Force"] = Force
        Distance = float(input("What is the distance? "))
        system_energy_data[name]["Distance"] = Distance
        Time = float(input("What is the time? "))
        system_energy_data[name]["Time"] = Time
        i_power = float(input("What is the input power? "))
        system_energy_data[name]["Input Power"] = i_power
        continue_adding = input("Do you want to continue adding new data? type 'yes' or 'no'")
        if continue_adding == "yes":
            print("\n" * 10)
        elif continue_adding == "no":
            enough = True
main()
for key in system_energy_data:
    Work = calculate_work(d = system_energy_data[key]["Distance"], f = system_energy_data[key]["Force"])
    Power = calculate_power(time = system_energy_data[key]["Time"], work = Work)
    efficiency = calculate_efficiency(useful_input = system_energy_data[key]["Input Power"], useful_output = Power)
    print(f"{key}")
    print(f"Work-done: {Work}J")
    print(f"Power: {Power}Watt")
    print(f"Efficiency: {efficiency}%")
