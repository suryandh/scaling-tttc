import math
num=int(input("Enter the number:"))


def fin(n):
    
    i=True
    c=0
    while i:
        
     n=n/10
     c=c+1
     if (int(n)==0):
         i=False
    
    return c
nc=nc1=num
p=fin(num)
num1=0
for t in range(1,p+1):
#  d=num%10
#  t=(int(num/10))%10
#  h=(int(num/100))%10
    d=nc%10
    #print(d)
    nc=int(nc/10)
    num1=num1+pow(d,p)
    
#print(d*math.pi,t,h)
#num1=pow(d,p)+pow(t,p)+pow(h,p)

if(nc1==num1):
    print("Number", num1,"is a", p,"digit Arm number")
else:
    print(num1,"is not Armstrong number")

