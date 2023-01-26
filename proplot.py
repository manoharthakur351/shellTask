#!/bin/python
import shutil

# basic iniatialisation
rows, columns = shutil.get_terminal_size()
print(rows, columns)

# CONSTANTS
LABELXPAD=1
LABELYPAD=3

# TEST DATA
x = (1,2,3,4,5,6)
y = (3,8,5,9,4,9)

# FUNCTIONS
# data_valid: check wheather data is valid or not
def data_valid(x = None, y = None, xy = None):
    print()
# MAIN
def proplot ():
    pass



proplot()


# TEST CODE

a , b = input("a: "), input("b: ")
ab = ((1,2),(2,3))
print(data_valid(x=a,y=b))
