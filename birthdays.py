#Read birthday csv and push onto message stack

# Revision History
#09-Sep-2023, J. Nolan, Created from original concept
#28-Sep-2023, J. Nolan, Added days to next birthday
#29-Dec-2024, J. Nolan, Fixed next year bug

import csv
import datetime
from datetime import date
birthday_file = '/home/pi/birthday_minder/birthdays.csv'

birthday_message = []

def read_birthdays():
	print("\n-------------------------------------------")
	print("+Jim's Birthday Minder Rev 3, 29-Dec-2023 +")
	print("-------------------------------------------")

	if (len(birthday_message) > 0):
		return

	# count the number of birthdays in the birthdays.csv file
	last_line_num = row_count(birthday_file)
	#print("Rows found in: ", str(birthday_file), ": ", str(last_line_num))

	d = datetime.date.today()
	day = f'{d.day:02d}'
	month = f'{d.month:02d}'
	year = f'{d.year:04d}'
	year_int = d.year 

	# find today birthdays if there are any and que then up
	with open(birthday_file) as csvfile:
		csvReader = csv.reader(csvfile, delimiter=',')
		for row in csvReader:
			if row[0] == month and row[1] == day:
				age = year_int - int(row[2])
				birthday_message.append(" ")
				birthday_message.append(str(age) + " years old!") 
				birthday_message.append(row[3])
				birthday_message.append(row[4])
				birthday_message.append("Happy Birthday:")
				print("Found birthday today Month: "+row[4]+"-"+row[3]+"-"+row[2]+"-"+row[1]+"-"+row[0])

	found_next_birthday = False
	days_until_birthday = 0

	# find next birthday
	with open(birthday_file) as csvfile:
		csvReader = csv.reader(csvfile, delimiter=',')
		for row in csvReader:
			if ((row[0] == month and row[1] > day) or (row[0] > month)):

				# Calculate number of days until next birthday
				date1 = date(int(year),int(row[0]),int(row[1])) #Y-M-D
				delta = date1 - d
				days_until_birthday = delta.days 
				birthday_message.append("days until birthday: " + str(days_until_birthday))
				print("Days to next birthday: ", days_until_birthday)

				#Calculate their age
				age = year_int - int(row[2])
				birthday_message.append(str(age) + " years old!") 

				# First name line
				birthday_message.append(row[3])

				# Second name line
				birthday_message.append(row[4])
				birthday_message.append("Next: "+str(row[0])+"/"+str(row[1]))
				print("Found (next) birthday today Month: "+row[4]+"-"+row[3]+"-"+row[2]+"-"+row[1]+"-"+row[0])
				found_next_birthday = True
				break;

	# If the next birthday search didn't find one then grab the first birthday in the list
	if found_next_birthday == False:
		with open(birthday_file) as csvfile:
			csvReader = csv.reader(csvfile, delimiter=',')
			# read the first row
			row = next(csvReader)

			# Calculate number of days until next birthday
			date1 = date(int(year)+1,int(row[0]),int(row[1])) #Y-M-D
			delta = date1 - d
			days_until_birthday = delta.days 
			birthday_message.append("days until birthday: " + str(days_until_birthday))
			print("Days to next birthday (new year): ", days_until_birthday)

			age = year_int - int(row[2])+1  #add year for wrap around to next year
			birthday_message.append(str(age) + " years old!")

			birthday_message.append(row[3])
			birthday_message.append(row[4])

			birthday_message.append("Next: "+str(row[0])+"/"+str(row[1]))
			print("Use first birthday of next year: "+row[4]+"-"+row[3]+"-"+row[2]+"-"+row[1]+"-"+row[0])

def row_count(filename):
    with open(filename) as in_file:
        return sum(1 for _ in in_file)

def get_birthdays():
	return birthday_message.pop()

def birthday_list_not_empty():
	if (len(birthday_message)>0):
		return (True)
	else:
		return (False)

#read_birthdays()
#while (birthday_list_not_empty()):
	#print(get_birthdays())
