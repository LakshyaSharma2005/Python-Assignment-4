try:
    with open('sample.txt', 'r+') as file:
        for line in file:
            print(line, end='')
except FileNotFoundError:
    print("The file 'sample.txt' was not found")
finally: 
    print("Continue to code")
    