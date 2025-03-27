buah=["Salak","Mangga","Apel"]
buah.append("Jeruk")
print(buah)

myList = [] # creating an empty list

for i in range(5):
    myList.append(i + 1)

print(myList)
print("\n")
print("insert")
buah = ["durian", "mangga", "apel"]
buah.insert(1,"kiwi")
print (buah)
print("\n\n")
numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)

print("\n\n")
print("menghapus elemen")
num = [5,4,3,2,1]

del num[3]
print(num)
print("\n\n\n")
# step 1
beatles = []
print("Step 1:", beatles)

# step 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# step 3
for i in range(2):
    nama = input("Masukkan anggota baru = ")
    beatles.append(nama)
print("Step 3:", beatles)

# step 4
del beatles[-2:]
print("Step 4:", beatles)

# step 5
beatles.insert(0,"Ringo Starr")
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))