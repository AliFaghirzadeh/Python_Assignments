x1=int(input()) ; y1=int(input())
x2=int(input()) ; y2=int(input())
x3=int(input()) ; y3=int(input())
x4=int(input()) ; y4=int(input())
side1=(x2-x1)**2+(y2-y1)**2
side1=side1**(0.5)
side2=(x3-x2)**2+(y3-y2)**2
side2=side2**(0.5)
side3=(x4-x3)**2+(y4-y3)**2
side3=side3**(0.5)
side4=(x1-x4)**2+(y1-y4)**2
side4=side4**(0.5)
if side1==side2==side3==side4:  # if it is a lozi
    print("lozi")
elif (side1==side3) and (side2==side4):  # if it is a motevazi azla
    print("motevazi azla")
elif ( (side1==side4) and (side2==side3)) or ( (side1==side2) and (side3==side4)) : # if it is a kite
    print("kite")
else:
    print("others")
