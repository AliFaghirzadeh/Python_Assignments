string = input()
sub_string_list = []

for i in range(len(string)):
    for j in range(i+1 , len(string) + 1):
        sub_string_list.append(string[i:j])

def comparator_logic(element):
    return len(element)


# sub_string_list.sort(key=comparator_logic)
for i in sub_string_list:
    print(i)
