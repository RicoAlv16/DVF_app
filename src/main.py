import pandas as pd

def load_data():
	data_path = "data/valeursfoncieres-2023.csv"
	data = pd.read_csv(data_path, sep="|")
	print(data)



load_data()


