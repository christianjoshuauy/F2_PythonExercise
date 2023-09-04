x = int(input('x:')); y = int(input('y:')); z = int(input('z:'))
if x > y and x > z:
    max = x
elif y > z:
    max = y
else:
    max = z

print(max)

