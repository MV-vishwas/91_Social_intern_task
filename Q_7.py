
# ----------------------------------------------------------------------------------------------------------------------#
"""     Write a script which can read the files line by line with .log ext and print it into a
file , while printing the data from the suffix with present date and time of the system.        """
# ----------------------------------------------------------------------------------------------------------------------#

from datetime import datetime
if __name__ == '__main__':
    #creating new file for update log with current time and date.
    new_file=open('./static_files/new_file.log','w')
    #opening the previous log file
    with open('./static_files/Q_7_data.log','r') as f:
        while True:
            line=f.readline()
            if len(line)==0:
                break

            #getting current date and time in given format
            curr_time = datetime.now()
            formatted_time = curr_time.strftime('%m-%d %H:%M:%S.%f')


            # print(formatted_time[0:-3])

            #writing the update line in new file new_file.log
            new_file.write(f'{formatted_time[0:-3]} {line.strip()[18:]}\n')

