lst = [1,4,3,2,7,6,5]
# list.sort(reverse=True)
# print(list)
i=0
n = len(lst)

for i in range(n):
    for j in range(0, n-i-1):
        if lst[j] > lst[j+1]:
            # Swap if the element found is greater than the next element
            lst[j], lst[j+1] = lst[j+1], lst[j]

print(lst)