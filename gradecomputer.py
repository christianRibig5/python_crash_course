data_valid = False
while data_valid==False:
    grade1= input('Type grade1:')
    try:
        grade1= float(grade1)
    except:
        print('invalid grade input. Grade must be a valid decimal real number')
        continue
    if grade1 < 0 or grade1 > 10:
        print('grade should be betwen 0 and 10')
        continue
    else:
        data_valid = True

data_valid = False
while data_valid == False:
    grade2= input('Type grade2:')
    try:
        grade2= float(grade2)
    except:
        print('invalid grade input. Grade must be a valid decimal real number')
        continue
    if grade2 < 0 or grade2 > 10:
        print('grade should be betwen 0 and 10')
        continue
    else:
        data_valid = True

data_valid = False
while data_valid == False:
    total_classes = input('Type total number of classes:')
    try:
        total_classes = int(total_classes)
    except:
        print('Total classes must be a valid integer')
        continue
    if total_classes <= 0:
        print('total class atendance must be greater than zero')
        continue
    else:
        data_valid = True

data_valid = False
while data_valid == False:
    absences = input('Type number of absence from classes:')
    try:
        absences = int(absences)
    except:
        print('Total absentism from class must be a valid integer')
        continue
    if absences < 0 or absences > total_classes:
        print('absentism to class should be betwen 0 and ',total_classes,'which is the total number of classes')
        continue
    else:
        data_valid = True


average_grade = (grade1+grade2)/2
attendance = (total_classes-absences)/total_classes

print('Average grade', average_grade)
print('Attendance',str(round(attendance*100,2))+'%' )

if (average_grade >= 6 and attendance >= 0.8):
        print('The student has been approved')
elif(average_grade < 6 and attendance < 0.8):
    print('The student faild due average garde lower than 6 and attendance lower than 80%')
elif(attendance < 0.8):
    print('The student failed due to attendance rate is lower than 80%')
else:
    print('The student failed due to average grade is lower than 6')
