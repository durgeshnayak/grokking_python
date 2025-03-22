with open(file="file1.txt", mode="r") as file1:
    file1_data = file1.readlines()

with open(file="file2.txt", mode="r") as file2:
    file2_data = file2.readlines()

result = [int(num) for num in file1_data if num in file2_data]

# Write your code above 👆

print(result)
