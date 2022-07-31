# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел нет одного, чтобы выполнялось условие A[i]-1 = A[i-1]
# Найдите это число

import os
path = os.path.join('Folder', 'File_1')

# 1-й вариант

with open(path, 'r') as file:
    data = (file.read()).split()    
my_list = list(map(int, data))
print(my_list)

numb = [my_list[i] for i in range(1, len(my_list))
                    if my_list[i] - 1 != my_list[i-1]]
res = numb[0] - 1                               
print(res)

#--------------------------------------------------------------------------#

# 2-й вариант

with open(path, 'r') as file:
    data = (file.read()).split()    
my_list = list(map(int, data))
print(my_list)

f = lambda x: my_list[x] - my_list[x-1] != 1
numb = list(filter(f, range(1, len(my_list))))
res = numb[0] + 1
print(res)