import datetime
import sys
import os
import re

folders = []
data = []
pattern = r'^\d{4}-\d{2}-\d{2}$'

months = [
    "January", "February", "March", "April", "May", "June", "July", "August",
    "September", "October", "November", "December"
]

valid_folders = [f"{(i+1):02}-{months[i]}" for i in range(12)]

month_readme = [None]*12
year = 0

def preProcess():
	global folders, pattern, valid_folders

	if len(sys.argv) > 1:
		for i in range(1, len(sys.argv)):
			if re.match(r'^(%s)/(0[1-9]|[1-2][0-9]|3[0-1])$' % "|".join(valid_folders), sys.argv[i]):
				folders.append(sys.argv[i])
			else:
				print(f"Invalid folder name {sys.argv[i]}")
	else:
		dir_state = os.listdir()
		for month in dir_state:
			if os.path.isdir(month) and month in valid_folders:
				days = os.listdir(month)
				for day in days:
					if os.path.isdir(f"{month}/{day}") and re.match(r"0[1-9]|[12][0-9]|3[01]", day):
						folders.append(f"{month}/{day}")
	
	print(folders)

def readData():
	global data
	with open('readme.md', 'r', encoding="utf-8") as file:
		data = file.readlines()
		year = int(data[0][:4])

def readMonth(month, i):
	global month_readme
	with open(month + '/readme.md', 'r', encoding='utf-8') as file:
		month_readme[i] = file.readlines()

def updateFolder(name):
	global data, month_readme
	month, date = map(int, [name[:2], name[-2:]])
	question = ""
	if month_readme[month-1] == None:
		readMonth(name[:-3], month-1)

	if os.path.exists(name + '/solution.md'):
		with open(name + '/solution.md', 'r', encoding='utf-16') as file:
			lines = file.readlines()
			if len(lines) > 3 and len(lines[3]) > 3:
				question = lines[3][3:-1]
	else:
		return
		

	index = -1
	tmp = month_readme[month-1]
	try:
		index = data.index(f"[{months[month-1]}]({name[:-3]})\n")
	except Exception as e:
		print(e)
	
	if index==-1: return
	for i in range(index, min(index+11, len(data))):
		data[i] = data[i].replace(f"| {date:<3} |", f"| [**{date}**]({name}) |")

	for i in range(min(11, len(tmp))):
		tmp[i] = tmp[i].replace(f"| {date:<3} |", f"| [**{date}**]({name[-2:]}) |")
	
	found, search = False, f"| [{date:02} {months[month-1]} {year}]({name}) |"
	for i in range(160, len(data)):
		if data[i].startswith(search):
			data[i] = f"{search} {question} |\n"
			found = True
			break
	
	if not found:
		data.append(f"{search} {question} |\n")

	found, search = False, f"| [{date:02} {months[month-1]} {year}]({name[-2:]}) |"
	for i in range(11, len(tmp)):
		if tmp[i].startswith(search):
			tmp[i] = f"{search} {question} |\n"
			found = True
			break
	if not found:
		tmp.append(f"{search} {question} |\n")

def process():
	global folders
	for folder in folders:
		updateFolder(folder)

def saveData():
	global data

	for i in range(12):
		if month_readme[i] != None:
			with open(valid_folders[i] + '/readme.md', 'w', encoding='utf-8') as file:
				file.writelines(month_readme[i])

	with open('readme.md', 'w', encoding="utf-8") as file:
		file.writelines(data)
		print("Calendar updated successfully.")

preProcess()
if len(folders)==0:
	print("No valid folder names found. Operation aborted.")
	exit()
readData()
process()
saveData()
