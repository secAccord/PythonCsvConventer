
import csv
import datetime

from scripts import addnow

def interpretation(file_name):
    tab_lines = []
    name = "mBank"
    with open(f'input/{file_name}', mode='r') as file:
        csvFile = csv.reader(file)
        l = 0
        for lines in csvFile:
            if l == 0 :
                l +=1
                continue
            tab = lines[0].split(";")
            tab.extend(lines[1].split(";"))
            tab = addnow.tab_el_remove_white(tab)
            #print(tab)
            pay , num = addnow.price(tab[4])
            windraw = 0
            if(pay):
                windraw = num
                num = 0

            date = tab[8].split("/")
            okres = date[2] + "." + date[1]
            new_date = date[2] + "-" + date[1] + "-" + date[0]


            temp_tab = [okres,new_date,new_date,tab[12],tab[11],"","","\"mBank PLN\"",windraw,num]

            tab_lines.append(addnow.tab_to_string(temp_tab))
    now = datetime.datetime.now()
    name = f"{name}_{now.strftime('%Y-%m-%d_%H-%M-%S')}"
    addnow.recreate_csv(tab_lines, f"{name}.csv")
    return
