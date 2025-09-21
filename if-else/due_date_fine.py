# Program to calculate due date (10 days after issue date) and fine if overdue

# Take issue date from user in format DD/MM/YYYY
issue_date = input("Enter the issue date (dd/mm/yyyy): ")
day, month, year = map(int, issue_date.split("/"))

# Add 10 days to issue date
due_day = day + 10
due_month = month
due_year = year

# Handle month overflow (assuming 30 days in every month for simplicity)
if due_day > 30:
    due_day -= 30
    due_month += 1
    if due_month > 12:
        due_month = 1
        due_year += 1

print(f"Your due date is: {due_day}/{due_month}/{due_year}")

# Take current date
current_date = input("Enter the current date (dd/mm/yyyy): ")
cur_day, cur_month, cur_year = map(int, current_date.split("/"))

# Fine calculation (only if same month & year, simplified)
if (cur_year == due_year) and (cur_month == due_month):
    if cur_day > due_day:
        fine = (cur_day - due_day) * 10   # 10 Rs fine per day
        print(f"Your fine is: {fine} Rs")
    else:
        print("No fine, returned on time ✅")
else:
    print("Fine calculation across months/years not handled in this version.")
