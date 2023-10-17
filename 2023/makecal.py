import calendar
import datetime
import sys
import os

year = datetime.datetime.now().year

months = [
    "January", "February", "March", "April", "May", "June", "July", "August",
    "September", "October", "November", "December"
]

data = []

def getArgs():
	global year
	if len(sys.argv) > 1:
		year = int(sys.argv[1])

def printf(line = ""):
	global data
	print(line)
	data.append(line)

def saveFile():
	if os.path.exists("readme.md"):
		print("\n\nFiles already exist, file not saved.")
		return
	with open('readme.md', 'w', encoding="utf-8") as file:
		file.write("\n".join(data))
		print("\n\nCalendar generated successfully.")

def generate():
	printf(str(year) + " - Calendar")
	printf("-"*(len(str(year)) + 11))
	printf("")
	printf("---")
	printf(" - ".join(f"[**{months[i]}**](#{months[i]})" for i in range(12)))
	printf("")
	printf("---")

	for month_num in range(1, 13):
		month_name = months[month_num - 1]
		cal = calendar.monthcalendar(year, month_num)

		printf("")
		printf(f"{month_name}\n---")
		printf("| Mon | Tue | Wed | Thu | Fri | Sat | Sun |")
		printf("| :---: | :---: | :---: | :---: | :---: | :---: | :---: |")

		# Print the calendar for the month
		for week in cal:
			week_str = " | ".join(f"{day:<3}" if day > 0 else "   " for day in week)
			printf(f"| {week_str} |")

		printf("| ----- | ----- | ----- | ----- | ----- | ----- | ----- |")
		printf("")
		printf("---")

getArgs()
generate()
saveFile()