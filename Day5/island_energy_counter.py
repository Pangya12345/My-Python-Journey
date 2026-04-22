energy_stone = [3, 8, 12, 5, 7, 10, 6]
stone_energy = 0

for stone in energy_stone:
    if stone % 2 == 0:
        stone_energy += stone
print(f"Total Energy: {stone_energy}")
