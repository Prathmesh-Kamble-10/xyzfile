thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
y.remove("cherry")
thistuple = tuple(y)

# del thistuple #its vanish whole tuple
print(thistuple)