lst = [100,200,300,400,500]
print(lst[-1])
print(lst[-2])
print(lst[-5])

print("\n")
print(lst[4])
print(lst[3])
print(lst[0])

print("\n")
print("searching")
lst=[4,1,6,9,10,8]

print(lst[0:3])
print(lst[1:3])

print(lst[-3:])
print(lst[:-3])

print(lst[:])

print("\n")
print("sort")
myList = [8, 10, 6, 2, 4] # list to sort
swapped = True # it's a little fake - we need it to enter the while loop

while swapped:
    swapped = False # no swaps so far
    for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]:
            swapped = True # swap occured!
            myList[i], myList[i + 1] = myList[i + 1], myList[i]

print(myList)