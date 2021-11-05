print('\n3.9')
num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']
a = num_list[::-1]
b = word_list[::-1]
print('10 in:', len(a) - a.index(10),' ruby in:',len(b) - b.index('ruby'))