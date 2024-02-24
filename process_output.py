
import argparse
import json
DELIMETER = '#' * 100
def process_file(input_file, output_file):
    
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    part_after_generating_responses = content.split("Generating responses...\n", 1)[-1]

    parts = part_after_generating_responses.split(DELIMETER)
    
    items = []
    
    # Process each part
    for part in parts[1:-1]: # Exclude the last part
        # Initialize a dict to store the prompt and generation
        item = {"prompt": "", "generation": ""}
        if "[92m" in part and "[0m" in part:
            # Extract the prompt and generation parts
            prompt_part, generation_part = part.split("[0m", 1)
            prompt_part = prompt_part.split("[92m")[-1] # Remove the [92m marker from the start
            # Store the parts in the dict
            item["prompt"] = prompt_part
            item["generation"] = generation_part
        items.append(item)
    
    # Convert the list of items to JSON
    json_data = json.dumps(items, indent=4)
    
    # Write the JSON data to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(json_data)

if __name__ == "__main__":
    # Set up the argument parser
    parser = argparse.ArgumentParser(description='Process a text file and save the results in JSON format.')
    parser.add_argument('--input', type=str, help='The input text file.', required=True)
    parser.add_argument('--output', type=str, help='The output JSON file.', required=True)
    
    # Parse command-line arguments
    args = parser.parse_args()
    
    # Process the file based on input and output arguments
    process_file(args.input, args.output)