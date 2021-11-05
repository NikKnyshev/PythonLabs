print('\n3.8')
IP = '192.168.3.1'
a = IP.split('.')
a = ['{:<10}'.format(i) for i in a]
b = ['{:<010d}'.format(int(bin(int(i))[2:])) for i in a]
print(' '.join(a))
print(' '.join(b))