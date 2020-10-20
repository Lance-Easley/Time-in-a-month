#This progam takes any month and will give you the amount of hours, minutes, or
#seconds in that given month.

#initiate variable 'days'.
days = 0
#ask the user to input whether they want weeks, days, hours, minutes, or seconds.
time_type = str(input('Would you like weeks, days, hours, minutes, or \
seconds?\n'))
#readout variables allow the "Spelling Error" message to display the misspelled string.
time_readout = time_type
#turns the entire string to lowercase so the input is not case sensitive.
time_type = time_type.casefold()
#checks to see if the input string is acceptable.
if time_type == 'hours' or time_type == 'minutes' or time_type == 'seconds'\
	or time_type == 'days' or time_type == 'weeks':
	pass
else:
	print('Spelling Error:', time_readout)
	#waits for the user to press enter to continue
	input('Press Enter to continue...')
	exit()
#ask the user to input which month they want.
month = str(input('What month would you like? \n'))
month_readout = month
month = month.casefold()
#checks which month was entered, then assigns days the number of days in the month.
if month == 'february':
#asks the user for what year this february is in just in case it is a leap year.
    year = int(input('What year would you like? \n')) % 4
if month == 'january':
		days = 31
elif month == 'february':
    if year == 0:
        days = 29
    else:
        days = 28
elif month == 'march':
		days = 31
elif month == 'april':
		days = 30
elif month == 'may':
		days = 31
elif month == 'june':
		days = 30
elif month == 'july':
		days = 31
elif month == 'august':
		days = 31
elif month == 'september':
		days = 30
elif month == 'october':
		days = 31
elif month == 'november':
		days = 30
elif month == 'december':
		days = 31
else:
	print('Spelling Error:', month_readout)
	input('Press Enter to continue...')
	exit()
#calculates how many hours, minutes, or seconds there are given the value of 'days'.
weeks = days // 7
days_left = days % 7
hours = days * 24
minutes = days * 24 * 60
seconds = days * 24 * 60 * 60
#checks to see which time type was entered, then displays the relevant text.
if time_type == 'hours':
    print('There are', hours, 'hours in that month')
elif time_type == 'minutes':
    print('There are', minutes, 'minutes in that month')
elif time_type == 'seconds':
    print('There are', seconds, 'seconds in that month')
elif time_type == 'days':
	print('There are', days, 'days in that month')
elif time_type == 'weeks' and days_left == 1:
	print('There are', weeks, 'weeks and', days_left, 'day in that month')
elif time_type == 'weeks' and days_left == 0:
	print('There are', weeks, 'weeks in that month')
elif time_type == 'weeks':
	print('There are', weeks, 'weeks and', days_left, 'days in that month')
input('Press Enter to continue...')
#yeet