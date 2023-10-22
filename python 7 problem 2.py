unique_names = set()
while True:
    name = input("Enter a name (or press Enter to finish): ")
    if name == "":
        break

    if name in unique_names:
        print("Existing name")
    else:
        print("New name")
        unique_names.add(name)
print("\nList of input names:")
for name in unique_names:
    print(name)