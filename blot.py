#Import csv to be able to work in csv files
import csv

#Be sure to include ".csv" at the end of the file name
file_name = input("What is the name of the file? ")
gender = input("What gender would you like to take out? ")
new_file = input("what name would you like to give the new file? ")

#Opening the csv file
with open(file_name,'r') as file:

    #assigning
    original = csv.reader(file)
    #opening the new file
    feminine = open(new_file,'w', newline = '')
    female_list = csv.writer(feminine, delimiter = ',',quoting=csv.QUOTE_MINIMAL)
    for line in original:
        
        if line[1] != gender.capitalize():
            female_list.writerow(line)
    feminine.close()
