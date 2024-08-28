import os

def combine_text_files(input_folder, output_file):
    try:
        with open(output_file, 'w', encoding='utf-8') as outfile:  # Use UTF-8 encoding
            for filename in sorted(os.listdir(input_folder)):
                if filename.endswith('.txt'):
                    file_path = os.path.join(input_folder, filename)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as infile:  # Use UTF-8 encoding
                            outfile.write("--------------------- Next Application --------------------- \n")
                            outfile.write(f"--------------------- {filename} ---------------------\n")  # Write the name of the next file
                            outfile.write(infile.read())
                            outfile.write("\n")  # Add a newline after each file's content
                    except UnicodeDecodeError as e:
                        print(f"Error reading {filename}: {e}")
    except FileNotFoundError as e:
        print(f"Error: {e}")

input_folder = r'C:\Users\aksha\Desktop\YCApplicationBooster\Top 10 apps'  # Replace with the correct path
output_file = r'C:\Users\aksha\Desktop\YCApplicationBooster\combined_output.txt'  # The name of the output file

combine_text_files(input_folder, output_file)

print(f"All text files in {input_folder} have been combined into {output_file}")
