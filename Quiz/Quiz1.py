# Quiz 1
# cordinates of firstShape
x1=int(input()) ; y1=int(input())
x2=int(input()) ; y2=int(input())
# cordinates of the point
a1=int(input()) ; b1=int(input())
# setting the minimum of y
if y1 < y2 :
    y_min=y1
    y_max=y2
else:
    y_min=y2
    y_max=y1
# setting the minimum of x
if x1<x2 :
    x_min=x1
    x_max=x2
else:
    x_min=x2
    x_max=x1
# main condition : if the point is in rectangle
if (x_min<a1<x_max) and (y_min<b1<y_max):
    print("yes")
else :
    print("no")
