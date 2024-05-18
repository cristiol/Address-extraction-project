import pandas as pd

df = pd.read_parquet("../input_files/list of company websites.snappy.parquet")
val = df.values
links = [f'https://{link[0]}' for link in val]

























