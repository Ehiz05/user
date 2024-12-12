import sys


def reverse_and_number_lines(input_file, output_file):
    
    try:
        
        with open(input_file, 'r') as infile:
            lines = infile.readlines()  
       
        modified_lines = [
            f"{len(lines) - i}. {line.strip()}" for i, line in enumerate(reversed(lines))
        ]
       
        modified_content = "\n".join(modified_lines)
        
        with open(output_file, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified content has been written to {output_file}.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except IOError as e:
        print(f"An error occurred while processing the file: {e}")


input_file_path = sys.argv[1]  
output_file_path = sys.argv[2]  

reverse_and_number_lines(input_file_path, output_file_path)
