import argparse
import sys
import mysql.connector
import os
import hashlib
import configparser
import getpass
from prettytable import PrettyTable

# some basic initialisations
config = configparser.ConfigParser()
config.read("config.ini")

# CLASSES (incomplete)============================================================================================================--

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


# FUNCTIONS============================================================================================================--

# delete goal
def delete_goal(cursor, conn):
    goal_id = input("\t enter goal id you wanna delete >_ ")
    q = f"DELETE FROM goals WHERE goalid='{goal_id}'"
    try:
        cursor.execute(q)
        conn.commit()
    except:
        print("[!] ERROR! unable to delete goal.")
        input("")
    return

# new goal: create new goal
def newgoal(cursor, conn):
    name = input("\t name: ")
    dead = input("\t deadline: ")
    q = f"insert into goals (name, deadline) values ('{name}','{dead}')"
    try:
        cursor.execute(q)
        conn.commit()
    except:
        print("[!] failed to add new goal named %s",(name))
        input("[*] press enter to return to main menu")
    return

# view goal: viewing tasks in a goal
def view_goal(cursor, conn):
    return

# clean screen with logo
def clear():
    os.system("clear")
    os.system("echo WELCOME TO")
    os.system("figlet shellTask")


# authentication
def authentic():
    username = input("\t username: ")
    pass_str = getpass.getpass("\t password: ")

    try:
        mydb = mysql.connector.connect(
            host=config["DATABASE"]["host"],
            user=username,
            password=pass_str,
            database="shelltask",
        )
    except:
        print("[!] sonething went wrong")

    mycursor = mydb.cursor()

    querry = (
        f"select * from users where username='{username}' and password='{pass_str}'"
    )
    # print(querry)
    mycursor.execute(querry)
    result = mycursor.fetchone()
    if result:
        print("Welcome, " + username)
    else:
        print("Incorrect username or password.")
        clear()
        print("incorrect username or password")
        authentic()
    return (mydb, mycursor)


# MAIN ==========================================================================================================================================
def main():
    clear()

    # initialisations
    table = PrettyTable(["id", "goal", "dead line"])

    # authentication
    mydb, mycursor = authentic()
    user = User()

    # mainloop
    while True:
        clear()

        # options
        user.print_goals(mycursor)
        print("[ ] MAIN MENU:")
        print("  01: new goal")
        print("  02: remove goal")
        print("  03: view goal")
        print("  04: edit goal")
        print()

        choice = input("\t Choice >_ ")

        # 1 adding new goal
        if choice == "01":
            newgoal(mycursor, mydb)

        # 2 remove goal
        if choice == "02":
            delete_goal(mycursor, mydb)

        # 3 view goal
        if choice == "03":
            view_goal(mycursor, mydb)

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
