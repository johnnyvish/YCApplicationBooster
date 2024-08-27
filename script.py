import os
import re

def sanitize_filename(name):
    # Replace or remove any character that is not alphanumeric, space, hyphen, or underscore
    sanitized_name = re.sub(r'[^a-zA-Z0-9\s\-_]', '', name)
    # Replace spaces with underscores to ensure compatibility
    sanitized_name = sanitized_name.strip().replace(' ', '_')
    return sanitized_name

def detect_and_split(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    output_dir = 'output_files'
    os.makedirs(output_dir, exist_ok=True)

    current_question = None
    current_data = []
    file_counter = 1

    for line in lines:
        if line.startswith("Q:"):
            # Save the previous question data if any
            if current_question:
                save_to_file(file_counter, current_question, current_data, output_dir)
                file_counter += 1
            
            # Extract the question text and sanitize it
            current_question = sanitize_filename(line[2:].strip())
            current_data = []
        else:
            current_data.append(line.strip())

    # Save the last question data
    if current_question:
        save_to_file(file_counter, current_question, current_data, output_dir)

def save_to_file(counter, question, data, output_dir):
    # Create the file name using the sanitized question
    file_name = f"{counter}. {question}.txt"
    file_path = os.path.join(output_dir, file_name)

    with open(file_path, 'w') as file:
        file.write("\n".join(data))

if __name__ == "__main__":
    detect_and_split('input.txt')