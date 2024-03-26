
"""
int
float
complex
"""

a = 10
b = -10
print(f"a :{a}")
print(type(a))          # RTTI - runtime type identification
print(f"b :{b}")
print(type(b))
print("-" * 60)

c = 10.0
print(f"c :{c}")
print(type(c))
d = -10.0
print(f"d :{d}")
print(type(d))
print("-" * 60)

e = +2e3
f = -2e3
print(f"e :{e}")
print(type(e))
print(f"f :{f}")
print(type(f))
print("-" * 60)

g = 3.141j
h = -3.141j
print(f"g :{g}")
print(type(g))
print(f"h :{h}")
print(type(h))
print("-" * 60)

print(max(10, 8, 4, 7, 9, 12, 6))
print(min(10, 8, 4, 7, 9, 12, 6))

x = 2 + 3.5
print(type(x))
print("-" * 60)

x = 2
y = 3.5
z = x + y
print("x = ", type(x))
print("y = ", type(y))
print("z = ", type(z))

print("Conversion".center(60, "-"))
a = 100
print(f"a :{a}")
print(f"{type(a)}\t\t{a}")
print(f"{type(float(a))}\t\t{float(a)}")
print(f"{type(complex(a))}\t\t{complex(a)}")
print(f"{type(bool(a))}\t\t{bool(a)}")

print("Number System".center(60, '-'))
print(11)       # decimal
print(0b11)     # binary    2 ** 1 + 2 ** 0
print(0b101)    # binary    2 ** 2 + 0 + 2 ** 0
print(0o11)     # octal
print(0o101)    # octal
print(0xe)      # hexa
print(0xa)      # hexa

print("Number System Conversion".center(60, "-"))
a = 100
print(bin(a))
print(oct(a))
print(hex(a))

