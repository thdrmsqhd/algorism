target_number = input()
number_arr = []
for i in range(len(target_number)):
    number_arr.append(int(target_number[i]))
number_arr.sort(reverse=True)
str_list = list(map(str,number_arr))
print(''.join(str_list))
