#! /opt/miniconda3/bin/python3
'''
tracker is an app that maintains a list of personal
financial transactions.

It uses Object Relational Mappings (ORM)
to abstract out the database operations from the
UI/UX code.

The ORM, Category, will map SQL rows with the schema
  (rowid, category, description)
to Python Dictionaries as follows:

(5,'rent','monthly rent payments') <-->

{rowid:5,
 category:'rent',
 description:'monthly rent payments'
 }

Likewise, the ORM, Transaction will mirror the database with
columns:
amount, category, date (yyyymmdd), description

In place of SQL queries, we will have method calls.

This app will store the data in a SQLite database ~/tracker.db

Note the actual implementation of the ORM is hidden and so it 
could be replaced with PostgreSQL or Pandas or straight python lists

'''

# from transactions import Transaction
from datetime import datetime
from enum import Enum

from category import Category
import sys

# transactions = Transaction('tracker.db')
category = Category('tracker.db')

# here is the menu for the tracker app

menu = '''
0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu
'''


def process_choice(choice):
    # 0. quit
    if choice == '0':
        return
    # 1. show categories
    elif choice == '1':
        cats = category.select_all()
        print_categories(cats)
    # 2. add category
    elif choice == '2':
        name = input("category name: ")
        desc = input("category description: ")
        cat = {'name': name, 'desc': desc}
        category.add(cat)
    # 3. modify category
    elif choice == '3':
        print("modifying category")
        rowid = int(input("rowid: "))
        name = input("new category name: ")
        desc = input("new category description: ")
        cat = {'name': name, 'desc': desc}
        category.update(rowid, cat)
    # 4. show transactions
    elif choice == '4':
        for cat in category:
            print(cat)
    # 5. add transaction
    # Author: Kelly Zhang
    elif choice == '5':
        print("adding a transaction")
        name = input("new category name: ")
        desc = input("new category description: ")
        cat = {'name': name, 'desc': desc}
        category.add(cat)
    # 6. delete transaction
    # Author: Kelly Zhang
    elif choice == '6':
        print("deleting a transaction")
        rowid = int(input("rowid to be deleted: "))
        category.delete(rowid)
    # 7. summarize transactions by date
    # Author: Xianzhen Zhao
    elif choice == '7':
        print("summarizing transactions by date")
        try:
            date_input = input("Please input date(YYYY-MM-DD): ")
            validate(date_input, DateFormat.DATE)
            cats = category.select_by_date(date_input)
            print_categories(cats)
        except ValueError as error:
            print(str(error))

    # 8. summarize transactions by month
    # Author: Xianzhen Zhao
    elif choice == '8':
        print("summarizing transactions by month")
        try:
            date_input = input("Please input date(YYYY-MM): ")
            validate(date_input, DateFormat.MONTH)
            cats = category.select_by_month(date_input)
            print_categories(cats)
        except ValueError as error:
            print(str(error))

    # 9. summarize transactions by year
    elif choice == '9':
        print("summarizing transactions by year")

    # 10. summarize transactions by category
    elif choice == '10':
        print("summarizing transactions by category")

    # 11. print this menu
    # Author: Kelly Zhang
    elif choice == '11':
        print("menu: ", menu)
    # all other choices
    else:
        print("choice", choice, "not yet implemented")

    choice = input("> ")
    return (choice)


def toplevel():
    ''' handle the user's choice '''

    ''' read the command args and process them'''
    print(menu)
    choice = input("> ")
    while choice != '0':
        choice = process_choice(choice)
    print('bye')


#
# here are some helper functions
#

def print_transactions(items):
    ''' print the transactions '''
    if len(items) == 0:
        print('no items to print')
        return
    print('\n')
    print("%-10s %-10d %-10s %-10d %-30s" % (
        'item #', 'amount', 'category', 'date', 'description'))
    print('-' * 40)
    for item in items:
        values = tuple(item.values())
        print("%-10s %-10d %-10s %-10d %-30s" % values)


def print_category(cat):
    print("%-3d %-10s %-30s" % (cat['rowid'], cat['name'], cat['desc']))


def print_categories(cats):
    print("%-3s %-10s %-30s" % ("id", "name", "description"))
    print('-' * 45)
    for cat in cats:
        print_category(cat)


def validate(date_text, date_format):
    try:
        if date_format == DateFormat.DATE:
            format_str = "%Y-%m-%d"
            if date_text != datetime.strptime(date_text, format_str).strftime(format_str):
                raise ValueError("Wrong Date Input Format, yyyy-mm-dd")
            return True
        elif date_format == DateFormat.MONTH:
            format_str = "%Y-%m"
            if date_text != datetime.strptime(date_text, format_str).strftime(format_str):
                raise ValueError("Wrong Date Input Format, yyyy-mm")
            return True
        elif date_format == DateFormat.YEAR:
            if date_text != datetime.strptime(date_text, "%Y").strftime('%Y'):
                raise ValueError("Wrong Date Input Format, yyyy")
            return True
    except ValueError:
        raise ValueError("Wrong Date Input Format")


class DateFormat(Enum):
    DATE = 1
    MONTH = 2
    YEAR = 3


# here is the main call!

toplevel()
