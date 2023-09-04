a=int(input("How many numbers do you want in your list"))
average=0
sum=0
list=[]
c=0
for i in range(0,a,1):
    b=int(input("Enter a number to add to your list"))
    list.append(b)

for c in list:
    sum=sum+c

average=sum/a
print("Your list is", list)
print("The average of your list is", average)
print("The sum of your list is", sum)
