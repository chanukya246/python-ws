items = [("p1", 243), ("p2", 34), ("p3", 2)]

# sorting
items.sort(key=lambda item: item[1])

x = [item for item in items if item[1] >= 34]

print(x)


list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]

print(list(zip("abcde", list1, list2)))
print(items[1])
