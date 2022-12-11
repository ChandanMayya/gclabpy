lst=[]
n=int(input("Enter max: "))
for i in range(0,n):
    ele = int(input("enter element:"))
    lst.append(ele)
lst2=sorted(lst)
print(lst2)
e=int(input("Enter a element to insert: "))
for i in range(len(lst2)):
    if lst2[i]>e:
        lst2.insert(i,e)
        break
    elif lst2[len(lst2)-1] < e:
        lst2.insert(len(lst2),e)
        break
print(lst2)


    




