from collections import OrderedDict
import datetime
import sys, os

from peewee import *
db = SqliteDatabase('dairy.db')


class Entry(Model):
    content = TextField()
    time_stamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        """
        what is it for? it's tell the Model what Database is belongs to We do that, by defining a class called Meta
        (this is just a class that called meta) inside of our Entry class in this case,
        (you can have classes inside of classes.) and it have one attribute which is 'database', because we're going to
        set database as being equal to 'db' which is our SQLite database we created up on line above.
        """
        database = db


def initialize():
    """
    Create database and the table if they don't exist
    :return:
    """
    db.connect()
    db.create_tables([Entry], safe=True)


def menu_loop():
    """
    show the menu
    因為 python 沒有 switch 所以寫成這樣
    :return:
    """
    choice = None
    while choice != 'q':
        print("Enter 'q' to quit!")
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        #     因為value是 function, 所以 value.__doc__就是function的註解
        choice = input('Action: ').lower().strip()  # stripe of any extra spaces
        # choice -> the func user selected
        if choice in menu:
            menu[choice]()  # -> 執行function

def add_entry():
    """
    add an entry
    :return:
    """
    print('Enter your entry. Press ctrl+d when finished.')
    data = sys.stdin.read().strip()
#     請注意，使用 sys.stdin.read() 要小心，因為它會等待直到標準輸入中的數據結束，如果沒有明確的結束標誌（例如 Ctrl+D），
#     那麼程序可能會一直等待
#     stdin -> keyboard
    if data:
        if input('Save entry? [Y / n]').lower() != 'n':
            Entry.create(content=data)
            print('Saved successfully')


def view_entries(search_query=None):
    """
    view previous entry
    當有 search_query 才會啟用
    :return:
    """
    entries = Entry.select().order_by(Entry.time_stamp.desc())
    if search_query:
        entries = entries.where(Entry.content.contains(search_query))
    #     where 就像 filter

    for entry in entries:
        timestamp = entry.time_stamp.strftime(' %A %B %d, %Y %I:%M%p')
        print(timestamp)
        print('='*len(timestamp))
        print(entry.content)
        print('N) next entry')
        print('q) return to main menu')

        next_action = input('Action: [Ndq]. ').lower().strip()
        if next_action == 'q':
            break
        elif next_action == 'd':
            delete_entry(entry)


def search_entry():
    view_entries(input('Search query: '))



def delete_entry(entry):
    """
    :param entry:
    :return:
    """
    entry.delete_instance()

def clear():
    os.system('cls' if os.name =='nt' else 'clear')
    # 檢查操作系統，選擇清空屏幕的命令
#     在 window是cls ios是clear




menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    ('s', search_entry)

])

if __name__ == "__main__":
    initialize()
    menu_loop()