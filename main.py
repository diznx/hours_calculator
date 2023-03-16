target_minutes = 5040

total_hours = int(input("Total hours: ")) * 60
total_minutes = int(input("and minutes: "))
total_time = total_hours + total_minutes

hour_in = int(input("Hour clocked in: "))
minute_in = int(input("Minute in: "))

hour_left = (target_minutes - total_time) // 60
minute_left = (target_minutes - total_time) % 60

print(f"You have {hour_left} hours and {minute_left} minutes left.")

hour_out = hour_in + hour_left
minute_out = (minute_in + minute_left) % 60
if minute_out >= 0.60:
    hour_out = hour_out + 1

print(f"Clock out at {hour_out}:{minute_out}.")
