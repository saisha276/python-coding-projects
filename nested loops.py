string = input("please enter a word: ")
char = input("please enter a charrecter: ")
i = 0
count = 0

while (i < len(string)):
    if[string[i] == char]:
        count = count + i
    i = i + 1 
    
print(" The total number of times", char, "has occures = ", count)