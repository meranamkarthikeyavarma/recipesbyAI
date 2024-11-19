import requests
from bs4 import BeautifulSoup
from receipebycourse import recipeByCourse

# List of URLs from recipeByCourse
urls = recipeByCourse()

def procedure(i):
# URL of the recipe page
    
        url = i

        headers = {'User-Agent': 'Mozilla/5.0'}

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Locate the div containing the procedure steps
        procedure_list = soup.find('div', id='structured-project__steps_1-0')

        # Check if the procedure list was found
        if procedure_list:
            # Find all <p> tags within the procedure div and filter out any unwanted text
            steps = [step.text.strip() for step in procedure_list.find_all('p') if 'Serious Eats' not in step.text]
            
            # Print the cleaned steps list
            # print(steps)
        else:
            print("Procedure steps not found.")

        return steps
