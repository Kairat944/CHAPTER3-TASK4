a = input("Ввeдите число через пробел:").split(' ')
for i in range(len(a)):
    a[i] = int(a[i])
a.sort()
print(a)

for i in range(1,max(a)):
    if i > 0 and i not in a:
        print(i)