import requests
import sys
import os
import json
import uuid
import re
from datetime import datetime


api_url = 'https://workat.tech/api/ps/'
# Headers will contain AuthCode, Cookie, Token, etc.
headers = {}

links = []
folder = ''
date = ''

languages = {'1235' : 'cpp', '1311' : 'java', '1421' : 'py'}

readmeTmp = '''
# {}

# Questions{}

---
# [Solution](solution.md)
'''

solutionTmp = '# Solution - {}{}'

questionTmp = '\n\n---\n## [{}. {}]({})'
questionSolutionTmp = '\n\n---\n## [{}. {}]({})'

def toDate():
	global date
	date = datetime.strptime(folder, '%Y-%m-%d').strftime('%d %b %Y')

def preprocess():
	if not os.path.exists(folder):
		os.makedirs(folder)
	global headers
	with open(".headers.json", 'r') as file:
		headers = json.loads(file.read())

def randomName():
	return str(uuid.uuid4()).split("-")[0]

def format(code):
	return re.sub(r'^( {4}|\t {4})*', lambda match: '\t' * (match.group(0).count('\t') + len(match.group(0).replace('\t', '')) // 4), code, flags=re.MULTILINE)

def generate():
	questions = ""
	solutions = ""
	index = 1
	for link in links:
		if 'leetcode.com' in link:
			leetLink = f'[(LeetCode)]({link})'
			questions = questions.replace("${ExtraLink}", leetLink + " ${ExtraLink}")
			solutions = solutions.replace("${ExtraLink}", leetLink + " ${ExtraLink}");
			continue
		if 'workat.tech' not in link:
			continue
		questions = questions.replace("${ExtraLink}", "")
		solutions = solutions.replace("${ExtraLink}", "")
		id = link.split("/")[-1]
		url = api_url + id
		res = requests.get(url, headers = headers)
		if res.status_code==200:
			data = json.loads(res.text)
			name = data['name']
			questions += questionTmp.format(index, name, link) + " ${ExtraLink}\n\n"
			questions += data["content"]
			solutions += questionSolutionTmp.format(index, name, link) + " ${ExtraLink}\n\n" 
		
		url = api_url + "codes/" + id
		res = requests.get(url, headers = headers)
		if res.status_code==200:
			data = json.loads(res.text)
			for lang in data['languages']:
				solutions += f"### {languages[lang]}\n```{languages[lang]}\n"
				solutions += format(data['languages'][lang]['savedCode'])
				solutions += "\n```\n"
		else:
			print(res)
		index += 1
	
	questions = questions.replace("${ExtraLink}", "")
	solutions = solutions.replace("${ExtraLink}", "")
	readme = readmeTmp.format(date, questions)
	solution = solutionTmp.format(date, solutions)

	suffix = ""
	if os.path.exists(folder + "/readme.md") or os.path.exists(folder + "/solution.md"):
		print("Files already exist, saving files with random names.")
		suffix = "_" + randomName()
	
	with open(folder + '/readme' + suffix+ '.md', 'w', encoding="utf-16") as file:
		file.write(readme)
	with open(folder + '/solution' + suffix + '.md', 'w', encoding="utf-16") as file:
		file.write(solution)
	print("Files saved successfully.")

if len(sys.argv)>=3:
	folder = sys.argv[1]
	links = sys.argv[2:]

	# toDate()
	# preprocess()
	# generate()
	try:
		toDate()
		preprocess()
		generate()
	except Exception as e:
		print(e)
		print(e.with_traceback)
else:
	folder = input("Enter folder name : ")
	links = list(input("Paste links space separated: ").split())
	try:
		toDate()
		preprocess()
		generate()
	except Exception as e:
		print(e)
		print(e.with_traceback)