

# ----------------------------------------------------------------------------------------------------------------------#
"""     Write a Python program that takes a text file as input and returns the number of words of a given text file.
Note: Some words can be separated by a comma with no space.     """
# ----------------------------------------------------------------------------------------------------------------------#

if __name__ == '__main__':
    with open('./static_files/Q_5_data','r') as f:
        data=f.read()
        data=data.replace(',',' ')
        # print(data)
        ans_list=data.split()
        # print(ans_list)
        print('Total words in file is-',len(ans_list))