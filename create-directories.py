"""Purpose of this script is to create directory of employee records from list of employees"""

import os
import csv

root_path = r'C:\Users\User\Desktop\Project Folder'

# creating empty list
list = []

# read employee list, append to empty list
with open('employees.csv') as f:
    for row in f:
        list.append(row.strip('\n').strip('"'))

for items in list:
    path = os.path.join(root_path, items)
    os.mkdir(path)
