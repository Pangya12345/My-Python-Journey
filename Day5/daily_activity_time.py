print("Welcome to Daily Activity time Analyzer")
activity_times = [15, 45, 90, 30, 10, 60, 120]

shortime_total_time = 0
Medium_time_total_time = 0
long_time_total_time = 0

for activity in activity_times:
    if activity < 30:
        shortime_total_time += activity
    elif 30 <= activity <= 60:
        Medium_time_total_time += activity
    else:
        long_time_total_time += activity

print(f"Short time total: {shortime_total_time}")
print(f"Medium time total: {Medium_time_total_time}")
print(f"Long time total: {long_time_total_time}")
