n=int(input())
fib_sequence_string="1 , 1";
fib_first=1;  
fib_second=1;
turn=0

while turn < n-2:
    turn+=1
    fib_third=fib_first+fib_second
    fib_sequence_string += " , " + str(fib_third)
    fib_first=fib_second
    fib_second=fib_third

print(fib_sequence_string)
    
