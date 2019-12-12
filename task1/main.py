import csv
import datetime

def main():
    content = get_csv_content()
    born_after = datetime.date(1999, 12, 31)
    print(count_people_born_after(content, born_after))
    for name in get_people_that_names_end_with(content, 'a'):
        print(name)

def get_csv_content():
    with open('test.csv', 'r') as file:
        reader = csv.reader(file)

        #skip header
        next(reader)
        content = list(reader)

    return content

def count_people_born_after(people_list, born_after):
    count = 0
    for person in people_list:
        person_birthday = datetime.datetime.strptime(person[2], '%d.%m.%Y').date()
        if(person_birthday > born_after):
            count += 1
    return count

def get_people_that_names_end_with(people_list, letter):
    names = []
    for person in people_list:
        if(person[0][-1:] == letter):
            names.append(person[0])
    names = list(set(names))
    return names

if __name__ == '__main__':
    main()