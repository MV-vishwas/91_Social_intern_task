
# ----------------------------------------------------------------------------------------------------------------------#
"""     4: Write a Python program to sort a list of dictionaries using Lambda.
Original list of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2',
'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
Sorting the List of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7,
'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]        """
# ----------------------------------------------------------------------------------------------------------------------#


if __name__ == '__main__':
    list1=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': 2,'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
    #lamda taking the one arugment that is value at location ith on list and the key is based on that
    ans=sorted(list1,key=lambda item:item['color'])
    print('\nSorted list by color-\n',ans)
    ans = sorted(list1, key=lambda item: item['make'])
    print('\nSorted list by make-\n', ans)
    ans = sorted(list1, key=lambda item: item['model'])
    print('\nSorted list by model-\n', ans)

