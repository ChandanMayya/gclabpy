lst=[]
n=int(input("Enter max: "))
for i in range(0,n):
    ele = int(input("enter element:"))
    lst.append(ele)
print(lst)
se=int(input("Enter a search element: "))
for i in lst:
    if i==se:
        print("ele found")
        flag=-1
        break
    else:
        flag=0
if flag==0:
    print("ele not found")
    
