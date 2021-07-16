import csv

# For reading csv file
# Using lists
with open('population-density 2017 data.csv', 'r') as csv_file:             # r is for specifying read mode
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        Location = row[0]                            # While Using lists we have to reference fields using their indexes
        Location_Code = row[1]
        Year = row[2]
        Population_Density = row[3]
        print(Location, Location_Code, Year, Population_Density)
csv_file.close()

# Using dictionary
with open('population-density 2017 data.csv', 'r') as csv_file:
    csv_dict_reader = csv.DictReader(csv_file)

    for row in csv_dict_reader:
        print(row['Entity'])                    # Benefit of dictionary is that we can reference fields by their names
csv_file.close()








