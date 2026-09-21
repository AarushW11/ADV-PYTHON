filename = input("Enter the file name: ")
word = input("Enter the word to search: ")

count = 0

try:
    with open(filename, "r") as file:
        for line in file:
            if word.lower() in line.lower():
                count += 1

    print("Number of lines containing", word, "=", count)

except FileNotFoundError:
    print("File not found.")
