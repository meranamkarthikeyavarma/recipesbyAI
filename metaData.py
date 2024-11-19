import requests
from bs4 import BeautifulSoup
import json
from receipebycourse import recipeByCourse

# List of URLs from recipeByCourse
urls = recipeByCourse()

# Initialize an empty list to store all recipe data
def metaData(i):
        recipes_data = []

      # Limiting to the first 5 URLs for demonstration
        url = i
        headers = {'User-Agent': 'Mozilla/5.0'}
        
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the <div> element with the specified ID
        procedure_list = soup.find('div', id='breadcrumbs-new_1-0')
        
        # Check if procedure_list is found and prepare data for JSON
        if procedure_list:
            # Split procedure into a list by line breaks or any other delimiter
            procedure_steps = [step.strip() for step in procedure_list.text.split('\n') if step.strip()]
        else:
            procedure_steps = ["Procedure not found"]

        return procedure_steps
        
       