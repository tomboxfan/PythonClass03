

# floor division - // : find quotient
# modulus        - %  : find reminder

def years_days(minutes):
   hours_count = minutes // 60
   day_count = hours_count // 24
   year_count = day_count // 365
   remaining_day_count = day_count % 365
   print(f"{minutes} minutes is approximately {year_count} years and {remaining_day_count} days")

# Step 1) Read total minutes from user, save into a variable
user_input_minutes = int(input("Enter the number of minutes: "))

# Step 2) call the function
years_days(user_input_minutes)