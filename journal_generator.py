import datetime
from dateutil import parser


def load_template():
    with open('_template.txt', 'r') as content_file:
        content = content_file.read()
    return content


def write_file(name, content):
    with open(name, 'w+') as file:
        file.write(content)


def add_week_days(week_date, date_list):
    for i in range(0, 5):
        date_list.append(week_date + datetime.timedelta(days=i))


def create_date_list(date):
    dates = [date]
    # journal date

    week1_date = date - datetime.timedelta(days=14)
    week2_date = date - datetime.timedelta(days=7)
    end_date = date - datetime.timedelta(days=3)

    dates.append(week1_date)
    dates.append(end_date)

    dates.append(week1_date)
    add_week_days(week1_date, dates)

    dates.append(week2_date)
    add_week_days(week2_date, dates)

    return dates


def format_journal(dates, template):
    datestrings = [date.strftime("%m/%d/%Y") for date in dates]
    return template.format(*datestrings)


def generate_journal(date):
    template = load_template()
    dates = create_date_list(date)
    file_name = '{}-InternshipJournal-MarcChesebro.txt'.format(date.strftime("%m-%d-%Y"))
    write_file(file_name, format_journal(dates, template))


if __name__ == '__main__':
    datestring = input('Enter the due date: ')
    date = parser.parse(datestring)

    generate_journal(date)
    print("done")
