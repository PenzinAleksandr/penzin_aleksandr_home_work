new_list = [i ** 3 for i in range(1, 1001, 2)]

count = 0


for i in new_list:
    new_i = i
    temp = 0
    while i != 0:
        temp = temp + i % 10
        i = i // 10
    if temp % 7 == 0:
        count = count + new_i
print(count)


new_num = 17

for elem in range(len(new_list)):
    new_list[elem] += new_num


count = 0


for i in new_list:
    new_i = i
    temp = 0
    while i != 0:
        temp = temp + i % 10
        i = i // 10
    if temp % 7 == 0:
        count = count + new_i
print(count)
