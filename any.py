# any 
print(any([0,0,0,0,0]))
print("=================")
print(any([0,1,0,0,0]))
print(any([]))
print("========================")
numbers = [1,2,4,6,8]
print(any([num %2 != 0 for num in numbers]))