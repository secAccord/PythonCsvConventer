
import csv
import datetime

from scripts import addnow

def interpretation(file_name):
    tab_lines = []
    name = "ing"
    with open(f'input/{file_name}', mode='r') as file:
        l = 0

        for lines in file.read().splitlines():
            #temp_tab = []

            if l == 0 :
                l +=1
                continue
            #print(lines)
            temp_tab = ( lines.split(";") )
            #print(temp_tab)

            pay , num = addnow.price(temp_tab[-3])
            windraw = 0
            if (pay):
                windraw = num
                num = 0

            date = temp_tab[1].split("-")
            okres = date[2] + "." + date[1]
            new_date = date[2] + "-" + date[1] + "-" + date[0]

            temp_tab = [okres, new_date, new_date, temp_tab[3], temp_tab[4], "", "", "\"ING PLN\"", windraw, num]
            tab_lines.append(addnow.tab_to_string(temp_tab))
    now = datetime.datetime.now()
    tab_lines.reverse()
    name = f"{name}_{now.strftime('%Y-%m-%d_%H-%M-%S')}"
    addnow.recreate_csv(tab_lines, f"{name}.csv")
    return