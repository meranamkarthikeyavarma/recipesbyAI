import json

# Input and output file paths
input_file = "formatted_recipes.txt"  # Replace with your actual file path
output_file = "data2.jsonl"

# Convert recipes in frecipe.txt into JSONL format
with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
    recipe_lines = []  # To store lines for a single recipe
    for line in infile:
        if line.strip():  # Non-empty line
            recipe_lines.append(line.strip())  # Add line to current recipe
        else:
            # Empty line indicates the end of a recipe
            if recipe_lines:  # If we have collected lines for a recipe
                # Combine all lines into one recipe and format as JSON
                json_entry = {"text": " ".join(recipe_lines)}
                json.dump(json_entry, outfile)
                outfile.write("\n")  # Newline for JSONL format
                recipe_lines = []  # Reset for the next recipe

    # Handle the last recipe if the file doesn't end with a blank line
    if recipe_lines:
        json_entry = {"text": " ".join(recipe_lines)}
        json.dump(json_entry, outfile)
        outfile.write("\n")

print(f"Data converted to JSONL and saved to {output_file}")
