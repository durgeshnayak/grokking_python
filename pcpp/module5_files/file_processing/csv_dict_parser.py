import csv

with open(file='exp_contacts.csv', mode='w', newline='') as csv_file:
    field_names = ['Name', 'Species']
    dict_writer = csv.DictWriter(csv_file, field_names)

    dict_writer.writeheader()
    dict_writer.writerow({'Name': 'Frodo', 'Species': 'Hobbit'})

with open(file='exp_contacts.csv', mode='r', newline='') as csv_file:
    dict_reader = csv.DictReader(f=csv_file, fieldnames=field_names, delimiter=',')
    for row in dict_reader:
        print(f'{row["Name"]}, {row["Species"]}')

