#Import csv to be able to work in csv files
import csv

#Be sure to include ".csv" at the end of the file name
file_name = input("What is the name of the file? ")
keep = input("What would you like to keep? ")
column = int(input("What column number can it be found on? "))
new_file = input("what name would you like to give the new file? ")

#Opening the csv file
with open(file_name,'r') as file:

    #assigning
    original = csv.reader(file)
    #opening the new file
    file_to_keep = open(new_file,'w', newline = '')
    new_list = csv.writer(file_to_keep, delimiter = ',',quoting=csv.QUOTE_MINIMAL)
    for line in original:
        
        if line[column-1] == keep:
            new_list.writerow(line)
    file_to_keep.close()
