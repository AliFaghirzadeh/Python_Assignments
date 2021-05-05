string = input()
char_list=[]
i=0
while i<len(string)-1:
    char_list.append(string[i]+string[i+1])
    i+=2
if len(string)%2==1:
    char_list.append(string[len(string)-1])
print(char_list)
