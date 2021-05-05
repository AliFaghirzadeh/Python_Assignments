str1=input()
str2=input()
commonLetters=""
for char in str1:
    if ( char in str2 ) and ( char not in commonLetters ):
        commonLetters+=char
print(commonLetters)
