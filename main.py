import argparse
import sys
import mysql.connector
import os
import hashlib
import configparser

# some basic initialisations
config = configparser.ConfigParser()
config.read('config.ini')

class task:

    STATUS = None
    PERCENT = None
    created_on = None
    completed_on = None

    # constructor
    def __init__(self):
        return None

    #


class Goal:
    DEADLINE = None

    pass


class Day:
    tasks = []
    pass


# functions
querry1 = """
CREATE TABLE test1 (                                          sno int (5) ,
name varchar (50) not null,
deadline datetime not null,
taskid int (5) not null,
primary key (sno)
)
"""

def clear():
    os.system("clear")
    os.system("echo WELCOME TO")
    os.system("figlet shellTask")

def authentic(cursor):
    username = input("username: ")
    pass_str = input("password: ")
    querry = (
        f"select * from users where username='{username}' and password='{pass_str}'"
    )
    #print(querry)
    cursor.execute(querry)
    result = cursor.fetchone()
    if result:
        print("Welcome, " + username)
    else:
        print("Incorrect username or password.")
        clear()
        print("incorrect username or password")
        authentic(cursor)



# Main
def main():
    clear()
    mydb = mysql.connector.connect(
        host=config['DATABASE']['host'], user="u0_a74", password="0000", database="shelltask"
    )

    mycursor = mydb.cursor()

    # authenticate
    authentic(mycursor)
    while True:
        clear()
        print("[ ] Choose a operation:")
        print("  01: List goals")
        print("  02: New goal")
        print("  03: exit")
        print("  04: other.....")
        print("  05: list tables in shelltask")
        choice = input("[*] Choice >_ ")

        if choice == "01":
            clear()
            print("[ ] Here os list of goals:-")
            mycursor.execute("SELECT * FROM goals")
            for x in mycursor:
                print(x)

            input()

        if choice == "05":
            clear()
            mycursor.execute("SHOW tables")
            for x in mycursor:
                print(x)
            input()

        if choice == "":
            clear()
            print("[ ] Terminating Session")
            mydb.close()

            exit()


if __name__ == "__main__":
    main()
