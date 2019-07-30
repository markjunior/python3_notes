from csv import reader
with open('./../data/fighters.csv') as file:
    csv_reader = reader(file, delimiter=',')
    print(csv_reader)
    print(list(csv_reader))
    print('second time')
    print(list(csv_reader))
    file.seek(0)
    next(csv_reader)
    csv_reader = list(reader(file))
    for fighter in csv_reader:
        print(f"{fighter[0]} is from {fighter[1]}")

print('-------------------------------------------')
from csv import DictReader
with open('./../data/fighters.csv') as file:
    csv_reader = DictReader(file)
    print(csv_reader)
    print(list(csv_reader))
    print('second time')
    print(list(csv_reader))
    file.seek(0)
    next(csv_reader)
    csv_reader = list(DictReader(file))
    print(csv_reader)


from csv import writer
with open('./../data/fighters2.csv', 'w') as file:
    csv_writer = writer(file)
    csv_writer.writerow(['name', 'country'])


from csv import DictWriter
with open('./../data/fighters2.csv', 'w') as file:
    headers = ['Name', 'Breed', 'Age']
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        'Name': 'Mark',
        'Breed': 'Asia',
        'Age': 23
    })
