import pandas as pd

read_file = pd.read_csv('data.csv')
read_file.to_excel('table.xlsx', index=False, header=True)