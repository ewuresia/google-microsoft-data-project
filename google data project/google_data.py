import pandas as pd
import zipfile
import kaggle
import csv

financial_data = 'financial-statements-of-major-companies2009-2023.zip'
with zipfile.ZipFile(financial_data, 'r') as file:
    file.extractall()

f = open('Financial Statements.csv', 'r')
reader = csv.reader(f)
data_info = next(reader)

#sorting out microsoft and google finance data.
with open('google_finance_data.csv', 'w', newline ='') as g_file:
    with open('microsoft_finance_data.csv', 'w', newline ='') as m_file:
        writer1 = csv.writer(g_file)
        writer2 = csv.writer(m_file)
        writer1.writerow(data_info)
        writer2.writerow(data_info)
        for row in reader:
            if row[1] == 'GOOG':
                writer1.writerow(row)
            elif row[1] == 'MSFT':
                writer2.writerow(row)


google_data = pd.read_csv("google_finance_data.csv")
microsoft_data = pd.read_csv("microsoft_finance_data.csv")
all_data = pd.read_csv("Financial Statements.csv")




