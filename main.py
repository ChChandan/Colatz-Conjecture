import matplotlib.pyplot as plt

x=[]
y=[]

#userinput=int(input("Enter the number you want to find the hailstone numbers:- "))
userinput=7
hailstoneno=0
count=0
if(userinput%2==0):
    hailstoneno=userinput/2
else:
    hailstoneno=(userinput*3)+1

while hailstoneno>4:
    if(hailstoneno%2==0):
        hailstoneno=hailstoneno/2
        x.append(hailstoneno)
        count=count+1
        y.append(count)
    else:
        hailstoneno=(hailstoneno*3)+1
        x.append(hailstoneno)
        count=count+1
        y.append(count)
count=count+1
y.append(count)
count=count+1
y.append(count)
x.append(2.0)
x.append(1.0)
plt.plot(y, x, color='green', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=12)
plt.title("Colatz Conjecture")
plt.ylabel('The hailstone numbers')
plt.xlabel('The count of iteration')
plt.plot(y, x, label = "line 1")
plt.show()



   


    


