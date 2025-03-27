a = 5
b = 6

if a==b:
    print("oke")
    print("berhasil")
else:
    print("Gagal")

    print("\n\n")
    bil = int(input("Masukan bilangan bulat: "))

if(bil%2 == 0):
    print("genap")
else:
    print("ganjil")
    print("\n\n")


    print("Masukan nilai koordinat")
x = int(input("Nilai x: "))
y = int(input("Nilai y: "))

if x>0 and y>0:
    print("Koordinat ("+ str(x) + ","+ str(y) +") berada pada Kuadran I" )
elif x<0 and y>0:
    print("Koordinat ("+ str(x) + ","+ str(y) +") berada pada Kuadran II" )    
elif x<0 and y<0:
    print("Koordinat ("+ str(x) + ","+ str(y) +") berada pada Kuadran III" )
elif x>0 and y<0:
    print("Koordinat ("+ str(x) + ","+ str(y) +") berada pada Kuadran IV" )
else:
    pass
print("\n\n")
print("mencari bilangan terbesar/terkecil")

num1 = int(input("First Number : "))
num2 = int(input("Second Number : "))
num3 = int(input("Third Number : "))

#set number1 sebagai yang terbesar
largestNum = num1

#deteksi apakah num2 > num1
if num2 > largestNum:
    largestNum = num2

#deteksi apakah num3 > num2
if num3 > largestNum:
    largestNum = num3

print("The largest number is: ", largestNum)