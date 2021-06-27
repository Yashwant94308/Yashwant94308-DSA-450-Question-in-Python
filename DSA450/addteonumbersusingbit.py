def add(a,b):
            if b == 0:
                return a
            else:
                return add(a^b, (a&b)<<1)

print(add(3,4))