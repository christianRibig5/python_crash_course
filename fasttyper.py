import matplotlib.pyplot as plt
import time as t

print('Program to help you type faster. You will have to type "Programming" as fast as you can five times')

times = []
mistakes = 0

input('press enter before you begin: ')

while len(times) < 5:
    start = t.time()
    word = input("Type the word: ")
    end = t.time()
    time_elapsed = end - start
    times.append(time_elapsed)

    if word.lower() != 'programming':
        mistakes+=1
print('You made '+str(mistakes)+' mistakes and the time diferences are',times)
print("lets visualize your perfomance in using graph plot")
t.sleep(5)

x = [1,2,3,4,5]
y = times
legend =['1','2','3','4','5']
plt.xticks(x,legend)
plt.plot(x,y)
plt.ylabel("Time in seconds")
plt.title("Typing Speed Evaluation")
plt.xlabel('Attempts')
plt.show()

