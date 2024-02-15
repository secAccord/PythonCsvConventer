# This is a sample Python script.
from typing import Any

import csv


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def recreate_csv(tab):
    return
def price(num):

     num = float(num)
     if(num < 0):
         num *= -1
         return True , num
     return False, num

def mBank_interpretation():
    with open('historia.csv', mode='r') as file:
        csvFile = csv.reader(file)
        l = 0
        for lines in csvFile:
            if l == 0 :
                l +=1
                continue
            tab = lines[0].split(";")
            tab.extend(lines[1].split(";"))
            print(tab)
            pay , num = price(tab[4])
            windraw = 0
            if(pay):
                windraw = num
                num = 0
            print(windraw ,num)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mBank_interpretation()


