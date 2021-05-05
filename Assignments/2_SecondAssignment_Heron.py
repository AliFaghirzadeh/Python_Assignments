a=eval(input())
b=eval(input())
c=eval(input())
p=(a+b+c)/2
s=((p)*(p-a)*(p-b)*(p-c))**(0.5)
# print(round(s,3)) or
print(f"{s:.3f}")
