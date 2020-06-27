class MyClass:
    name="Satish"

    def sum(self,a,c):
        print(a+c)

clsObj=MyClass()  #--->Creating obj to class
print(clsObj.name)   #--->Calling variable in the class
clsObj.sum(55,4) #---->calling method


class Test:
    test="john"
    def __init__(self,a):   #--->this init is like constructor
        self.test=a
        print("init  "+a)

y=Test("satish")
del y  #-->delete the class obh
