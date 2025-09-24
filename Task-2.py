with open('output.txt', 'r+') as file:
    writing_file = file.write(input("Enter something to write in the file: ") + "\n")
    print("Data successfully written to output.txt")

with open('output.txt', 'a') as file:
    appending_file = file.write(input("Enter additional text to append: ") + "\n")
    print("Data successfully appended.")

with open('output.txt', 'r') as file:
    reading_file = file.read()
    print("Final content of output.txt: \n" + reading_file)
