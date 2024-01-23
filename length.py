str1 = 'python'
# 1st way:
lenstr = 0
for i in str1:
    lenstr += 1
print(lenstr)
# 2nd way
print(len(str1))
# 3rd way
j = 0
while j == len(str1):
    lenstr += 1
print(lenstr)
# 4th way
l1 = list(str1)
print(len(l1))
