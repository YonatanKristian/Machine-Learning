temps = [[0.0 for h in range(2)] for d in range(4)]
print (temps)

print("\n\n")
temps = [[0.0 for h in range(24)] for d in range(31)]

# 1. the monthly average noon temperature
sum = 0.0

for day in temps:
    sum += day[11]

average = sum / 31

print("Average temperature at noon:", average)

# 2. the highest temperature during the whole month 
highest = -100.0

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

print("The highest temperature was:", highest)

# 3.count the days when the temperature at noon was at least 20 ℃
hotDays = 0

for day in temps:
    if day[11] > 20.0:
        hotDays += 1

print(hotDays, "days were hot.")