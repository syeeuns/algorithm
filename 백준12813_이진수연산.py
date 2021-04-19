import sys
read = sys.stdin.readline

n = int('0b' + read().rstrip(), 2)
m = int('0b' + read().rstrip(), 2)
print(bin(n & m)[2:].zfill(100000))
print(bin(n | m)[2:].zfill(100000))
print(bin(n ^ m)[2:].zfill(100000))

n = list(bin(n)[2:])
for i in range(len(n)):
    if n[i] == '0':
        n[i] = '1'
        continue
    elif n[i] == '1':
        n[i] = '0'
        continue
print('1' * (100000 - len(n)) + ''.join(n))

m= list(bin(m)[2:])
for i in range(len(m)):
    if m[i] == '0':
        m[i] = '1'
        continue
    elif m[i] == '1':
        m[i] = '0'
        continue
print('1' * (100000 - len(m)) + ''.join(m))