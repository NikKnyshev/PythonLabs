print('\n3.3')
CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'
cse = CONFIG.strip(',').split(' ')[-1]
print('--'+CONFIG, '--'+cse, sep='\n')