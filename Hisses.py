def func(x):
  res = 0
  for i in range(x):
     res += i
     print(res)
  return res

print(func(4))

list1=[i for i in range(10)]
print(list1)

for i in list1:
    j=i+1
    list1.append(j)
print(list1)
