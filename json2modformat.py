import json

# Load the JSON data
with open("recipesbyIng.json", "r") as file:
    data = json.load(file)

# Function to format data for LLaMA-2
def format_for_llama2(example):
    metadata = ", ".join(example["Metadata"])
    details = json.dumps(example["Details"], separators=(",", ":"))
    ingredients = ", ".join(example["Ingredients"])
    procedure = " ".join(example["Procedure"])
    tags = ", ".join(example["Tags"])
    nutrition = json.dumps(example["Nutrition"], separators=(",", ":"))
    extra_info = json.dumps(example["ExtraInfo"], separators=(",", ":"))
    
    return (
        f"<s>[INST] <<SYS>>\n"
        f" You are an expert chef who provides step-by-step recipes. Use only the provided ingredients and do not add extra ones that are not listed.\n"
        f"<</SYS>>\n"
        f"Metadata: {metadata}\n"
        f"Details: {details}\n"
        f"Ingredients: {ingredients}\n"
        f"Tags: {tags}\n"
        f"Nutrition: {nutrition}\n"
        f"Extra Information: {extra_info}\n"
        f"Task: Provide a step-by-step recipe based on these details and available ingredients, without involving other ingredients.. [/INST]\n"
        f"{procedure} </s>"
    )

# Convert all examples in the dataset
formatted_data = [format_for_llama2(recipe) for recipe in data]

# Save to a text file
# Save to a text file with UTF-8 encoding
with open("formatted_recipes.txt", "w", encoding="utf-8") as file:
    for entry in formatted_data:
        file.write(entry + "\n")
