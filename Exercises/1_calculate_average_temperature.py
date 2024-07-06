"""
A script to calculate the average temperature.

Inputs:
    - number of days
    - temperature value for each day

Output:
    - average temperature
    - temperature values above average, if any.

"""

number_of_days = int(input("How many day's average temperature do you want to calculate? "))

total_temperature = 0
daily_temperature = []

for i in range(number_of_days):
    day_temperature = int(input(f"Day {i + 1} temperature: "))
    daily_temperature.append(day_temperature)
    total_temperature += day_temperature

average_temperature = round((total_temperature / number_of_days), 2)
above_average = [str(temperature) for temperature in daily_temperature if temperature > average_temperature]

print(f"\nAverage temperature is: {average_temperature}")

if len(above_average) > 0:
    print(f"\n{len(above_average)} day(s) temperature is above the average. {', '.join(above_average)}\n")
