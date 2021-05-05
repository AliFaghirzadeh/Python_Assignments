file = open("infoDB.txt", 'w')

boolean = True
detail_list = ["Name : ", "Family : ", "Age : ", "Gender : ", "BirthDate : ", "Nationality : ", "National ID : "]
input_list = []
info_list = []
while boolean:
    for i in range(len(detail_list)):
        info = detail_list[i] + input(detail_list[i])
        file.write(info + "\n")
    file.write("-------------------------------------------------------\n")
    req = input("register anyone else ? Y/N")
    if req == 'n' or req == 'N':
        boolean = False
file.close()
