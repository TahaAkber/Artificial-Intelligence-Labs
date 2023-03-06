# greater than 5 strings and smaller case then append in newlist
list1 = ["TAHA", "AKBER", "zulminun", "zia",
         "Talha", "khan", "abdullah","wahab"]
new_list = []

for x in list1:
    if len(x) > 5:
        if x.lower() == x:
            new_list.append(x)

print(new_list)

# removing 0,4,5 index and then append in newlist
sample = ["red", "green", "yellow", "pink", "margenda", "blue", "yellow-Red"]
new_list1 = []
i = 0
for i in range(len(sample)):
    value = sample[i]
    if i != 0 and i != 4 and i != 5:
        new_list1.append(value)

print(new_list1)
