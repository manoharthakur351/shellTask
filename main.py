import argparse
import sys
import mysql.connector
import os
import hashlib
import configparser
from prettytable import PrettyTable

# some basic initialisations
config = configparser.ConfigParser()
config.read("config.ini")


class task:
    STATUS = None
    PERCENT = None
    created_on = None
    completed_on = None

    # constructor
    def __init__(self):
        return None


class User:
    name = None
    id = None
    goals = []

    # constructor
    def __init__(self):
        pass

    # print goals
    def print_goals(self, cursor):
        table = PrettyTable(["id", "goal", "dead line"])
        # printing all goals
        cursor.execute("SELECT * FROM goals")
        for x in cursor:
            table.add_row(list(x))
        print(table)
        return


class Goal:
    dead = None
    name = None

    # constructor
    def __init__(self):
        pass


class Day:
    tasks = []
    pass


# FUNCTIONS--------------------------------------------------------------------------------------------------------------

# delete goal
def delete_goal(cursor, conn):
    goal_id = input("\t enter goal id you wanna delete >_ ")
    q = f"DELETE FROM goals WHERE goalid='{goal_id}'"
    try:
        cursor.execute(q)
        conn.commit()
    except:
        print("[!] ERROR! unable to delete goal.")
    return


def newgoal(cursor, conn):
    name = input("\t name: ")
    dead = input("\t deadline: ")
    q = f"insert into goals (name, deadline) values ('{name}','{dead}')"
    try:
        cursor.execute(q)
        conn.commit()
        return "success"
    except:
        return "faliure"


# clean screen with logo
def clear():
    os.system("clear")
    os.system("echo WELCOME TO")
    os.system("figlet shellTask")


# authentication
def authentic(cursor):
    username = input("username: ")
    pass_str = input("password: ")
    querry = (
        f"select * from users where username='{username}' and password='{pass_str}'"
    )
    # print(querry)
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

    # initialisations
    table = PrettyTable(["id", "goal", "dead line"])

    # connection object
    mydb = mysql.connector.connect(
        host=config["DATABASE"]["host"],
        user="u0_a74",
        password="0000",
        database="shelltask",
    )

    mycursor = mydb.cursor()

    # authenticate
    authentic(mycursor)
    user = User()
    clear()

    # mainloop
    while True:
        clear()

        # options
        user.print_goals(mycursor)
        print("[ ] Choose a operation:")
        print("  01: new goal")
        print("  02: remove goal")
        print("  03: view goal")
        print("  04: edit goal")
        print()

        choice = input("[*] Choice >_ ")

        # 1 adding new goal
        if choice == "01":
            o = newgoal(mycursor, mydb)
            input(o)

        # 2 remove goal
        if choice == "02":
            delete_goal(mycursor, mydb)

        # 3 view goal
        if choice == "03":
            pass

        # 4 edit goal
        if choice == "04":
            pass

        # test
        if choice == "05":
            mycursor.execute("SHOW tables")
            for x in mycursor:
                print(x)
            input()

        # exit
        if choice == r"/":
            print("[ ] Terminating Session")
            mycursor.close()
            mydb.commit()
            mydb.close()
            exit()


if __name__ == "__main__":
    main()
