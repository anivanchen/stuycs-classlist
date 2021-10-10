import requests
from bs4 import BeautifulSoup

print("Enter your teacher's name in the format firstInitialLastName. Example: dholmes")
teacherName = str(input('Teacher Name (ex. dholmes): '))
print("Enter your term name in the format [fall/spring]year. Example: fall2021")
term = str(input("Enter the term (fall2021): "))

url = 'http://bert.stuy.edu/{}/{}/pages.py?page=submit_homework'.format(teacherName, term)
page = requests.get(url)
substring = ''

soup = BeautifulSoup(page.content, 'html.parser')
script = soup.find('script').string.split(' ++i)', 1)[0].split(';')

for line in script: 
  if 'students[' in line:
    start = line.find('"') + len('"')
    end = line.find('|')
    period = line[start:end]

    start = line.replace('|', '', 1).find('|') + len('|')
    end = line.replace('"', '', 1).find('"')
    name = line[start+1:end+1]

    substring = substring + period + ' | ' + name + '\n'

file = open('ClassList.txt', 'w')
file.write(substring)
file.close()
