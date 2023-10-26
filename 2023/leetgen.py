import requests
import sys
import os
import json
import uuid
import re
import subprocess
from datetime import datetime, date as datex

api_url = 'https://leetcode.com/'
# Headers will contain AuthCode, Cookie, Token, etc.
headers = {}

queries = {
	'content' : {
		'query': '\n    query questionContent($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    content\n  }\n}\n    ',
		'variables': {
			'titleSlug': 'two-sum'
		},
		'operationName': 'questionContent'
	},
	'details' : {
		'query': '\n    query questionTitle($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    title\n    titleSlug\n  }\n}\n    ',
		'variables': {
			'titleSlug': 'two-sum'
		},
		'operationName': 'questionTitle'
	},
	'questionOfToday': {
		"query": "\n    query questionOfToday {\n  activeDailyCodingChallengeQuestion {\n  link\n  }\n}\n    ",
		"variables": {},
		"operationName": "questionOfToday"
	}
}

languages = {'cpp':'cpp', 'java':'java', 'py':'python3'}

templates = {
	'readme': '# {}\n\n# Questions{}\n\n---\n# [Solution](solution.md)',
	'question': '\n\n---\n## [{}. {}]({})',
	'solution': '# Solution - {}{}'
}

links = []
folder = ''
date = ''

def toDate():
	global date
	date = datetime.strptime(folder, '%Y-%m-%d').strftime('%d %b %Y')

def preprocess():
	if not os.path.exists(folder):
		os.makedirs(folder)
	global headers
	with open('leet.headers.json', 'r') as file:
		headers = json.loads(file.read())

def randomName():
	return str(uuid.uuid4()).split('-')[0]

def format(code):
	return re.sub(r'^( {4}|\t {4})*', lambda match: '\t' * (match.group(0).count('\t') + len(match.group(0).replace('\t', '')) // 4), code, flags=re.MULTILINE)

def generate():
	questions = ''
	solutions = ''
	for _ in links:
		if not _.startswith("https://leetcode.com/problems/"):
			continue

		link = '/'.join(_.split('/')[:5])
		slug, url, q = link.split('/')[-1], api_url + 'graphql', dict()

		queries['details']['variables']['titleSlug'] = slug;
		queries['content']['variables']['titleSlug'] = slug;

		res = requests.post(url, headers = headers, json=queries['details'])
		if res.status_code==200:
			q = json.loads(res.text)['data']['question']
			questions += templates['question'].format(q['questionFrontendId'], q['title'], link) + '\n\n'
			solutions += templates['question'].format(q['questionFrontendId'], q['title'], link) + '\n\n'
		
		res = requests.post(url, headers = headers, json=queries['content'])
		if res.status_code==200:
			questions += json.loads(res.text)['data']['question']['content']
		
		for lang in languages:
			res = requests.get(api_url + f'submissions/latest/?qid={q["questionId"]}&lang={languages[lang]}', headers = headers)
			if res.status_code==200:
				solutions += f'### {lang}\n```{lang}\n{json.loads(res.text)["code"]}\n```\n'
	
	readme = templates['readme'].format(date, questions)
	solution = templates['solution'].format(date, solutions)

	with open(folder + '/readme.md', 'w', encoding='utf-16') as file:
		file.write(readme)
	with open(folder + '/solution.md', 'w', encoding='utf-16') as file:
		file.write(solution)

	try: 
		result = subprocess.run(f"python link.py {folder}", shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
	except Exception as e:
		print(e)

	print("Files saved successfully.")

try:
	if len(sys.argv)>1 and sys.argv[1].lower()=="today":
		date = datex.today().strftime('%d %b %Y')
		folder = datex.today().strftime('%Y-%m-%d')
		res = requests.post(api_url + "graphql", headers = headers, json = queries['questionOfToday'])
		slug = json.loads(res.text)['data']['activeDailyCodingChallengeQuestion']['link']
		links.append(api_url[:-1] + slug)
	elif len(sys.argv)>=3:
		folder = sys.argv[1]
		links = sys.argv[2:]
		toDate()
	else:
		folder = input("Enter folder name : ")
		links = list(input("Paste links space separated: ").split())
		toDate()
	preprocess()
	generate()
except Exception as e:
	print(e)