fib1=1
fib2=2
fib=0
print('0,1,1,2')

i=int(input("Enter the iteration:"))

for j in range(1, i):
    fib=fib1+fib2
    print(fib)
    fib1=fib2
    fib2=fib
    
    
    

