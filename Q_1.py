# ----------------------------------------------------------------------------------------------------------------------#
"""     Write a Python program to read a file line by line and store it into a list.    """
# ----------------------------------------------------------------------------------------------------------------------#
if __name__ == '__main__':
    with open('./static_files/Q_1_data.txt','r') as f:
        data=f.readlines()

    l1=[] #define a list

    for line in data:
        # storing the line in l1
        l1.append(line.strip())

    #print data of list
    print('\t\tList of lines are--\n')
    for index,item in enumerate(l1):
        print(f'Line-{index+1} : {item}')
