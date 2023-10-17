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

def preProcess():
	global folders, pattern
	if len(sys.argv) > 1:
		for i in range(1, len(sys.argv)):
			if re.match(pattern, sys.argv[i]):
				folders.append(sys.argv[i])
			else:
				print(f"Invalid folder name {sys.argv[i]}")
	else:
		dir_state = os.listdir()
		for val in dir_state:
			if os.path.isdir(val) and re.match(pattern, val):
				folders.append(val)

def readData():
	global data
	with open('readme.md', 'r', encoding="utf-8") as file:
		data = file.readlines()

def updateFolder(name):
	global data
	year, month, date = map(int, name.split("-"))
	if month>12 or month<1 or date>31 or date<1:
		return
	index = -1
	try:
		index = data.index(f"{months[month-1]}\n")
	except Exception as e:
		print(e)
	
	if index==-1: return
	for i in range(index, min(index+8, len(data))):
		data[i] = data[i].replace(f" {date:<2} ", f" [**{date}**]({name}) ")

def process():
	global folders
	for folder in folders:
		updateFolder(folder)

def saveData():
	global data
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
