num = eval(input("enter number"))
myList=[]
arr = []
for i in range(1,num+1):
    for j in range(1,i+1):
        #print(j)
        arr.append(j*i)
    myList.append(arr)
    #arr.clear()
    arr = []
    #print(i)

print(myList)