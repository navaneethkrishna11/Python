#DIFFERENT METHODS USED FOR SWAPPING TWO NUMBERS
a=4
b=3
a,b=b,a
print(a,b)

c=7
f=2
c=c^f
f=c^f
c=c^f
print(c,f)

r=9
t=2
r=r+t
t=r-t
r=r-t
print(r,t)
###----------------------------------------###
#PALINDROME OF A NUMBER
pal=121
rev=0
a=pal
while a!=0:
    rev=(rev*10)+a%10
    a//=10

print(rev)
if rev == pal:
    print("palindrome")
else:
    print("Not")

##-------------------------------------##
#ROTATING AN ARRAY
l=[1,2,3,4,5,6]
print(l[2:]+l[:2])
num=2

num=num%len(l)
print(l[num:]+l[:num])
#-----------------------------------------#
#SUM OF FIBINACCI SERIES
print("Fibbinacci sum")
a=0
b=1
sum=a+b
for i in range(2,9):
     c=a+b
     sum =sum+c
     a=b
     b=c
print(sum)
######

def fib(n):
    if n<=0:
        return n
    else:
        return fib[n-1]+fib[n-2]


print('sum')
fib(5)
