print("right angle triangle using star pattern **")
rows = int(input("enter the number of rows: "))
for i in range(rows) :
    for j in range(i+1):
        print("*", end = "")
    print()