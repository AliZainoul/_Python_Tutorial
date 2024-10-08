N = 25
print(list(map(lambda el : f"{el} is even" if el%2==0 else f"{el} is odd", [_ for _ in range (N)])))