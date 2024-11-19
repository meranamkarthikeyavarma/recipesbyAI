from bs4 import BeautifulSoup
import requests

def extraInfo(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Locate the main div containing the sections
    main_div = soup.find('div', id='structured-project__steps_1-0')
    if not main_div:
        return "Main instructions section not found."

    # Dictionary to store each section separately
    extra_info = {
        "Special Equipment": [],
        "Notes": [],
        "Make-Ahead and Storage": []
    }

    current_section = None
    for tag in main_div.find_all(['h2', 'p']):
        if tag.name == 'h2':  # Check if the tag is a header
            if tag.text.strip() == "Special Equipment":
                current_section = "Special Equipment"
            elif tag.text.strip() == "Notes":
                current_section = "Notes"
            elif tag.text.strip() == "Make-Ahead and Storage":
                current_section = "Make-Ahead and Storage"
            else:
                current_section = None
        elif tag.name == 'p' and current_section:  # If <p> and a section header was previously found
            extra_info[current_section].append(tag.text.strip())

    # Remove empty sections
    extra_info = {k: v for k, v in extra_info.items() if v}

    return extra_info

