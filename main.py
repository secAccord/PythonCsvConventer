# This is a sample Python script.
import datetime
import os

import csv
import sys
from scripts import file, mbank, ing

if __name__ == '__main__':
    temp_file = file.list_csv_files("input")

    #print(temp_file[0])
    if(sys.argv[1] == "mBank"):
        mbank.interpretation(temp_file[0])
    elif(sys.argv[1] == "ing"):
        ing.interpretation(temp_file[0])
    #os.remove("input/" + temp_file[0])



