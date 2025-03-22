# 🚨 Don't change the code below 👇
row1 = ["0","️0","️0"]
row2 = ["0","0","️0"]
row3 = ["0","0","0"]
map = [row1, row2, row3]
print("   1    2   3")
print(f"1{row1}\n2{row2}\n3{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
column = int(position[0])
row = int(position[1])
if row == 1 and 0 < column <= 3:
    row1[column - 1] = "X"
elif row == 2 and 0 < column <= 3:
    row2[column - 1] = "X"
elif row == 3 and 0 < column <= 3:
    row3[column - 1] = "X"
else:
    print("Bad input...")
# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
