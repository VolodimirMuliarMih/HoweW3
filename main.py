#1 step
a1 = 5
a2 = 5
a3 = 5
#2 step
print(id(a1))
print(id(a2))
print(id(a3))
#3 step
a1=[a1,]
a2=[a2,]
a3=[a3,]
#4 step
print(id(a1))
print(id(a2))
print(id(a3))
#5 step
b1 = [5,]
b2 = [5,]
#6 step
print(id(b1))
print(id(b2))
#7 steo
b1= b1.pop()
b2= b2.pop()
#8 step
print(id(b1))
print(id(b2))


