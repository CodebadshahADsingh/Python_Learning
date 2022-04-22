#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      AMANDEEP SINGH
#
# Created:     05-03-2022
# Copyright:   (c) AMANDEEP SINGH 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------


marks=[0,1,2]
print(marks)
print(marks[1])
print(marks[2])

print(marks[0])


print("-----------------------")
print(marks[-1])
print(marks[-2])
print(marks[-3])
print("-----------------------")


print(marks[0:2])
print(marks[1:3])

print("--------------------------")

for score in marks:
    print(score)
print("-----------------------")

marks.append(99)
print(marks)



print("-----------------------")


marks.insert(2,88)
print(marks)
print("-----------------------")


print(93 in marks)
print(88 in marks)

print("-----------------------")

print(len(marks))

print("-----------------------")
print("-----------------------")



m=0
while m < len(marks):
    print(marks[m])
    m+=1

    #lets clear thre list

marks.clear()
print(marks)