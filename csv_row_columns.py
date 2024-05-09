'''
When you open a file in text mode without specifying newline='', Python automatically converts any newline characters encountered on read to the 
'\ n' character. Similarly, on write operations, it converts '\ n' characters to the appropriate newline convention for the operating system.

By specifying newline='', you're effectively disabling this automatic newline conversion behavior. This can be useful when you want full control over newline handling, 
especially when dealing with CSV files, where you want to maintain the exact formatting specified by the writer.

In the context of working with CSV files, it's often recommended to use newline='' 
when working with the csv module to prevent double spacing between rows when writing to CSV files, 
especially on Windows systems. This ensures consistent behavior across different platforms.
'''
#This below script creates a CSV file named "experiment.csv" with three columns: 'Name', 'Age', and 'Country', and five rows of data.
import csv
# first we import standard csv module of python 

def main():
    
    # first we create csv file initialized with pre-exisitng columns 'Name', 'Age' , 'Country'
    creating_csv("experiment.csv",headers = ["Name", "Age", "Country"]) 
    
    rows = [
        ["Skrillix hellios", 20 , "America"],
        ["Helmand kilochock",22,"Kazakhistan"],
        ["Precarious ferriera",28,"Lebnon"],
        ["Sphinix Herodotous",32,"Ezypt"],
        ["Carolina Camroon",35,"United kingdom"]
    ] 
    adding_rows("experiment.csv",rows ) 
    
def creating_csv(filename,headers):
    with open(filename, "w", newline='') as csvfile:
        col_writer = csv.writer(csvfile)
        col_writer.writerow(headers)  # here using writerow function as we need to write one row of headers acts as columns

def adding_rows(filename, rows):
    with open(filename,"a",newline='') as csvfile:
        row_writer =csv.writer(csvfile)
        row_writer.writerows(rows)  # here using writerows function as we can append multiple rows at a time .
        
 
if __name__=="__main__":
     
    main()

'''
in  experiment.csv file :

Name,Age,Country
Skrillix hellios,20,America
Helmand kilochock,22,Kazakhistan
Precarious ferriera,28,Lebnon
Sphinix Herodotous,32,Ezypt
Carolina Camroon,35,United kingdom
'''