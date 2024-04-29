# Example of break and continue statements
for i in range(10): 
    if i == 5:
        break # Exit the loop when i equals 5 
    print(i, end=' ')
print("\n")

for i in range(10): 
    if i % 2 == 0:
        continue # Skip the current iteration if i is even 
    print(i, end=' ')