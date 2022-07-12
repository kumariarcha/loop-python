num=int(input("enter the num:-"))
count=0
i=2 
while i<=num:
    if num%i==0:
        count=count+2
    i=i+1
if count==2:
    print(num,"is prime num")
else:
    print(num,"is not prime num")


    

        
