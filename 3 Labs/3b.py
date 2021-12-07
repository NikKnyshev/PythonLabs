input_file = open("CAM_table.txt", 'r')

input_file_data = input_file.readlines()
input_file_data_processed = []

chosen_VLAN = int(input("Enter VLAN number: "))

for line in input_file_data:
    if '.' in line and int((line.split())[0]) == chosen_VLAN:
        input_file_data_processed.append(line)

for line in input_file_data_processed:
    print(line.rstrip())