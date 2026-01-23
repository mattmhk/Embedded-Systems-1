start_time = 6.5
print("Start time expressed in hours:", start_time)
speed = 5
total_time= 0
distance = 5
total_time = total_time + distance / speed
speed= 10
distance = 10
total_time = total_time + distance / speed
speed=5
distance = 1
total_time = total_time + distance / speed
print("Total running time expressed in hours:", total_time)
end_time = start_time + total_time
end_time_minutes = (end_time - int(end_time)) * 60
print(" End time is:", int(end_time), "hours and", round(end_time_minutes), "minutes")