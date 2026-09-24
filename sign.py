input("XOR sign detection - n ^ m < 0 mens different sign. Press Enter")
print(" 4 ^ 2 =", 4 ^ 2, " same sign positive")
print(" 4 ^ -2 =", 4 ^ -2, " different sign negative")

n = int(input("Enter a number(try 2 or -5)"))
guess = input("Will " + str(n) + " ^ -8 be positive or negative? ")
input("XOR is negative when signs differ. Press Enter")
print(" ", "^ -8 =", n ^ -8, "  your guess:",guess)