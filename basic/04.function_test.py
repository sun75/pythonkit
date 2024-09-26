def sum_values(values):
    s = 0
    for i in values:
        s += i
    return s
array = [1,3,5,7,9]
print(sum_values(array))   # 25

# default params
def show_name(name="frank"):
    print(name)
show_name("peter")      # peter
show_name()             # frank
show_name(name="amy")   # amy