# This is a sample Python script.
import datetime
import os

import csv

from scripts import file, mbank, ing

def App(bank_name = "mbank"):
    temp_file = file.list_csv_files("input")

    if (bank_name == "mbank"):
        mbank.interpretation(temp_file[0])
    elif (bank_name == "ing"):
        ing.interpretation(temp_file[0])

    os.remove("input/" + temp_file[0])






