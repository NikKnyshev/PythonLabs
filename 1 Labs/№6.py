print('\n3.6')
ospf_route = 'OSPF 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
keys = ('Protocol','Prefix','AD/Metric','Next-Hop','Last update','Outbound Interface')
ospf_route = ospf_route.replace(',','').replace('[','').replace(']','')
out = ospf_route.split(' ')
out.remove(out[3])  #удаляем слово "via"
dictionary = dict(zip(keys,out))
print(dictionary)
