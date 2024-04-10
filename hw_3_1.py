from datetime import datetime

def get_days_from_today(date):
    '''
    This function calculates the total amount 
    of days between the given date and the current date
    '''
    # Convert the date string in format 'YYYY-MM-DD' into a datetime object
    date_obj = datetime.strptime(date, '%Y-%m-%d').date()
    
    # Get current date
    today = datetime.now().date()
    
    # Calculate the difference in days
    difference = date_obj - today
    
    # Return total amount of days
    return difference.days 

# For example:
calculate = get_days_from_today('1988-05-18') 
print(calculate)