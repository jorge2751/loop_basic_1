for a in range(151):
    print(a)

for b in range(5,1001,5):
    print(b)

for c in range(1,101):
    if c %10 == 0:
        print("Coding Dojo")
    elif c %5 == 0:
        print("Coding")
    else:
        print(c)

sum = 0
for d in range(500000):
    if d %2 == 1:
        sum += d
print(sum)

for e in range(2018,0,-4):
    print(e)

lowNum = 10
highNum = 100
mult = 7

for f in range(lowNum,highNum):
    if f % mult == 0:
        print(f)