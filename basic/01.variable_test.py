name = "hello"
online = True
age = 20
price = 6.3
array = [1, 2, 3, 4, 5, 6]
my_dict = {"a":1,"b":2,"c":"hello"}

print(name, online, age, price)
print(name[0:2])           # trim value from string => he
print(type(name))
print(float("3"))
print(len(array))          # 6
print(array[0], array[1])  # 1 2
print(my_dict["a"])
my_dict["a"]=100           # update value in dictionary
print(my_dict["a"])
