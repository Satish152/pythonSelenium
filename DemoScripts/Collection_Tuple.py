tupleEx=("apple","banana","orange") #-->tuple dont support changing data stored in tuple
#it dont delete the value added to tuple,update or changing value also not supported
print(tupleEx)
print(tupleEx[0])
print(tupleEx[1][3])
tuple1=("satish","ramesh","munna")
result=tupleEx.__add__(tuple1) #---able  to concat tuple data only
print(result)