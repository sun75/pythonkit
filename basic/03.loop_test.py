array = [1,3,5,7,9]
for x in array:
    print(x)

# print loop times
# 0 1
# 1 3
# 2 5
# 3 7
# 4 9
for(i,x) in enumerate(array):
    print(i, x)

counter = 100
while counter > 10:
    print(counter)
    counter -= 1