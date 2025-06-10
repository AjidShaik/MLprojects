# Sample values
a = 10
b = 3
c = [1, 2, 3]
d = a

print("🔢 Arithmetic Operators")
print("Addition:", a + b)         # 13
print("Subtraction:", a - b)      # 7
print("Multiplication:", a * b)   # 30
print("Division:", a / b)         # 3.333...
print("Floor Division:", a // b)  # 3
print("Modulus:", a % b)          # 1
print("Exponentiation:", a ** b)  # 1000

print("\n📏 Comparison Operators")
print("Equal:", a == b)           # False
print("Not Equal:", a != b)       # True
print("Greater Than:", a > b)     # True
print("Less Than:", a < b)        # False
print("Greater or Equal:", a >= b) # True
print("Less or Equal:", a <= b)   # False

print("\n🧠 Logical Operators")
print("Logical AND:", a > 5 and b < 5) # True
print("Logical OR:", a < 5 or b < 5)   # True
print("Logical NOT:", not(a < 5))     # True

print("\n📝 Assignment Operators")
x = 5
x += 3
print("Add and assign (+=):", x)     # 8
x -= 2
print("Subtract and assign (-=):", x) # 6
x *= 2
print("Multiply and assign (*=):", x) # 12
x /= 3
print("Divide and assign (/=):", x)   # 4.0
x //= 2
print("Floor divide and assign (//=):", x) # 2.0
x %= 2
print("Modulus and assign (%=):", x)  # 0.0
x = 3
x **= 2
print("Exponent and assign (**=):", x) # 9

print("\n💡 Bitwise Operators")
print("Bitwise AND:", a & b)        # 2
print("Bitwise OR:", a | b)         # 11
print("Bitwise XOR:", a ^ b)        # 9
print("Bitwise NOT:", ~a)           # -11
print("Left Shift:", a << 1)        # 20
print("Right Shift:", a >> 1)       # 5

print("\n🔎 Membership Operators")
print("Is 2 in list:", 2 in c)      # True
print("Is 5 not in list:", 5 not in c) # True

print("\n🆔 Identity Operators")
print("Is a same as d:", a is d)    # True
print("Is a not same as b:", a is not b) # True
