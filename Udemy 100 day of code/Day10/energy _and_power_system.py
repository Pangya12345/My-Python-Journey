stop = False
while not stop:
    from art import logo
    print(logo)
    energy_and_power = {}
    name = input("What is the name of the student? ")
    energy_and_power[name] = {}
    print(energy_and_power)
    def calculate_work(f, d):
        w = f * d
        return w
    def calculate_power(work, t):
        power = work * t
        return power
    def calculate_efficiency(useful_power, input_power):
        efficiency = (useful_power / input_power) * 100
        return efficiency

    def main():
        force = float(input("What is the force? "))
        distance = float(input("What is the distance? "))
        time = float(input("What is the time? "))
        i_power = float(input("What is the input power? "))
        Work = calculate_work(force, distance)
        round_work = round(Work, 2)
        energy_and_power[name]["Work"] = round_work
        Power = calculate_power(work = calculate_work(force, distance), t = time)
        round_power = round(Power, 2)
        energy_and_power[name]["Power"] = round_power
        Efficiency = calculate_efficiency(input_power = i_power, useful_power = calculate_power(work = calculate_work(force, distance), t = time))
        round_efficiency = round(Efficiency, 2)
        energy_and_power[name]["Efficiency"] = round_efficiency
        print(f"Work_done: {round_work}J")
        print(f"Power: {round_power}W(Watt)")
        print(f"Efficiency: {round_efficiency}%")
        print(energy_and_power)
    main()

    restart = input("Do you want to restart the calculation? type 'yes' or 'no'\n").lower()
    if restart == "yes":
        print("\n" * 10)
    elif restart == "no":
        stop = True
print("The game is finish! Well done!")
