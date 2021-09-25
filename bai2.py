
print("Câu a")
a = [1,1,2,3,5,8,13,21,34,55,88]
b = [1,3,5,4,7,88,66,59,40,54]
c = list(set (a)& set(b))
print(c)

print("Câu b")
a = list (set(a)-set(c))
b = list (set(b)-set(c))
print(a)
print(b)