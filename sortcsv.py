# TODO: Package for deployment to both Linux and Windows

# sort csv by first column
import csv
import pprint
from operator import itemgetter
import math
from pathlib import Path
import os
import sys

if getattr(sys, 'frozen', False):
    extDataDir = sys._MEIPASS
    extDataDir = os.path.join(extDataDir, 'sample.csv')
else:
    extDataDir = os.getcwd()
    extDataDir = os.path.join(extDataDir, 'sample.csv')

filetoopen = input("Please type the filename of the .csv file you would like to open: \n")

file = open("{}".format(filetoopen), "r")
csvfile = csv.reader(file, delimiter=",")
items = []

for eachline in csvfile:
    # if csvfile.line_num in range(4):
    #     continue
    # else:
    items.append(eachline)


def isint(num):
    try:
        int(num)
        return True
    except:
        return False


def number():
    for item in items:
        isanum = False
        # print(item[0])
        isanum = isint(item[0])
        # print(isanum)
        if isanum == True:
            item[0] = int(item[0])
            # print(item[0])
        else:
            continue


def linesfunc(l, n):
    for i in range(0, int(len(l)), int(n)):
        yield l[i:i + int(n)]


def testsort(ts):
    if ts == '1' or ts == '0':
        return True
    else:
        return False


def sortfunc(test, sort):
    # this puts the user in an endless loop if they choose an invalid input - fix it
    while test is False:
        newbool = input("I\'m sorry, but that is not a valid input.  Please enter 1 for ascending order \n"
              "or 0 for descending.  Thank you!\n")
        boolcheck(newbool)
        testsort(newbool)
    if sort is True:
        return pprint.pprint(sorted(items[3:-2], key=itemgetter(0)))
    else:
        return pprint.pprint(sorted(items[3:-2], key=itemgetter(0), reverse=True))


def boolcheck(bool):
    if bool == '1':
        ad_bool = True
    elif bool == '0':
        ad_bool = False
    else:
        ad_bool = None
        print("Invalid Input")
    return ad_bool


number()


def splitcsv():
    lines = input("How many lines would you like each output file to have?  ")
    asc_desc = input("Would you like the data to be sorted in ascending or descending order?  \n"
                     "Choose 1 for ascending or 0 for descending. \n ")
    # sortcolumn = input("Which column would you like to sort by?  ")

    print("Parameter 1:  Number of lines in each file = {} \n"  # trailing parentheses is just a placeholder
          "Parameter 2:  Ascending / Descending = {}\n".format(lines, asc_desc))
    # "Parameter 3:  Column to be sorted by = {}".format(lines, asc_desc, sortcolumn))


# These functions seem unnecessary if I am not going to be error checking.

    # ad_bool = boolcheck(asc_desc)

    # ad_input = testsort(asc_desc)
    # sort = sortfunc(ad_input, ad_bool)

    # output = linesfunc(items, lines)

    if asc_desc == '1':
        ascending = sorted(list(items[3:-2]), key=itemgetter(0))
        output = list(linesfunc(ascending, lines))
    elif asc_desc == '0':
        descending = sorted(list(items[3:-2]), key=itemgetter(0), reverse=True)
        output = list(linesfunc(descending, lines))

    files = math.ceil(len(items[3:-2]) / int(lines))
    filecount = 0
    while filecount < files:
        outfile = Path("outfile{}.csv".format(filecount))
        if outfile.is_file():
            print("There is a file named {}".format(outfile))
            with open('outfile{}.csv'.format(filecount), 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(list(items[0:3]))
                writer.writerows(output[filecount])
                writer.writerows(list(items[-2:]))
        else:
            print("The file outfile{}.csv does not exist".format(filecount))

            with open('outfile{}.csv'.format(filecount), 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(list(items[0:3]))
                writer.writerows(output[filecount])
                writer.writerows(list(items[-2:]))
            # csv.writer()
        filecount += 1


splitcsv()
