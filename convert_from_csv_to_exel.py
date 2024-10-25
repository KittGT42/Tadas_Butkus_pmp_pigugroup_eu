import pandas as pd

read_file = pd.read_csv('detailed_info_product_24_10_2024.csv')
read_file.to_excel('detailed_info_excel.xlsx', index=None, header=True)