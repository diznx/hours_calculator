print("Hours calculator")

targetHours = 83

targetMinutes = 0

totalHours = int(input("How many hours did you have after your last day of work? "))

totalMinutes = int(input("and minutes? "))

remainingHours = targetHours - totalHours

remainingMinutes = 60 - totalMinutes

hourIn = int(input("Now I need the time you clocked in.  What hour was it? "))

minuteIn = int(input("and the minute? "))

hourOut = hourIn + remainingHours

minuteOut = minuteIn + remainingMinutes

if minuteOut > 59:
    hourOut = hourOut + 1

minuteOut = minuteOut % 60

print("The time left you have to work is", remainingHours, "hours and", remainingMinutes, "minutes.")

print("You need to clock out at ", hourOut, ":0", minuteOut, sep="")