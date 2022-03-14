print('assignment to calculate BMI is body mass index in meter')

weight = float(input('Type body weight:'))
height = float(input('Type body height:'))

bmi = weight/(height**2)
print('bmi =',str(round(bmi,2))+'kg/m')

if (bmi<=18.5):
    classification = 'You are underweight'
    
elif(bmi > 18.8 and bmi <= 24.9):
    classification ='You have Normal weight'
    
elif(bmi > 24.9 and bmi <= 29.9):
    classification ='You are overerweight'
    
else:
    classification ='You are obese'
    
print(classification)

print('while loop')

people =[]
while len(people) < 5:
    person = input('Type name of person:')
    people.append(person)
print(people)

print('program to implement a gues game')


    
