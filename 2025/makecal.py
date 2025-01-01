import calendar
import datetime
import sys
import os
import uuid

year = datetime.datetime.now().year

months = [
    "January", "February", "March", "April", "May", "June", "July", "August",
    "September", "October", "November", "December"
]

data = []

def randomName():
	return str(uuid.uuid4()).split("-")[0]

def getArgs():
	global year
	if len(sys.argv) > 1:
		year = int(sys.argv[1])

def printf(line = ""):
	global data
	print(line)
	data.append(line)
	return line

def saveFile():
	if os.path.exists("readme.md"):
		print("\n\nFiles already exist, file not saved.")
		return
	with open('readme.md', 'w', encoding="utf-8") as file:
		file.write("\n".join(data))
		print("\n\nCalendar generated successfully.")

def saveMonthFile(name, content):
	with open(name, 'w', encoding="utf-8") as file:
		file.write("\n".join(content))

def generate():
	printf(str(year) + " - Calendar")
	printf("-"*(len(str(year)) + 11))
	printf("")
	printf("---")
	printf(" - ".join(f"[**{months[i]}**](#{months[i]})" for i in range(12)))
	printf("")
	printf("---")

	backup_folder = f"backup_{randomName()}"

	for month_num in range(1, 13):
		month_name = months[month_num - 1]
		folder = f"{month_num:02}-{month_name}"
		cal = calendar.monthcalendar(year, month_num)
		
		month_data = []

		# If folder exists then move to backup
		if os.path.exists(folder):
			if not os.path.exists(backup_folder):
				os.makedirs(backup_folder)
			os.system(f"move {folder} {backup_folder}/{folder}")
		
		os.makedirs(folder)
		
		printf("")
		printf(f"[{month_name}]({folder}#{month_name})\n---")
		month_data.append(f"{month_name}\n---")
		month_data.append(printf("| Mon | Tue | Wed | Thu | Fri | Sat | Sun |"))
		month_data.append(printf("| :---: | :---: | :---: | :---: | :---: | :---: | :---: |"))

		# Print the calendar for the month
		for week in cal:
			week_str = " | ".join(f"{day:<3}" if day > 0 else "   " for day in week)
			month_data.append(printf(f"| {week_str} |"))

		month_data.append(printf("| ----- | ----- | ----- | ----- | ----- | ----- | ----- |"))
		month_data.append(printf(""))
		month_data.append(printf("---"))

		month_data.append("")
		month_data.append("Questions\n---\n| Day | Question |\n| --- | --- |\n")

		saveMonthFile(folder + "/readme.md", month_data)
	
	printf("")
	printf("Questions\n---\n| Day | Question |\n| --- | --- |\n")

getArgs()
generate()
saveFile()