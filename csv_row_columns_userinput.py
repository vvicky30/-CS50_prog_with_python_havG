# creating csv file with pre-exisiting headers/columns 
import csv 
def main():
    # first we create csv file initialized with pre-exisitng columns 'Name', 'Age' , 'Country'
    headers = ["Name", "Age", "Country"]
    creating_csv_withHeader("exp.csv", headers)
    # now we're going to make enteries in this file  
    Row_data_entries("exp.csv",headers)

       
     
    

def creating_csv_withHeader(filename, headers):
    with open(filename, 'w', newline='') as csvfile:
        column_writer = csv.writer(csvfile)
        column_writer.writerow(headers)
         

#def rows(filename, data):
#    with open(filename,'a',newline='') as csvfile:
#        row_writer = csv.writer(csvfile)
#        row_writer.writerows(data)
    
def Row_data_entries(filename, headers):
    while True:
        try:  
            num_entries = int(input(f"How many Row-entries do you want to add to {filename}-file? (Enter 0 to exit): "))
            if num_entries == 0:
                print("You entered zero, exiting data entry...")
                break
            # This loop will continue to take input from the user according to the number of entries specified
            data = []  # Initialize list to store all row entries
            for i in range(num_entries):
                print(f"Enter data for Row {i + 1}:")
                entry = []  # Initialize list to store one row of data
                for header in headers:
                    value = input(f"Enter the suitable value for the column '{header}': ").strip().title()
                    entry.append(value)  # Append each header value to the row
                data.append(entry)  # Append the entire row to the data list
            # Write the data to the CSV file
            with open(filename, 'a', newline='') as csvfile:
                row_writer = csv.writer(csvfile)
                row_writer.writerows(data)
        except ValueError:
            print("Please enter a valid number, foe making enteries in the CSV-file")
        
        
if __name__=="__main__":
    main()  
'''
o/p:
How many Row-entries do you want to add to exp.csv-file? (Enter 0 to exit): 3
Enter data for Row 1:
Enter the suitable value for the column 'Name':          heroshima nigaski  
Enter the suitable value for the column 'Age':    67
Enter the suitable value for the column 'Country':   japan
Enter data for Row 2:
Enter the suitable value for the column 'Name':    geliiepio hemrath
Enter the suitable value for the column 'Age': 33
Enter the suitable value for the column 'Country':   newzealand 
Enter data for Row 3:
Enter the suitable value for the column 'Name': gaurav mishra
Enter the suitable value for the column 'Age': 28
Enter the suitable value for the column 'Country':  bharat
How many Row-entries do you want to add to exp.csv-file? (Enter 0 to exit): 0
You entered zero, exiting data entry...
'''
         
         
                       
                    