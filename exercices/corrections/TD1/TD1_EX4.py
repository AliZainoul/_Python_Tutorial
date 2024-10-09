def fix_indentation(input_file: str, output_file: str):
    """Fix the indentation of a Python file and add comments to each line."""
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        lines = infile.readlines()
        indent_level = 0
        for line in lines:
            stripped_line = line.strip()
            # Skip empty lines
            if not stripped_line:
                outfile.write("\n")
                continue
            # Adjust indentation based on the Python code structure
            if stripped_line.endswith(":"):
                indent_level += 1
            if stripped_line.startswith("return") or stripped_line.startswith("pass"):
                indent_level -= 1
            
            # Write the indented line and add a comment
            outfile.write("    " * indent_level + stripped_line + "  # Re-indented line\n")
        
    print(f"Re-indented file saved to {output_file}.")

def main():
    input_file = input("Enter the name of the Python file to fix indentation: ")
    output_file = input("Enter the name of the output file: ")
    fix_indentation(input_file, output_file)

if __name__ == "__main__":
    main()