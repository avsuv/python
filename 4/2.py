my_list = [2, 3, 21, 123, 63, 452, 140, 141, 12, 40, 140, 147, 240]
print(my_list)

new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]
print(new_list)

final_list = [el for el in new_list if el in range(20, 241) and (el % 20 == 0 or el % 21 == 0)]
print(final_list)