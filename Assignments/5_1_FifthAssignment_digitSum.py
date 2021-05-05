number=int(input())
sum_int=0
while number>0 :
    sum_int += number%10
    number //= 10
print(sum_int)
