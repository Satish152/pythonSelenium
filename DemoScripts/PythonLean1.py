print("Hello World")

a=10
c=1
print(a+c)

if a<c:
    print("working")

if(a>c):  #--->if,ifelse,else
    print("wrong")
elif(a<c):
    print("correct")
else:
    print("equal")

while c<a:  #---while
    print(c);
    c=c+1;

list1=[1,2,3]  #--->list
for val in list1: #for to iterate list
    print(val)

print("done")

#this is a function
def sum(a,c):  #---->def function
    print(a+c,"this is function")

sum(10,20)

def returnMethod(a,c):
    return print(a+c,"this is return method")

d=returnMethod(50,80)

