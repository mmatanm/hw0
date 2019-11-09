# Q1
if __name__ == "__main__":
    print("Hello World")


# Q2
def bool_or_not(b: bool):
    if b is True:
        return 1
    elif b is False:
        return -1


# Q3
def power(x, y):
    return x ** y


# Q4
x = 1
y = 2
z = (x, y)
y, x = z
# print("Y is", y, "X is ", x)

# Q5
listm = []
listm.append('a')
listm.append('b')
listm.reverse()
# print(list)

# Q6
listm = list(range(2, 24))
# print(listm)

# Q7
num_list = list(range(1, 11))
#print(num_list[-1:2:-2])


# Q8
import functools
def funcsum(mlist: list):
    return functools.reduce(lambda x,y:x+y,mlist)


# Q9
f=open("my_file.txt","w")
f.write("I know how to write")

# Q10
def perfectnum(number):
    sum=functools.reduce(lambda x,y:x+y,list(filter(lambda x:number%x==0,range(1,number))))
    if(sum==number):
        return True
    return False


# PART TWO

# Q1+Q2
class MyClass(object):
    def __init__(self):
        print("this is my class")

# Q3 +Q4
class Point(object):
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def show(self):
        print("my location is {x},{y}".format(x=self.x, y=self.y))

# Q5
import random
def randnum(number):
    r = random.randint(1,1000)
    if(r>number):
        return 0
    return r

# Q6
def sublist(mlist:list,num):
    return [random.choice(mlist) for _ in range(num)]

# Q7
import re
def sumstr(num:str):
    sum=functools.reduce(lambda a,b:a+b,[int(x) for x in re.findall(r'\d+',num)])
    if num[0]=='-':
        sum*=-1
    return sum


import unittest
class testsumstr(unittest.TestCase):
    def testnegative(self):
        self.assertEqual(sumstr("-23.13"),-36)
    def testpositive(self):
        self.assertEqual(sumstr("13.23"), 36)

unittest.main()