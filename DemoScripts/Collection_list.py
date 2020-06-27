list1=["satish","ramesh","munna"]
print(list1)
print(len(list1))
list1.insert(1,"test")
print(list1)
list1.append("python")
print(list1)
list1.pop()#-->if index not mentioned,it will delete  last element in list
print(list1)
list1[1]="testing"#--->can change /update value directly
print(list1)

list2=["apple","jam",list1]
print(list2)
for val in list2:
    print(val);
    print(type(val))
    if type(val)==list:
        for test in val:
            print(test)

