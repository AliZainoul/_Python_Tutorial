def save_help_to_file(function_names: list, file_name: str):
    """Save the help documentation of functions to a file."""
    with open(file_name, 'w') as f:
        for function_name in function_names:
            f.write(f"Documentation for {function_name}:\n")
            f.write(help(function_name))
            f.write("\n" + "="*40 + "\n")

def main():
    functions = ["len", "input", "print"]
    file_name = "function_help.txt"
    save_help_to_file(functions, file_name)
    print(f"Documentation saved to {file_name}.")

if __name__ == "__main__":
    main()
