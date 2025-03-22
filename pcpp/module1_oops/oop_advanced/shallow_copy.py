a_list = [10, 20, 30]
b_list = a_list[:]

print(a_list)
print(b_list)
print(a_list is b_list)

b_list[1] = 40
print(a_list)
print(b_list)
print(a_list is b_list)