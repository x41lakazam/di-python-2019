# readfile.py

# Read a file
# file_obj = open("myfile.txt", 'r')
# lines = file_obj.readlines()
# file_obj.close()

# # Write something to a file
# file_obj = open("myfile.txt", 'w')
# file_obj.write("Hello again from readfile.py\n")
# file_obj.close()

def add_line(filename, msg):
    file = open(filename, 'a')
    file.write(msg+"\n")
    file.close()
    print("Added <{}> to {}".format(msg, filename))

def add_upperline(filename, message):
    f = open(filename, 'a')
    f.write(message.upper()+'\n')
    f.close()

def write_in_files(list_of_files, msg):
    for name_of_file in list_of_files:
        add_line(name_of_file, msg)

files = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt', 'file5.txt']
write_in_files(files, "Hello World :)")