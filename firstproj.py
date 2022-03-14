print('My first python program')
print(2+3)

age = 35
print('i am ',age,' years old')

age = 32

print('i am ',age,' years old')

print('the average of two numbers 4 and 8')
print('average is', (4+8)/2)

number1=4
number2 =8
print('the average of two numbers',number1,'and',number2)
print('average is', (number1+number2)/2)

firstname='christian'
lastname='onyeukwu'
print('my eamil is',firstname+'.'+lastname+'@gmail.com')

number1 = float(input('please enter first number:'))
number2 = float(input('please enter second number:'))
print('average is', (number1+number2)/2)

print('program to convert kilometer to miles')
km = float(input('please enter kilometer:'))
print(km,'km =',round(km/1.609344,4),'miles')

firstname = input('firstname:')
middlename = input('middlename:')
lastname = input('lastname:')
print('my initials are', firstname[0]+'.'+middlename[0]+'.'+lastname[0])
lot = '037-00901-00027'
print('country code:',lot[:3])
print('product code:',lot[4:9])
print('batch number:',lot[10:])
import math
print('5 factorial is',math.factorial(5))
print('Program to calculate area of circle')
radius = float(input('please enter radius:'))
print('Area =:',round(math.pi*radius**2,2))
print('Circumfrence =:',round(2*math.pi*radius, 2))
print('program to user for their birthday in format "dd-mm-yyyy"')
birthday = input('what is your birthday:')
monthsofYear = ('january','february','march','april','may','june','july','august','september','october','novermber','december')
print('your are born in:', monthsofYear[(int(birthday[3:5]))-1])
familyMembers =['Nduka','Johnken','emeka']
name = input("what's your name:")
familyMembers.append(name)
print('updated family list',familyMembers)
print('Program to implement a dictionary of person detail')
person ={'name':'Christian Onyeukwu','age':35, 'address':'Rue Forest J1k1R2','phone':'+18199196872'}
key=input('what do you want to know about person:').lower()
answer = person.get(key,'The information you requested is not available')
print('The', key,'is',answer)

num1 = float(input('Type the first number:'))
num2 = float(input('Type the second number:'))

if (num1 > num2):
    print(num1,'is greater than', num2)
elif(num1==num2):
    print(num1,'is equal to',num2)
else:
    print(num1,'is less than',num2)
    
print('program to compare your age with another user')
myAge = 35
userAge = float(input('Type your age:'))
if (userAge > myAge):
    print('You are older than me')
elif(userAge == myAge):
    print('We have same age')
else:
    print('You are younger than me')
    

      
