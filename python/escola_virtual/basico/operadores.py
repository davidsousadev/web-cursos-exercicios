a = 5
b = 10
c = 15

print("a == b e b > c : ", a == b and b > c)
print("a < b ou b > c : ", a < b or b > c)
print('não a == b : ', not a == b)

if a == b:
    print("a == b")
else:
    if a >= b:
        print("a >= b")
    else:
        print("a <= b")


if a == b:
    print("a == b")
elif a >= b:
    print("a >= b")
else:
    print("a <= b")