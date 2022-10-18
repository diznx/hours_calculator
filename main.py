print("Hours calculator")

targetHours = 84

totalHours = int(input("How many total hours did you have after last day of work? "))
totalMinutes = int(input("and minutes? "))

remainingHours = targetHours - totalHours
remainingMinutes = 60 - totalMinutes

hourIn = int(input("What hour did you clock in? "))
minuteIn = int(input("and the minute? "))

hourOut = hourIn + remainingHours
minuteOut = minuteIn + remainingMinutes


if minuteOut > 59:
    hourOut = hourOut + 1

minuteOut = minuteOut % 60

print("The time left you have to work is", remainingHours, "hours and", remainingMinutes, "minutes.")
print("You need to clock out at ", hourOut, ":", minuteOut, sep="")
