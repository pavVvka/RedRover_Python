list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
[print(list_1[i]) for i in range(len(list_1)) if type(list_1[i]) is int]

l1 = ['cat', 'dog', 'horse', 'cow']
print(tuple(l1))

l2 = [2, 6, 3, 4, 1, 9, 5]
n = len(l2)
print(n)
for i in range(1, n):
    print(f"i = {i}")
    for k in range(n - i):
        print(f"k = {k}", end="; ")
    print()


