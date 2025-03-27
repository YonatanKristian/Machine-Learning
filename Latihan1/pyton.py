print("Hello World!@#!#!$")
print("test\n\n\n")
print()

print("Saya sudah sarapan tadi pagi\n dan nanti siang makan lagi")
print("Saya sudah sarapan tadi pagi\t dan nanti siang makan lagi\n\n\n")


print("    *    "*2)
print("   * *   "*2)
print("  *   *  "*2)
print(" *     * "*2)
print("***   ***"*2)
print("  *   *  "*2)
print("  *   *  "*2)
print("  *****  "*2)
print("\n\n\n")

print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****\n"*2)
print("\n\n\n")


print("2"*2)
print(2*2)

print(type("2"))
print(type(2))
print(5, "mempunyai tipe", type(5))
print(.5, "mempunyai tipe", type(.5))
print("\n\n\n")

print("tipe boolean")
print(True)
print(False)

print(4>2)
print(3>4)
print("\n\n\n")

print("operator aritmatika")
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3.)
print(2. ** 3)
print("\n")
print(10 / 3)
print(10 // 3)

print(6 / 3.)
print(6 // 3.)

print(-4 + 4)
print(-4. + 8)
print("\n")
print(9 % 6 % 2)
print(9 % 6)
print(3 % 2)

print(2 ** 2 ** 3)
print(2 ** 2)
print(2 ** 8)
print("\n\n\n")

print("latihan variabel")

Darjo = 3
Darno = 5
Waginem = 6

print(f"Darjo: {Darjo}, Darno: {Darno}, Waginem: {Waginem}")


totalApel = Darjo + Darno + Waginem
print(f"Total apel: {totalApel}")


apelTambahan = 4
apelHilang = 2


totalSetelahTambahan = totalApel + apelTambahan
totalSetelahKehilangan = totalSetelahTambahan - apelHilang


print(f"Total setelah tambahan: {totalSetelahTambahan}")
print(f"Total setelah kehilangan: {totalSetelahKehilangan}")
print("\n\n")
kilometer = 12.25
mil = 7.38

miles_to_kilometers = mil * 1.61
kilometers_to_miles = kilometer / 1.61

print(mil, "1 mil adalah", round(miles_to_kilometers, 2), "kilometer")
print(kilometer, "1 kilometer adalah", round(kilometers_to_miles, 2), "mil")
print("\n\n\n")
print("replikasi")
print("+" + 10*"-" + "+")
print(("|" + 10*" " + "|\n") * 5, end="")
print("+" + 10*"-" + "+")