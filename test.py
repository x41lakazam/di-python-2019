mylist = ['cho','co','la','t','e']
mylist[1] = 'hello world'

i = 0
while True:
    print(mylist[i])
    if i == 5: # if i is equal to 5
        i = 0  # i takes the value of 0
    i += 1

print(mylist)
