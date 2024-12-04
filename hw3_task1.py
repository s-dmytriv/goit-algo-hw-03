from datetime import datetime 

def get_days_from_today(date): 
    try:
        date_new = datetime.strptime(date, '%Y-%m-%d').date() #transform string into date format
        delta = date_new - datetime.today().date() #difference in days between today's and entered date
        return delta.days
    except ValueError:
        print("Invalid format. Please enter a date in a format YYYY-MM-DD")

days = get_days_from_today("2024-11-12") #call the function
print(days)