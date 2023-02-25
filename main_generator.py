import os
import csv
from tqdm import tqdm
import pandas as pd
from helpers.check_criteria import *
from dotenv import load_dotenv
load_dotenv(".env")

file_name = os.environ["CSV_URI"]

def csv_reader(file_name):
    headers = False
    counter = 0
    with tqdm(open(file_name, "rt")) as csv_file:
        reader = csv.reader(csv_file)
        for row in zip(reader):
            counter += 1
            if counter > 100000:
                break
            if not headers:
                headers = row[0]
                continue
            else:
                if row[0][2] == "7E3":
                    print(row[0])
                row_dict = dict(zip(headers, row[0]))
                yield check_criteria(row_dict)


arr = np.fromiter(csv_reader(file_name=file_name), dtype=object)

df = pd.json_normalize(arr)

# df_list = [item for item in csv_reader(file_name)]