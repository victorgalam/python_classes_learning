# time_str = input("Enter time as hh:mm: ")
# hour = int(time_str[0] + time_str[1])
# minute = int(time_str[3] + time_str[4])
# total_minutes = hour * 60 + minute
# print(f"Total minutes = {total_minutes}")


time_str = input("Enter time as hh:mm: ")
hour = int(time_str[:2])
minute = int(time_str[3:])
total_minutes = hour * 60 + minute
print(f"Total minutes = {total_minutes}")
