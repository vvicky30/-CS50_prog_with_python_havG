import csv 
from csv_row_columns_userinput import creating_csv_withHeader, Row_data_entries
def main():
    # first we're going to make sample.csv file with pre-existing headers/columns
    # specifying headers first
    headers = ["Name", "Age", "Country"] 
    creating_csv_withHeader("sample.csv", headers)
    # now we're going to extend the columns in this csv file so that we can enter more attributes correspondingly while entering row-entries
    #first here going to specify extending columns to the csv file 
    extd_headers = ["Gender", "Profession"] 
    extending_col_csv("sample.csv", extd_headers)
    #now we're going to make entries based on overall final headers in this csv file 
    
    final_headers= headers+extd_headers
    Row_data_entries("sample.csv", final_headers)

def extending_col_csv(filename, new_headers):
    with open(filename, 'r',newline='' ) as csvfile:
        col_reader = csv.reader(csvfile)
        first_row = list(col_reader)  # as well know first row here is actually the rows of headers
    # so here we're going to extend that first row with new_headers
    first_row[0].extend(new_headers)
    
    # now writtting again this first row (with new headers) to the csv file 
    with open(filename, 'w', newline='') as csvfile:
        col_writer = csv.writer(csvfile)
        col_writer.writerow(first_row)

if __name__=="__main__":
    main()

'''
o/p:
How many Row-entries do you want to add to sample.csv-file? (Enter 0 to exit): 5
Enter data for Row 1:
Enter the suitable value for the column 'Name':   vinchenzo halleos
Enter the suitable value for the column 'Age':    34
Enter the suitable value for the column 'Country':  italy
Enter the suitable value for the column 'Gender': male
Enter the suitable value for the column 'Profession': gangstar
Enter data for Row 2:
Enter the suitable value for the column 'Name':   precarous laos 
Enter the suitable value for the column 'Age': 24
Enter the suitable value for the column 'Country':  greece
Enter the suitable value for the column 'Gender': male
Enter the suitable value for the column 'Profession': athlete
Enter data for Row 3:
Enter the suitable value for the column 'Name': vignesh sharma
Enter the suitable value for the column 'Age': 32
Enter the suitable value for the column 'Country':  bharat
Enter the suitable value for the column 'Gender': male
Enter the suitable value for the column 'Profession': engineer
Enter data for Row 4:
Enter the suitable value for the column 'Name': kate dawson
Enter the suitable value for the column 'Age': 29
Enter the suitable value for the column 'Country': scotland
Enter the suitable value for the column 'Gender': female
Enter the suitable value for the column 'Profession': fashion designer
Enter data for Row 5:
Enter the suitable value for the column 'Name': heroshima nagaski
Enter the suitable value for the column 'Age': 45
Enter the suitable value for the column 'Country': japan
Enter the suitable value for the column 'Gender': male
Enter the suitable value for the column 'Profession': doctor
How many Row-entries do you want to add to sample.csv-file? (Enter 0 to exit): 0
You entered zero, exiting data entry...
'''