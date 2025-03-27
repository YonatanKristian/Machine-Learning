lst = [5, 1, 3, 2, 10]
print(lst)
lst.sort()
print(lst)
lst.reverse()
print(lst)

vehiclesOne = ['car', 'bicycle', 'motor']
print(vehiclesOne) # outputs: ['car', 'bicycle', 'motor']

vehiclesTwo = vehiclesOne
del vehiclesOne[0] # deletes 'car'
print(vehiclesTwo) # outputs: ['bicycle', 'motor']
print(vehiclesOne)