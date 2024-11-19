import requests
from bs4 import BeautifulSoup
from receipebycourse import recipeByCourse

# List of URLs from recipeByCourse
urls = recipeByCourse()

def nut(i):
    url = i
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Initialize an empty dictionary for nutrition
    nutrition_dict = {}

    # Try to find the nutrition table
    nutrition_table = soup.find('tbody', class_='nutrition-info__table--body')

    if nutrition_table:
        # If nutrition information exists, process it
        nutrition_list_items = [item.strip() for item in nutrition_table.text.split('\n') if item.strip()]
        nutrition_dict = {nutrition_list_items[i+1]: nutrition_list_items[i] for i in range(0, len(nutrition_list_items), 2)}
    else:
        print("Nutrition information not found.")
    
    # Return the nutrition dictionary (empty if not found)
    return nutrition_dict

