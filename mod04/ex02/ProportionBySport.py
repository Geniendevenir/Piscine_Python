import pandas as pd

def proportion_by_sport(df, year, sport, gender):
	filter_total = df[(df['Year'] == year) & (df['Sex'] == gender)]
	total_unique = filter_total['ID'].unique()
	total = len(total_unique)

	filter_portion = filter_total[filter_total['Sport'] == sport]
	portion_unique = filter_portion['ID'].unique()
	portion = len(portion_unique)
	print(portion / total)
