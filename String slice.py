base = "abcdefghijklmnopqrstuvwxyz"

print("here are some slices")
print(base[0:3])
print(base[0:5])
print(base[10:])
print(base[:10])
print(base[:])
print(base[::2]) #every other letter
print(base[5:15:3]) #every third letter from the 5th to the 15th
print(base[::-1]) #the whole string backwards
# in slices the beginning is included and end excluded
