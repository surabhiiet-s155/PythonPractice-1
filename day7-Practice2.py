with open("practice.txt", "r") as f:
    data = f.read()

if "learning" in data:
    print("Word Found")
else:
    print("Word Not Found")
