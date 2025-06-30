print("Name: Ishant Yadav")
print("USN: 1AY24AI047")
print("Section: o")
rows = 5
for i in range(rows):
    for j in range(rows):
        if (i + j) % 2 == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
