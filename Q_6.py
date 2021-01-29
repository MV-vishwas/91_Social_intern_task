
# ----------------------------------------------------------------------------------------------------------------------#
"""6: Write a Python program to convert an array to an array of machine values and return the bytes representation."""
# ----------------------------------------------------------------------------------------------------------------------#

from array import *
print('Enter the size of array.')
n=int(input())
arr=[]
print('Enter the Elements--')
for i in range(n):
    item=int(input())
    arr.append(item)
print(f'\nArray is - {arr}')
print("Bytes representation: ")

x = array('i', arr)
bytearray = x.tobytes()
# print(bytearray)
# temp=str(bytearray)
# print(temp)
# print(type(bytes))

print("b'",end='')
for item in bytearray:
    print(f"0{item}",end='')
print("'")