# module .py
def function() -> str:
    return (f"Function called from module")

if __name__ == "__main__":
# Code to execute only if this script is run as the main
    print("Module is being *RUN DIRECTLY*")
    print(function())
else:
# Code to execute if this script is imported as a module
    print("Module is being *IMPORTED*")