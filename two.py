print(QUESTION-1)
tuple1=('notebook',1234,4.3,['shirt','pant'])
print(tuple1)
print(len(tuple1))
print("\n")
print(QUESTION-2)
print("Enter the elements of first tuple")
a=input("enter first element")
b=input("enter second elememt")
c=input("enter third element")
d=input("enter fourth value")
tuple1=(a,b,c,d)
print(tuple1)
print("Enter the elements of second tuple")
w=input("enter first element")
x=input("enter second elememt")
y=input("enter third element")
z=input("enter fourth value")
tuple2=(w,x,y,z)
print(tuple2)
print('Maximum element in tuples 1,2: '+
      str(max(tuple1))+ ','+
      str(max(tuple2)))
print('Minimum element in tuples 1,2: '+
      str(min(tuple1))+ ','+
      str(min(tuple2)))
print("\n")
print(QUESTION-3)
print("Enter the elements of tuple")
a=int(input("enter first elememt"))
b=int(input("enter second elememt"))
c=int(input("enter third element"))
d=int(input("enter fourth value"))
tp=(a,b,c,d)
multiply=(tp[0]*tp[1]*tp[2]*tp[3])
print(multiply)
print("\n")
print(QUESTION-4)
setA=set(['gauri','riya'])
setB=set(['riya','meenal'])
setC=setA-setB
print(setC)
if(cmp(setA,setB)!=0):
    print("not same")
else:
    print("same")
print("\n")
print(QUESTION-5)



