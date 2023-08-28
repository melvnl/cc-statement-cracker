from datetime import datetime, timedelta

def generate_dates(start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        yield current_date.strftime('%d%m%Y')
        current_date += timedelta(days=1)

# Get today's date
today = datetime.today().date()

# Define the start date
start_date = datetime(1972, 1, 1).date()

# Generate dates
dates = list(generate_dates(start_date, today))

# Save dates to a text file
with open("dates.txt", "w") as file:
    for date in dates:
        file.write(date + "\n")
