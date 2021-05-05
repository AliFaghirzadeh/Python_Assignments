#Quiz2--> question2
x=float(input())
n=int(input())

i=1
d=1/x
while ( i <= n ) :
    if (i%2==0):
        d = d+( x**(-1*(i+1))/(i+1))
    else:  
        d = d- ( x**(-1*(i+1))/(i+1))
    i+=1
print(d)
    
