for i in range(5):
    print(i)
else:
    print("masuk else")
    print("\n\n\n")

    import time

for i in range(5):
    print(i," zoltark")
    time.sleep(1)
    print("\n\n\n")

    print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")