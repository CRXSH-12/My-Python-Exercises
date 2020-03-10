# Creating a varible with a list of numbers that will be used to calculate the sum of total numbers within the list
num = [56, 78, 34, 21, 56, 34, 125, 45, 89, 75, 12, 56]
print(type(num))
print(num)
print(sum(num))

# Using the sorted function to sort numbers and display the largest and smallest number
print(sorted(num))
print("largest number is: ", num[6])
print("smallest number is: ", num[10])

# Using an if statement to remove duplicate numbers
def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
# Making use of the Remove function to remove duplicate numbers
duplicate = [56, 78, 34, 21, 56, 34, 125, 45, 89, 75, 12, 56]
print(Remove(duplicate))