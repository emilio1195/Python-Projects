#Creating a list of tuples, where each tuple contains a key and the number of occurrences of that key.
number = '27528'
num_list = []
for n in number:
    num_list.append(n)

num_list = list(set(num_list))


list_tuplas = []
for i in range(len(num_list)):
    list_tuplas.append((num_list[i], number.count(num_list[i])))

print('Tuples List\n', list_tuplas)