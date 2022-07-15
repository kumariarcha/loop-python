# i=0
# while i<5:
#     j=0
#     while j<5:
#         if j==0 or j==4 or i==0 or i==4:
#             print("A",end=" ")
#         elif i==j==2:
#             print("A",end=" ")
#         else:
#             print("C  ",end=" ")
#         j=j+1
#     print()
#     i=i+1


i=0
while i<5:
    j=0
    while j<5:
        if j==0 or j==4 or i==0 or i==4:
            print("A",end=" ")
        elif i==j==2:
            print("B",end=" ")
        else:
            print("C",end=" ")
        j=j+1
    print()
    i=i+1