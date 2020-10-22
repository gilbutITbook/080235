
#
# 아이템 28
#
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print(flat)

#
squared = [[x**2 for x in row] for row in matrix]
print(squared)

#
my_lists = [
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [1, 2, 3]],
    [[4, 5, 6], [7, 8, 9]],
]
flat = [x for sublist1 in my_lists
        for sublist2 in sublist1
        for x in sublist2]

#
flat = []
for sublist1 in my_lists:
    for sublist2 in sublist1:
        flat.extend(sublist2)

#
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [x for x in a if x > 4 if x % 2 == 0]
c = [x for x in a if x > 4 and x % 2 == 0]

#
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
filtered = [[x for x in row if x % 3 == 0]
            for row in matrix if sum(row) >= 10]
print(filtered)
