print('program to print a randomly selected name in list of 8 names')
name = input('Type a user name: ')
names=[]
while len(names) < 8:
    names.append(name)
    name = input('Type a user name: ')
print(names)
import random
rand_index = random.randrange(len(names))
print('randomly selected name :',names[rand_index] )