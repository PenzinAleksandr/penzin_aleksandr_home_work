procent_list = [i for i in range(1, 101, 1)]
for i in procent_list:
    if i == 1 or i % 10 == 1 and (i not in range(11, 14)):
        i = (str(i) + " процент")
    elif i % 10 >= 2 and i % 10 <= 4 and (i not in range(12, 15)):
        i = (str(i) + " процента")
    else:
        i = (str(i) + " процентов")
    print(i)
