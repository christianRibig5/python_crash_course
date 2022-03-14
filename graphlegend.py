import matplotlib.pyplot as plt


x =[1,2,3,4]
y = [1500, 2000, 3000,3500]
legend = ['January','February', 'March','April']
plt.xticks(x,legend)
plt.plot(x,y)
plt.show()