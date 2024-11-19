import requests
from bs4 import BeautifulSoup

# URL of the recipe page
url = 'https://www.seriouseats.com/fan-tuan-recipe-8739042'

headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the <div> element with the specified class
procedure_list = soup.find('p', id='mntl-sc-block_118-0')
procedure_list2 = soup.find('p', id=  'mntl-sc-block_120-0')
print(procedure_list.text.strip())
print(procedure_list2.text.strip())
