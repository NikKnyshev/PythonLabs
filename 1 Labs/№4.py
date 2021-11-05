print('\n3.4')
command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'
cm1 = set(command1.split(' ')[-1].split(','))
cm2 = set(command2.split(' ')[-1].split(','))
answ = list(cm1.intersection(cm2))
print('--',answ,sep='')