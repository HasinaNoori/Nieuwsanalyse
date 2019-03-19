import csv
import re
import pandas as df


with open("Data/nu_nl.csv")as csv_file:
    reader = csv.DictReader((l.replace('\0', '') for l in csv_file))
    for x in reader:
        bad_characters= [",", "'", "</a>", "<a href=", "<em>", "</em>", "<span>", "</span>", "target=", "_blank", ">", "", "&nbsp;", "\""]
        # print(x["Content"])
        row = x["Content"]
        for char in bad_characters:
            row = row.replace(char, "")
        print(row)