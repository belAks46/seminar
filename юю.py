
f = open('input.txt' , 'w')
a = input()
f.write(a + '\n')
f.write(input())
f.close()
v = open('input.txt', 'r')
b = v.readlines()
x = list(map(int, b[0].split()))
y = x[0]
g = x[1]
k = x[2]
if b[1] =='+':
    q = y+g+k
    h = open('output.txt', 'w')
    print(q)
    h.write(str(q))