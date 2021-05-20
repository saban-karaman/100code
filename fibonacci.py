x = []
for i in range(1, 100):
    if x == []:
        x.append(i)
    elif len(x) < 2:
        x.append(i)
    elif i == x[len(x)-1] + x[len(x)-2]:
        x.append(i)
print(x)