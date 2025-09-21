# Program to print greeting message based on time (hour of the day)

time = int(input("Enter the time (in hours 0-23): "))

if time >= 1 and time < 12:
    print("Good Morning")

elif time >= 12 and time < 17:
    print("Good Afternoon")

elif time >= 17 and time <= 23:
    print("Good Evening")

elif time == 0:
    print("Good Night")

else:
    print("Invalid time! Please enter between 0 to 23")
