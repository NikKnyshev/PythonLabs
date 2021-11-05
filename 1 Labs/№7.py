print('\n3.7')
MAC = '1111:2222:3333'
out = MAC.split(':')
print((bin(int(out[0])))[2:],(bin(int(out[1])))[2:],(bin(int(out[2])))[2:],sep=':')