import os

# Make a function that read the content of a file
def print_content(direntry):

    if direntry.is_dir(): # If it's a directory
        return False        # Stop the function

    # Design
    print("#"*10, direntry.name.upper(), "#"*10)

    # Get the name of the file
    filename = direntry.name

    # Open the file and read his content
    file_obj = open(filename, 'r')
    lines = file_obj.readlines()
    file_obj.close()

    # Print all the lines that are not blank
    for line in lines:
        if line.strip():
            print(line, end="")

    # Design
    print("\n")

# List the files
files = os.scandir()

# Loop through them
for direntry in files:
    # Print the content
    try:
        print_content(direntry)
    except:
        print("Error on file:",direntry.name)





