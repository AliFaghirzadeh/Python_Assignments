string1 = input()
string2 = input()
list1 = string1.split('+')
list2 = string2.split('+')
concatenated_list = []


def sort_str(string):
    return ''.join(sorted(string))


def print_result(list0):
    for i in range(len(list0)):
        st = list0[i]
        st = st.replace(' ', '')
        if i != len(list0) - 1:
            print(st + " + ", end="")
        else:
            print(st)


def fill_list():
    for i in range(len(list1)):
        for j in range(len(list2)):
            concatenated_list.append(sort_str(list1[i] + list2[j]))


fill_list()
print_result(concatenated_list)