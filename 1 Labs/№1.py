print('3.1')
NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
print('--'+NAT, '--' + NAT.replace('Fast', 'Gigabit'), sep='\n')
