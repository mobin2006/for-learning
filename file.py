
# how to read,write a file whit a python in the terminal

# for read a file in terminal
with open('python3.txt') as file:
    content = file.read()
print(content)

# for write and add a text used (w)
with open('python3.txt' , 'w') as file:
    content = file.write('i am in the class computer')

# for read a file in terminal
with open('python3.txt') as file:
    content = file.read()
print(content)

# in the end for see all a file in terminal 
with open('python3.txt' , 'a') as file:
    content = file.write('shayan alvansaz')
print(content)
