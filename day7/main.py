import numpy as np

positions = np.array([int(p) for p in open("input.txt").read().split(",")])

part_one_fuel = -1
for i in range(max(positions)):
    fuel = abs(positions - i)
    total_fuel = sum(fuel)
    if part_one_fuel == -1:
        part_one_fuel = total_fuel
    else:
        part_one_fuel = total_fuel if total_fuel < part_one_fuel else part_one_fuel


print("Part 1:", part_one_fuel)

part_two_fuel = -1
for i in range(max(positions)):
    length = abs(positions - i)
    fuel = (length + 1) * (length / 2)
    total_fuel = sum(fuel)
    if part_two_fuel == -1:
        part_two_fuel = total_fuel
    else:
        part_two_fuel = total_fuel if total_fuel < part_two_fuel else part_two_fuel

print("Part 2:", part_two_fuel)

# Find number at Min, Max and Middle
# Choose smallest two as the next range
# continue until number is selected!
