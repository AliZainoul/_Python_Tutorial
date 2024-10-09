import sys
import os

# Get the absolute path to the OOP directory
oop_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the OOP directory to sys.path so packageA can be imported
sys.path.append(oop_dir)

# Now you can import from packageA
from packageA.test_class import TestClass

# Test the access
obj = TestClass()
try:
    print("Accessing in packageB:", obj._TestClass__private_method(), obj._TestClass__private_attr)
except AttributeError as e:
    print("Failed to access in packageB:", e)
