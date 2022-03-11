a, b, c, x = map(int, input().split())
# print(a,b,c,d)
if x <= a:
    print(1)
elif a < x <= b:
    print(c/(b-a))
else:
    print(0)