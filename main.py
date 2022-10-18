print("Hours calculator")

targetHours = 83

totalHours = int(input("How many total hours did you have after last day of work? "))
totalMinutes = int(input("and minutes? "))

remainingHours = targetHours - totalHours
remainingMinutes = 60 - totalMinutes

hourIn = int(input("Hour clocked in? "))
minuteIn = int(input("The minute? "))

hourOut = hourIn + remainingHours
minuteOut = minuteIn + remainingMinutes

if minuteOut > 59:
    hourOut = hourOut + 1

minuteOut = minuteOut % 60

print("The time left you have to work is", remainingHours, "hours and", remainingMinutes, "minutes.")

print("You need to clock out at ", hourOut, ":", minuteOut, sep="")
