

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
     num = num.replace(",", ".")
     num = float(num)
     if(num < 0):
         num *= -1
         return True , num
     return False, num
