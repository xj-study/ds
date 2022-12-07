import os


print(os.getcwd())
print(os.listdir())

# os.mkdir('test')
# os.rmdir('test')

p6 = os.path.abspath('python-v0.1/demo7.py')
print(p6)
file = open(p6,'r')
print(file.read())

lstfile = os.walk(os.getcwd())
print(lstfile)