import random
# rand_list = 
i = 0
rand_list = []
while i < 10:
    r = random.randint(1,20)
    rand_list.append(r)
    i = i+1
print(rand_list)

# list_comprehension_below_10 =
list_comprehension_below_10 = []
i = 0
while i < 10:
    if rand_list[i] < 10: list_comprehension_below_10.append(rand_list[i])
    i = i+1
print(list_comprehension_below_10)


# list_comprehension_below_10 =
list_comprehension_below_10 = []
def lessthanten(x):
  if x < 10:
    return True
  else:
    return False

lesser = filter(lessthanten, rand_list)

for x in lesser:
  list_comprehension_below_10.append(x)

print(list_comprehension_below_10)