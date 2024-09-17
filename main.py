import read_csv
import json_converter
import search
import json

def main():
    json_file_path = 'data.json'
    
    # Load existing JSON data from file
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)
    
    # Step 4: Search in JSON
    search_string = input("Enter the user (e.g., 'User 149') to search in the JSON data: ")
    search_result = search.search_json(json_data, search_string)
    
    # Print search results
    if search_result:
        print("Search Result:\n", json.dumps(search_result, indent=4))
    else:
        print(f"User '{search_string}' not found in the JSON data.")

if __name__ == "__main__":
    main()
