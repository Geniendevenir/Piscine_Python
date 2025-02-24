import pandas as pd

team_sports = ['Basketball', 'Football', 'Tug-Of-War', 'Badminton', 'Sailing',
'Handball', 'Water Polo', 'Hockey', 'Rowing', 'Bobsleigh', 'Softball',
'Volleyball', 'Synchronized Swimming', 'Baseball', 'Rugby Sevens',
'Rugby', 'Lacrosse', 'Polo']

def how_many_medals_by_country(df, country):
	reccord = {}
	sort_team = df[(df['NOC'] == country)]
	first_olympic = df['Year'].min()
	last_olympic = df['Year'].max()
	
	for year in range(first_olympic, last_olympic + 1):
		if (year - first_olympic) % 4 == 0:
			gold_medals = sort_team[(sort_team['Year'] == year) & (sort_team['Medal'] == 'Gold')]
			silver_medals = sort_team[(sort_team['Year'] == year) & (sort_team['Medal'] == 'Silver')]
			bronze_medals = sort_team[(sort_team['Year'] == year) & (sort_team['Medal'] == 'Bronze')]
			count_gold = len(gold_medals)
			count_silver = len(silver_medals)
			count_bronze = len(bronze_medals)
			reccord[year] = {'G':count_gold, 'S':count_silver, 'B':count_bronze}
	print(reccord)

	#per_year = sort_team[(sort_team['Year'] - 1896) % 4 == 0]

	#df[(df['Medal'] == 'Gold') & df['Year']]

