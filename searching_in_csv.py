import csv

# Function to search for a person by name or occupation in a CSV file
def search_in_csv(filename, search_query):
    results = []
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # Skip the header row(which is top most row)
        for row in reader:
            # Check if the search query matches the name or profession
            if search_query.lower() in (row[0].lower(), row[-1].lower()):
                results.append(row)
    return results

# Example usage
sq= input("Enter the query-word based on which you want to search in csv-file: ")
search_results = search_in_csv('sample.csv', search_query=sq)      # using exisiting sample.csv file here for searching based on query 
if search_results:  # if search_results contain some value then this  will be true 
    print("Search Results:")
    for result in search_results:
        print(result)
else:
    print("No results found.")

'''
o/p:
first run (search by name ):-
Enter the query-word based on which you want to search in csv-file: vignesh sharma
Search Results:
['Vignesh Sharma', '32', 'Bharat', 'Male', 'Engineer']

in 2nd run (search by profession) :-
Enter the query-word based on which you want to search in csv-file: doctor
Search Results:
['Heroshima Nagaski', '45', 'Japan', 'Male', 'Doctor']


'''