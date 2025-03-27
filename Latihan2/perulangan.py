i = 1

while i<10:
    print(i**2)
    i = i+2

print("\n\n\n")
oddNumbers = 0
evenNumbers = 0

# read the first number
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution
while number != 0:
    # check if the number is odd
    if number % 2 == 1:
        # increase the oddNumbers counter
        oddNumbers += 1
    else:
        # increase the evenNumbers counter
        evenNumbers += 1
    # read the next number
    number = int(input("Enter a number or type 0 to stop: "))

# print results
print("Odd numbers count:", oddNumbers)
print("Even numbers count:", evenNumbers)

print("\n\n\n")

secretNum = 98

guessNum = 0

while guessNum != secretNum:
    guessNum = int(input("Input angka rahasia untuk berhenti : "))
    if guessNum != secretNum:
        print("Perulangan akan terus lanjut...")

print("Well done, Congrats...")