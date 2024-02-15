# This is a sample Python script.
import datetime
import os
from typing import Any
from os import listdir
import csv
import sys
import file


def tab_to_string(tab):
    string = ""
    for i in tab:
        string += f"{i};"
    return string
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def recreate_csv(tab, file_name):
    with open(file_name, mode='w') as file:
        for lines in tab:
            file.write(lines + "\n")
    return
def tab_el_remove_white(tab):
    for i in range(len(tab)):
        tab[i] = tab[i].replace("\"", "")
    return tab
def price(num):

     num = float(num)
     if(num < 0):
         num *= -1
         return True , num
     return False, num

def mBank_interpretation(file):
    tab_lines = []
    name = "mBank"
    with open(f'input/{file}', mode='r') as file:
        csvFile = csv.reader(file)
        l = 0
        for lines in csvFile:
            if l == 0 :
                l +=1
                continue
            tab = lines[0].split(";")
            tab.extend(lines[1].split(";"))
            tab = tab_el_remove_white(tab)
            print(tab)
            pay , num = price(tab[4])
            windraw = 0
            if(pay):
                windraw = num
                num = 0

            date = tab[8].split("/")
            okres = date[2] + "." + date[1]
            new_date = date[2] + "-" + date[1] + "-" + date[0]


            temp_tab = [okres,new_date,new_date,tab[12],tab[11],"","","\"mBank PLN\"",windraw,num]

            tab_lines.append(tab_to_string(temp_tab))

    now = datetime.datetime.now()
    name = f"{name}_{now.strftime('%Y-%m-%d_%H-%M-%S')}"
    recreate_csv(tab_lines, f"{name}.csv")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    temp_file = file.list_csv_files("input")

    #print(temp_file[0])
    if(sys.argv[1] == "mBank"):
        mBank_interpretation(temp_file[0])
    elif(sys.argv[1] == "ing"):
        print("ing")
    os.remove("input/" + temp_file[0])



