import requests
from bs4 import BeautifulSoup
from receipebycourse import recipeByCourse

# List of URLs from recipeByCourse
urls = recipeByCourse()

def ingredients(i):
# List to store ingredients for each recipe
        all_ingredients = []

        url = i
        headers = {'User-Agent': 'Mozilla/5.0'}

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the <ul> element containing ingredients
        ingredients_list = soup.find('ul', class_='structured-ingredients__list text-passage')

        # Initialize a list to store the ingredients of the current recipe
        recipe_ingredients = []

        # Check if the ingredients list was found
        if ingredients_list:
            # Find all <li> tags within this <ul> for each ingredient
            ingredients = ingredients_list.find_all('li')
            
            # Loop through each <li> tag and append its text content to the recipe_ingredients list
            for ingredient in ingredients:
                recipe_ingredients.append(ingredient.text.strip())
        else:
            recipe_ingredients.append("Ingredients list not found.")

        # Append the ingredients list of the current recipe to all_ingredients
        
        return recipe_ingredients

