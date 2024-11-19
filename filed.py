import requests
from bs4 import BeautifulSoup
from receipebycourse import recipeByCourse

# List of URLs from recipeByCourse
urls = recipeByCourse()

def filed(i):

# URL of the recipe page
    
        url = i
        headers = {'User-Agent': 'Mozilla/5.0'}

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the main <div> with the specified class
        procedure_list = soup.find('div', class_="loc tag-nav-content")

        # Check if the procedure list was found
        if procedure_list:
            # Extract text from each relevant tag (such as <a> or <span>) within this div
            tags = [tag.text.strip() for tag in procedure_list.find_all(['a', 'span', 'div']) if tag.text.strip()]
            # print(tags)  # This will print each tag's text as a separate list item
        else:
            print("Specified div not found.")
        return  tags
