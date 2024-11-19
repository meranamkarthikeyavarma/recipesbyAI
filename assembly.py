import json
from metaData import metaData
from recipeDetails import recipeDetails
from ingredients import ingredients
from procedure import procedure
from filed import filed
from nut import nut
from recipebyingredients import recipeByIngredients
from extraInfo import extraInfo

# List of URLs from recipeByCourse
urls = recipeByIngredients()
i = 1   

# Initialize a list to hold all recipe data
all_recipes = []

for url in urls:  # Modify the range as needed
    # Fetch each part of the recipe data
    k = ['https://www.seriouseats.com/lentil-recipes-7565962', 'https://www.seriouseats.com/bean-salad-recipes-for-summer', 'https://www.seriouseats.com/bean-soup-recipes-7965768', 'https://www.seriouseats.com/bean-recipes-7565978', 'https://www.seriouseats.com/recipes-that-celebrate-the-humble-bean', 'https://www.seriouseats.com/easy-bean-soups', 'https://www.seriouseats.com/vegan-vegetarian-sweet-potato-and-bean-chili40', 'https://www.seriouseats.com/vegan-vegetarian-sweet-potato-and-bean-chili', 'https://www.seriouseats.com/how-to-make-bean-salad-radicchio-almonds', 'https://www.seriouseats.com/the-vegan-experience-i-like-breakfast-once-ag', 'https://www.seriouseats.com/how-to-grow-bean-sprouts-in-a-jar', 'https://www.seriouseats.com/latin-american-cuisine-frijoles-molidos-refried-beans', 'https://www.seriouseats.com/greek-butter-bean-salad-tomatoes-dill-oregano']
    if url in k:
        print('skipped')
    else:

        print(url)  
        i = i+1
        print(i)
        metadata = metaData(url)
        recipedetails = recipeDetails(url)
        ingredientslist = ingredients(url)
        process = procedure(url)
        tags = filed(url)
        nutrients = nut(url)
        extrainfo = extraInfo(url)
        
        # Combine all data into a single dictionary for the recipe
        recipe_data = {
            "Metadata": metadata,
            "Details": recipedetails,
            "Ingredients": ingredientslist,
            "Procedure": process,
            "Tags": tags,
            "Nutrition": nutrients,
            "ExtraInfo":extrainfo
        }
        
        # Append the recipe data to the all_recipes list
        all_recipes.append(recipe_data)

# Save all recipes to a JSON file
with open("recipesbyIng.json", "w") as file:
    json.dump(all_recipes, file, indent=4)
    

print("Recipe data has been successfully saved to recipes.json")
