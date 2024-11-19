import requests
from bs4 import BeautifulSoup

def recipeByCourse():
    url = 'https://www.seriouseats.com/recipes-by-course-5117906'
    urls = []  

    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the div with the specified ID
    container = soup.find(id='mntl-taxonomysc-article-list_1-0')

    # Check if the container was found
    if container:
        # Find all <a> tags within this div
        links = container.find_all('a', href=True)
        
        # Loop through each <a> tag and print the href attribute
        for link in links:
            # print(link['href'])
            urls.append(link['href'])


    else:
        print("Div with the specified ID not found.")

    return urls


