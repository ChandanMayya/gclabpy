
lst=[]
n=int(input("Enter max: "))
for i in range(0,n):
    ele = int(input("enter element:"))
    lst.append(ele)
lst2=sorted(lst)
e=int(input("Enter a element to insert: "))
for i in range(len(lst2)):
    if ele<lst2[i]:
        lst2.insert(i+1,ele)
print(lst2)


    


