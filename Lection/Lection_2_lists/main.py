list1 = []
list2 = list()
size = 5
p = 2
for i in range(10): 
  i = p + 2
  p *= 2
  if i > 100:
    break
  list2.append(i)
print(type(list1), list2, len(list2))
index = 0
for el in list2:
  if index % 2 == 0 and index != 0:
    print("list[{}] = {}".format(index, el))
  index += 1

for i in range(len(list2)):
  print(f'list2[{i}] = {list2[i]}')

print(list2.pop())
print(list2)

for i in range(len(list2) - 2):
  list2.pop(i)
print(list2)