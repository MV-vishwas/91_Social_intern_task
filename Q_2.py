# ----------------------------------------------------------------------------------------------------------------------#
"""     Write a Python program to calculate the number of days between two dates. Sample dates : (20200702), (20200711)     """
# ----------------------------------------------------------------------------------------------------------------------#
if __name__ == '__main__':
    from datetime import date
    print('Enter the first date(format-YYYYMMDD)')
    date1=input()
    print('Enter the second date(format-YYYYMMDD)')
    date2=input()

    ## checking the format and range of input date is correct or not
    if date1.isdigit() and date2.isdigit() and len(date2)==8 and len(date1)==8:
        if 1 <= int(date1[6:]) <= 31 and 1 <= int(date2[6:]) <= 31 and 1 <= int(date1[4:6]) <= 12 and 1 <= int(date2[4:6]) <= 12:

            # pass
            # date1=f'{date1[0:4]},{date1[4:6]},{date1[6:]}'
            # print(date1)
            # date2 = f'{date2[0:4]},{date2[4:6]},{date2[6:]}'
            # print(date2)
            # date1=int(date1)
            # date2 = int(date2)

            date1=date(int(date1[0:4]),int(date1[4:6]),int(date1[6:]))
            date2=date(int(date2[0:4]),int(date2[4:6]),int(date2[6:]))

            diff=date2-date1

            #printing the difference in days
            print(diff.days)

        else:
            print('Invalid format')
    else:
        print('Invalid format.')
