import sys
import os
import re
import subprocess
from datetime import datetime, date as datex, timedelta
from bs4 import BeautifulSoup

templates = {
	'readme': '# {}\n\n# Questions{}\n\n---\n# [Solution](solution.md)',
	'question': '\n\n---\n## [{}]({})',
	'solution': '# Solution - {}{}'
}

folder = ''
date = ''

def toDate(datestr):
	global date
	date = datetime.strptime(datestr, '%Y-%m-%d').strftime('%d %b %Y')

def preprocess():
	if not os.path.exists(folder):
		os.makedirs(folder)

def getContent(fileName):
	with open(fileName, 'r', encoding='utf-8') as f:
		return f.read()

def generate(content):
	question = ''
	solution = ''

	soup = BeautifulSoup(content, 'html.parser')

	title = soup.find_all('div', class_='text-title-large')[0].text
	url = '/'.join(soup.find_all(attrs={'property': 'og:url'})[0].get('content').split('/')[:5])
	description = str(soup.find_all(attrs={'data-track-load': 'description_content'})[0])

	lang = soup.find_all(class_='h-full w-full', attrs={'data-mode-id': True})[0].get('data-mode-id')
	code = [line for line in soup.find_all('div', class_='view-lines')[0].children]
	code.sort(key=lambda line: int(re.search(r'top\s*:\s*(\d+)', line['style']).group(1)))
	code = '\n'.join([line.text for line in code])

	question = templates['question'].format(title, url) + '\n\n' + description
	solution = templates['question'].format(title, url) + '\n\n' + f'### {lang}\n```{lang}\n{code}\n```\n'

	readme = templates['readme'].format(date, question)
	solution = templates['solution'].format(date, solution)

	with open(folder + '/readme.md', 'w', encoding='utf-16') as file:
		file.write(readme)
	with open(folder + '/solution.md', 'w', encoding='utf-16') as file:
		file.write(solution)

	try: 
		result = subprocess.run(f"python link.py {folder}", shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
	except Exception as e:
		print(e)

	print("Files saved successfully.")

# try:
if len(sys.argv) > 1:
	folder = datetime.strptime(sys.argv[1], '%Y-%m-%d').strftime('%m-%B/%d')
	toDate(sys.argv[1])
else:
	date = (datetime.now() - timedelta(hours=5, minutes=30)).strftime('%d %b %Y')
	folder = (datetime.now() - timedelta(hours=5, minutes=30)).strftime('%m-%B/%d')
preprocess()
generate(getContent('today.test.html'))
# except Exception as e:
# 	print(e)