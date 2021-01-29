
# ----------------------------------------------------------------------------------------------------------------------#
"""Program to Generate random logs and write in a file , once the file size reaches 2Mb
open new file and continue writing"""
# ----------------------------------------------------------------------------------------------------------------------#


import json
import os
import time
from datetime import datetime

def create_file():
    with open('./static_files/count_log.json','r') as f:
        count=json.loads(f.read())
    curr_count=count['current_log']
    flag=os.path.exists(f'static_files/log_{curr_count+1}.log')
    if flag==False:
        with open(f'static_files/log_{curr_count+1}.log','w'):
            with open('./static_files/count_log.json', 'w') as f:
                d1 = {"current_log": curr_count + 1}
                json_object = json.dumps(d1, indent=4)
                f.write(json_object)


def check_size(path):
    file_size = os.path.getsize(path)
    # print("File Size is :", file_size, "bytes")
    if file_size>=2000000:
        #need to create new file
        return True
    else :
        return False

def get_curr_log():
    print('getting log file.')
    with open('./static_files/count_log.json', 'r') as f:
        count = json.loads(f.read())
    curr_count = count['current_log']
    path = f'./static_files/log_{curr_count}.log'
    return path

if __name__ == '__main__':
    # opening current log file
    path=get_curr_log()

    print('Generating logs.....')
    f=open(path,'a')
    for i in range(1,100000):
        curr_time = datetime.now()
        formatted_time = curr_time.strftime('%Y-%m-%d %H:%M:%S.%f')
        time.sleep(0.001)
        log=formatted_time+'    '+'that can be random msg for log   status{failed/passed}   IPaddress   Method\n'
        if check_size(path):
            print('Size exceeded..')
            create_file()
            path=get_curr_log()
            f=open(path,'a')
        f.write(log)
print("Successfully written logs.")
