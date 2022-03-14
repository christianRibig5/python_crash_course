f = open('test.txt','w')
f.write('This the updated text')

f= open('test.txt')
print(f.read())

f = open('test.txt','a')
f.write('\nThis is additional document update')
f= open('test.txt')
print(f.read())

f = open('/Users/Riibig5Techy/desktop/mytest.txt','x')