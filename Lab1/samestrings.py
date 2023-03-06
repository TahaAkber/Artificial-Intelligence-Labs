#if len greater than 2 and first and last index is same
list1 = ["taha", "talha", "zulminun", "aba", "1221", "acha","aa","abracadabra"]
i = 0
j = 0
for i in range(len(list1)):
    if len(list1[i]) > 2:
        if list1[i][0] == list1[i][-1]:
            j = j+1
print(j)
