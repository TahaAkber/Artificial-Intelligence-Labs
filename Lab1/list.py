list1 = ["Apple", "Samsung", "Oneplus", "Google", "Motorola"]
# print(dir(list))
# insert at end
list1.append("OPPO")
list1.append("VIVO")

# insert at given position
list1.insert(3, "Xiaomi")
print(list1)

# delete from end
list1.pop()
print(list1)

# delete from any position by giving name
list1.remove("Apple")
print(list1)

# sorting numbers in ascending order
Unsorted = [2, 10, 34, 6, 3, 2, 1]

# help(Unsorted.sort)
Unsorted.sort()
print(Unsorted)

# sorting in descending order
Unsorted.sort(reverse=True)
print(Unsorted)
