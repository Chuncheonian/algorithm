# Dongyoung Kwon @Chuncheonian (ehddud2468@gmail.com)

def exchange_sort(list: list) -> list:
  for i in range(len(list)-1):
    for j in range(i+1, len(list)):
        if (list[i] > list[j]):
            list[i], list[j] = list[j], list[i] # swap
  return list

# Testcase
list = [3, 2, 6, 5, 8, 7]
print(exchange_sort(list))