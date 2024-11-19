import requests
from bs4 import BeautifulSoup
from receipebycourse import recipeByCourse

# List of URLs from recipeByCourse
urls = recipeByCourse()

def recipeDetails(i):

    # List to store only Times and Servings data for each recipe
        recipes_data = []

    
        url = i
        headers = {'User-Agent': 'Mozilla/5.0'}
        
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Dictionary to store times and servings for each recipe
        recipe_info = {"Times": {}, "Servings": {}}
        
        # Find the <div> element for times and servings
        times = soup.find('div', class_='project-meta__times-container')
        servings = soup.find('div', class_='project-meta__results-container')

        # Extract times data
        if times:
            labels = times.find_all(class_='meta-text__label')
            data = times.find_all(class_='meta-text__data')
            
            for label, datum in zip(labels, data):
                recipe_info["Times"][label.text.strip()] = datum.text.strip()
        else:
            recipe_info["Times"] = "Time information not found."

        # Extract servings data
        if servings:
            labels = servings.find_all(class_='meta-text__label')
            data = servings.find_all(class_='meta-text__data')
            
            for label, datum in zip(labels, data):
                recipe_info["Servings"][label.text.strip()] = datum.text.strip()
        else:
            recipe_info["Servings"] = "Servings information not found."

        return recipe_info
        
        # Add only the Times and Servings information to the list
        # recipes_data.append(recipe_info)

    # Print the list to verify
