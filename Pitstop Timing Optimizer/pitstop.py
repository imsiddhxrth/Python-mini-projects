# 🏁 Pit Stop Timing Optimizer 🔧
#
# 1. Ask the user for the total race time in seconds.
# 2. Ask how many pit stops were made.
# 3. Ask for the average pit stop duration (in seconds).
#
# Then:
# - Calculate the total pit stop time.
# - Calculate the percentage of the race spent in the pits.
# - Round the percentage to 2 decimal places.
#
# Finally, print all of the following:
# - Total pit stop time in seconds
# - Percentage of race time spent in pits
# - A final message if pit time > 5% of the race: "You need a new pit crew. 🛠️"
# Get user input
total_race_time = float(input("Enter the total race time in seconds: "))
num_pit_stops = int(input("Enter the number of pit stops made: "))
avg_pit_stop_duration = float(input("Enter the average pit stop duration in seconds: "))
# Calculate total pit stop time
total_pit_stop_time = num_pit_stops * avg_pit_stop_duration
# Calculate percentage of race  time spent in pits
percentage_pit_time = (total_pit_stop_time / total_race_time) * 100
# Round percentage to 2 decimal places
percentage_pit_time = round(percentage_pit_time, 2)
# Print results
print(f"Total pit stop time: {total_pit_stop_time} seconds")
print(f"Percentage of race time spent in pits: {percentage_pit_time}%")
if percentage_pit_time > 5:
    print("You need a new pit crew. 🛠️")