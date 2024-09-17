import json

def search_json(json_data, search_string):
    # Loop through each item (dictionary) in the JSON data
    for item in json_data:
        # Check if the 'User' field matches the search string
        if 'User' in item and item['User'].lower() == search_string.lower():
            return item  # Return the matched user's data
    
    # If no match found, return an empty dictionary
    return {}
