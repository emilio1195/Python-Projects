number = '2752833366664'
num_list = []
for n in number:
    num_list.append(n)

num_list = list(set(num_list))


dic_digitos = {}
for i in range(len(num_list)):
    dic_digitos[num_list[i]] = number.count(num_list[i])

print('Dictionary\n', dic_digitos)