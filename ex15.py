from sys import argv

# passes a filename from a terminal argument and stores it as the filename variable
script, filename = argv

# calls the open() function to open a file and store the contents of a file into a variable
txt = open(filename)

# prints the name of file
print(f"Here's your file {filename}:")
# calls the read() function to return the contents of file stored as a variable
print(txt.read())

txt.close()
