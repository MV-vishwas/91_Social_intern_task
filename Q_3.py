# ----------------------------------------------------------------------------------------------------------------------#
"""     Write a Python program to convert the Python dictionary object (sort by key) to
JSON data. Print the object members with indent level 4.        """
# ----------------------------------------------------------------------------------------------------------------------#


if __name__ == '__main__':
    import json
    d1={'aman':'indore','jay':'dewas','deepak':'ujjain','arti':'indore','sachin':'dewas','shivam':'bhopal','manav':'indore'}
    print('Normal data=',d1)
    print('Json data--')
    print(json.dumps(d1,indent=4,sort_keys=True))
